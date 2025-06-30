# webhook-repo

This project receives GitHub webhook events (push, pull request, merge) and displays them in a minimal UI, polling MongoDB every 15 seconds.

## Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Start MongoDB

- If you have MongoDB installed locally, run:
  ```
  mongod
  ```
- Or use a cloud MongoDB URI (see .env section below).

### 3. Run the Flask app

```
python app.py
```

### 4. Expose your local server to the internet (for GitHub webhooks)

- Download ngrok from https://ngrok.com/download
- In a new terminal, run:
  ```
  ngrok http 5000
  ```
- Copy the HTTPS URL shown (e.g., `https://abcd1234.ngrok.io`).

### 5. Set up the webhook in your GitHub repo

- Go to your `action-repo` on GitHub.
- Settings > Webhooks > Add webhook.
- **Payload URL:** `https://abcd1234.ngrok.io/webhook`
- **Content type:** `application/json`
- **Events:** Select "Let me select individual events" and check **Push** and **Pull Request**.
- Save.

### 6. View the UI

- Open [http://localhost:5000/](http://localhost:5000/) in your browser.

## .env (Optional)

If you want to use a custom MongoDB URI, create a `.env` file:

```
MONGO_URI=mongodb://your-mongo-uri
```

## Notes

- Merge events are captured as pull requests closed with `merged: true`.
- The UI polls for new events every 15 seconds.
