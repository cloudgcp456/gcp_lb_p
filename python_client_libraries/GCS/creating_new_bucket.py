from google.cloud import storage 
def create_uniform_bucket(bucket_name):
    """Create a new GCS bucket with uniform access and PAP enabled."""
    
    # Initialize client
    storage_client = storage.Client()

    # Create a new bucket object
    bucket = storage.Bucket(storage_client, name=bucket_name)

    # Set properties to match CLI command
    bucket.storage_class = "NEARLINE"
    bucket.location = "asia-south1"
    bucket.iam_configuration.uniform_bucket_level_access_enabled = True
    bucket.iam_configuration.public_access_prevention = "enforced"

    # Create the bucket
    new_bucket = storage_client.create_bucket(bucket)
    print(f"✅ Bucket {new_bucket.name} created successfully.")
    print(f"📦 Storage class: {new_bucket.storage_class}")
    print(f"🌍 Location: {new_bucket.location}")
    print(f"🔒 Uniform access: {new_bucket.iam_configuration.uniform_bucket_level_access_enabled}")
    print(f"🚫 Public Access Prevention: {new_bucket.iam_configuration.public_access_prevention}")

if __name__ == "__main__":
    create_uniform_bucket("demo2-uniform-bucket-demo123")
