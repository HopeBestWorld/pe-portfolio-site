#!/bin/bash

echo "🔄 Starting automated site redeployment..."

# 1. Navigate to the project folder
echo "📁 Navigating to project folder..."
cd /root/Sub-Challenges/pe-portfolio-site || exit

# 2. Fetch the absolute latest code changes from GitHub
echo "📥 Fetching latest changes from GitHub..."
git fetch --all
git reset --hard origin/main

# 3. Activate the virtual environment and install dependencies
echo "🐍 Activating virtual environment and updating dependencies..."
source python3-virtualenv/bin/activate
pip install -r requirements.txt
# Ensuring our database driver and crypto libraries are present
pip install pymysql cryptography

# 4. Restart the systemd portfolio service
echo "Restarting myportfolio systemd service..."
sudo systemctl restart myportfolio

echo "✅ Deployment complete! Updated site is live and running as a service."
