resource "google_cloud_run_v2_service" "brewery_service" {
  name     = "brewery-service"
  location = var.region
  client   = "terraform"

  template {
    containers {
      image = "IMAGE"
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "noauth" {
  location = google_cloud_run_v2_service.brewery_service.location
  name     = google_cloud_run_v2_service.brewery_service.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}