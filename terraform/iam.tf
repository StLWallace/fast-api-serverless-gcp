# Create a service account for the Cloud Run deployment
resource "google_service_account" "cloud_run_fast_api" {
  account_id   = "cloud-run-fast-api-${var.environment}"
  display_name = "Cloud Run FastAPI ${var.environment}"
}


# Give the necessary roles to the Cloud Run SA
resource "google_project_iam_member" "project" {
  project = var.project_id
  role    = "roles/datastore.user"
  member  = google_service_account.cloud_run_fast_api.member
}