#! /bin/bash
# Create a variable for latest commit
commit_id=$(git log --format="%H" -n 1)
# Format the image name
image_name=us-central1-docker.pkg.dev/$GCP_PROJECT/brewery-service/brewery-service

docker build -t brewery-service:latest services/brewery-service

docker tag brewery-service $image_name:$commit_id

docker push $image_name:$commit_id

# Add "latest" tag to image
gcloud artifacts docker tags add $image_name:$commit_id $image_name:latest

echo $image_name