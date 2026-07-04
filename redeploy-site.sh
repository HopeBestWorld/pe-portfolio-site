#!/bin/bash

# 1. Kill all existing tmux sessions to stop the background Flask server
echo "Killing existing tmux sessions..."
tmux kill-server 2>/dev/null

# 2. Navigate directly into project directory
echo "Navigating to project folder..."
cd /root/Sub-Challenges/pe-portfolio-site || { echo "Directory not found"; exit 1; }

# 3. Fetch latest code changes from GitHub and force update
echo "Fetching latest changes from GitHub..."
git fetch --all
git reset origin/main --hard

# 4. Enter python virtual environment and update dependencies
echo "Activating virtual environment and updating dependencies..."
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 5. Start a new detached Tmux session and run the server
echo "Launching Flask app inside a new detached tmux session..."
tmux new-session -d -s portfolio

# Send the activation and startup commands directly to the background tmux session
tmux send-keys -t portfolio "cd /root/Sub-Challenges/pe-portfolio-site && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0" C-m

echo "Deployment complete! Your updated site is live."
