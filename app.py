from flask import Flask, request, jsonify, render_template, abort
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# MongoDB setup
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["webhook_db"]
events_collection = db["events"]

# Optional: Load ngrok URL and webhook secret from .env
NGROK_URL = os.environ.get("NGROK_URL", "")
GITHUB_WEBHOOK_SECRET = os.environ.get("GITHUB_WEBHOOK_SECRET", "")

@app.route('/webhook', methods=['POST'])
def webhook():
    # Optional: Verify GitHub webhook secret if set
    if GITHUB_WEBHOOK_SECRET:
        signature = request.headers.get('X-Hub-Signature-256')
        # Add signature verification logic here if needed
        # If verification fails, abort(401)

    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    event_data = None

    if event_type == "push":
        event_data = {
            "type": "push",
            "author": payload["pusher"]["name"],
            "from_branch": None,
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    elif event_type == "pull_request":
        action = payload.get("action")
        pr = payload.get("pull_request", {})
        if action == "opened":
            event_data = {
                "type": "pull_request",
                "author": pr.get("user", {}).get("login"),
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("created_at")
            }
        elif action == "closed" and pr.get("merged"):
            event_data = {
                "type": "merge",
                "author": pr.get("user", {}).get("login"),
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("merged_at")
            }
    # Add more event types if needed

    if event_data:
        events_collection.insert_one(event_data)
        return jsonify({"status": "success"}), 201
    else:
        return jsonify({"status": "ignored"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    events = list(events_collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(20))
    return jsonify(events)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 