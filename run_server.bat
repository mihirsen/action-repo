@echo off
REM Start Flask app in a new terminal
start cmd /k "python app.py"

REM Wait a few seconds for Flask to start
ping 127.0.0.1 -n 5 > nul

REM Start ngrok for port 5000
start cmd /k "ngrok http 5000"

echo Flask and ngrok started. Use the ngrok HTTPS URL for your GitHub webhook.
pause 