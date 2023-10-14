# fast-api-serverless-gcp
Example for creating a FastAPI deployment using Google Cloud serverless architecture. This creates a silly example service for storing information about breweries and beers. The service is deployed as a container on Google Cloud Run.


# Setup
Deploying this service to Google Cloud assumes you have a pre-existing GCS state bucket and Artifact Registry repository, as those are not configured here. 

Before running any steps, make sure you are authenticated to Google Cloud.

## Container build/push
Before doing the Terraform steps, build your image and push it to Artifact Registry.

Login:
```
gcloud auth configure-docker \
    {your region}-docker.pkg.dev
```

Set an environment variable for your GC project:  
```
export GCP_PROJECT={your project id}
```

Run the script to build, tag, and push your image:
```
./push-image-artifact-registry.sh
```
You can configure the repo, region, and image names by modifying this file

## Terraform
Before running Terraform steps, ensure that the Cloud Run Admin API is enabled for your Google Cloud project

For your backend config, create a file in the `/terraform/` directory called `backend_default.tfvars`. In that file include the following lines:
```
bucket = "{name of your GCS state bucket}"
prefix = "fast-api-serverless/default.tfstate"
```
You can set the prefix to whatever you prefer.

For your variables, create a file in the `/terraform/` directory called `default.tfvars`. In that file, include the following lines:
```
project_id  = "{Your Google Cloud project}"
region      = "{Region you want to use}"
environment = "default"
```

Run the Terraform steps from the `/terraform/` directory.
Initialize:
```
cd terraform
./scripts/init.sh
```
Plan:
```
./scripts/plan.sh
```
(If the plan looks good) Apply:
```
./scripts/apply.sh
```

If your apply succeeds, your app should now be running in Cloud Run

In a real production setting, it would be smart to consolidate the image build/push steps with the Terraform steps into a pipeline e.g. Cloud Build, Jenkins, etc.

Note: With the current setup, the Terraform plan won't detect changes if the image is updated since it's using the `latest` tag. Using the git commit hash instead would be a better production option.


# Testing the service on Cloud Run
By default, your service shouldn't allow unauthenticated traffic. To setup a proxy to make requests against it, use:
```
gcloud run services proxy brewery-service --project {your project}
```
After running this command, you should be able to navigate to the docs page in your browser or make requests via CURL or whatever at the local proxy url, which defaults to `http://127.0.0.1:8080`. Try opening `http://127.0.0.1:8080/docs` in your browser and using Swagger to test it out!