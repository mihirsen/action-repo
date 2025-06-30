@echo off
REM Run this script as Administrator!
choco install ngrok -y
ngrok config add-authtoken 2zEB4zulLMnaDPfTiLnYiEGQDkS_5dFv7sUWK1y27a7DJnoYv

echo ngrok installed and authtoken set. You can now run: ngrok http 5000
pause 