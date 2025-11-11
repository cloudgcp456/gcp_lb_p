provider "google" {
  project = "alpine-guild-477901-v6"
  region  = "us-central1"
  zone    = "us-central1-c"
}

# Create GCS Bucket
resource "google_storage_bucket" "uniform_bucket" {
  name                        = "demo2-uniform-bucket-demo3"
  location                    = "ASIA-SOUTH1"
  storage_class               = "NEARLINE"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}
