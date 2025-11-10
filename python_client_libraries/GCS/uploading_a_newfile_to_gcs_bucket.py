# i need to upload a file from the same location into a gcs bucket

from google.cloud import storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "third-bucket-lb"
    # source_file_name = "C:\\NOVGCP\\gcp_lb_p_clean\\python_client_libraries\\GCS\\creating_bucket.py"
    destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )   

upload_blob("third-bucket-lb", "C:\\NOVGCP\\gcp_lb_p_clean\\python_client_libraries\\GCS\\creating_bucket.py", "storage-object-name")    