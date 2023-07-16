// Authenticate
gcloud auth configure-docker us-east4-docker.pkg.dev

// Build image
./build_image.sh

// Create tag
docker tag fastapi-app:1.0.0 us-east4-docker.pkg.dev/personal-projects-388416/server-images-repositories-new/fastapi-app:1.0.0

// Push tag
docker push us-east4-docker.pkg.dev/personal-projects-388416/server-images-repositories-new/fastapi-app:1.0.0

// To check existing tags
docker images fastapi-app --format="{{ .Tag }}"
