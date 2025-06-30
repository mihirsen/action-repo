@echo off
REM Install MongoDB Community Edition using Chocolatey
choco install mongodb-community -y

echo MongoDB installation initiated. If you see 'installed successfully', MongoDB is ready.
pause 

mongo 