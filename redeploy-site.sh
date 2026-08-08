#!/bin/bash

echo "🔄 Starting automated site redeployment..."

# 1. Navigate to the project folder
echo "📁 Navigating to project folder..."
cd /root/Sub-Challenges/pe-portfolio-site || exit

# 2. Fetch and hard reset to latest main branch
echo "📥 Fetching latest changes from GitHub..."
git fetch && git reset origin/main --hard

# 3. Spin down existing containers to prevent OOM issues during build
echo "🛑 Stopping running Docker containers..."
docker compose -f docker-compose.prod.yml down

# 4. Rebuild and restart production containers in detached mode
echo "🚀 Building and starting containers..."
docker compose -f docker-compose.prod.yml up -d --build

echo "✅ Redeployment complete!"