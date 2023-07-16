#! /bin/bash

echo 'Removing tagged images'
docker rmi gcr.io/fastapi-app:1.0.0

echo 'Removing existing images'
docker rmi fastapi-app:1.0.0

echo 'Creating new image for fastapi-app'
docker build --tag fastapi-app:1.0.0 . --platform linux/amd64