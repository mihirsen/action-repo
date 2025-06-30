Webhook Receiver Project

This project receives GitHub webhook events (push, pull request, merge) and displays them in a minimal UI, polling MongoDB every 15 seconds.

Setup Instructions

1. Install dependencies:
   pip install -r requirements.txt

2. Start MongoDB:
   If you have MongoDB installed locally, run: mongod
   Or use a cloud MongoDB URI (see .env section below).

3. Run the Flask app:
   python app.py

4. Expose your local server to the internet (for GitHub webhooks):
   Download ngrok from https://ngrok.com/download
   In a new terminal, run: ngrok http 5000
   Copy the HTTPS URL shown (for example, https://abcd1234.ngrok.io).

5. Set up the webhook in your GitHub repository:
   Go to your action-repo on GitHub.
   Navigate to Settings, then Webhooks, and click Add webhook.
   Payload URL: Use your ngrok HTTPS URL with /webhook appended (for example, https://abcd1234.ngrok.io/webhook)
   Content type: application/json
   Events: Select Push and Pull Request
   Save the webhook.

6. View the UI:
   Open http://localhost:5000/ in your browser to see the latest events.

Environment Variables (.env)

MONGO_URI: MongoDB connection string (default is mongodb://localhost:27017/)
NGROK_URL: Your current ngrok public URL (update this each time you restart ngrok)
GITHUB_WEBHOOK_SECRET: Optional, set this if you use a secret in your GitHub webhook

Notes

- Merge events are captured as pull requests closed with merged: true.
- The UI polls for new events every 15 seconds.
- You can inspect incoming webhook requests using the ngrok dashboard at http://127.0.0.1:4040

Troubleshooting

- If you do not see events, ensure your Flask app, MongoDB, and ngrok are all running.
- Double-check that your webhook URL in GitHub matches your current ngrok URL.
- Use the ngrok dashboard to debug incoming requests and responses.
