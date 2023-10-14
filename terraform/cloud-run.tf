resource "google_cloud_run_v2_service" "brewery_service" {
  name     = "brewery-service"
  location = var.region
  client   = "terraform"

  template {
    containers {
      image = "${var.region}-docker.pkg.dev/${var.project_id}/brewery-service/brewery-service:latest"
      env {
        name  = "COLLECTION_NAME"
        value = "breweries"
      }
    }
  }
}

/*
resource "google_cloud_run_v2_service_iam_member" "noauth" {
  location = google_cloud_run_v2_service.brewery_service.location
  name     = google_cloud_run_v2_service.brewery_service.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
*/