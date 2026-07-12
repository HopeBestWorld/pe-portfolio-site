#!/bin/bash

echo "=== Starting API Endpoints Test ==="

RANDOM_NUM=$((1000 + RANDOM % 9000))
TEST_NAME="Tester-$RANDOM_NUM"
TEST_EMAIL="tester$RANDOM_NUM@test.com"
TEST_CONTENT="Automated test content generation script #$RANDOM_NUM"

echo "Creating a new timeline post for $TEST_NAME..."

RESPONSE=$(curl -s -X POST http://localhost:5001/api/timeline_post \
  -d "name=$TEST_NAME" \
  -d "email=$TEST_EMAIL" \
  -d "content=$TEST_CONTENT")

POST_ID=$(echo "$RESPONSE" | grep -o '"id": *[0-9]*' | grep -o '[0-9]*')

if [ -z "$POST_ID" ]; then
    echo "❌ Error: Failed to create post or retrieve valid ID."
    exit 1
else
    echo "Success: Created post with ID: $POST_ID"
fi

echo "Checking GET endpoint for our new post..."
GET_RESPONSE=$(curl -s http://localhost:5001/api/timeline_post)

if [[ "$GET_RESPONSE" == *"$TEST_CONTENT"* ]]; then
    echo "Success: Found our unique test content in the timeline database!"
else
    echo "Error: Could not find the newly added post content in the GET response."
    exit 1
fi

echo "Cleaning up: Triggering DELETE for post ID: $POST_ID..."
DELETE_RESPONSE=$(curl -s -X DELETE http://localhost:5001/api/timeline_post -d "id=$POST_ID")

if [[ "$DELETE_RESPONSE" == *"Successfully deleted"* ]]; then
    echo "Success: Database cleaned up properly."
else
    echo "Warning: Cleanup failed or returned an unexpected message."
fi

echo "=== All Tests Completed Successfully ==="
