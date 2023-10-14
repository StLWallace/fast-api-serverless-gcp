variable "project_id" {
  description = "Google Cloud project ID for deployment"
  type        = string
}

variable "region" {
  description = "Default region for deployment"
  type        = string
}

variable "zone" {
  description = "Default zone for deployment"
  type        = string
}

variable "environment" {
  description = "Cloud environment name. Usually something like 'dev', 'test', 'qa', 'prod'"
  type        = string
}
