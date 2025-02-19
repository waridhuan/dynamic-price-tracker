#!/bin/bash

# Set variables
IMAGE_NAME="price-tracker"
IMAGE_TAG="latest"

# Build the Docker image
echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

# Test the image by running it
echo "Testing Docker image..."
docker run -d --name price-tracker-test -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}

# Wait for the container to start
sleep 5

# Test the API
echo "Testing API endpoint..."
curl -X GET http://localhost:8000/

# Clean up
docker stop price-tracker-test
docker rm price-tracker-test

echo "Docker image built and tested successfully!"