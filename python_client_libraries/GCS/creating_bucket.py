from google.cloud import storage # library to interact with GCS


def create_bucket_class_location(bucket_name): # python function to create bucket
    """
    Create a new bucket in the US region with the coldline storage
    class
    """ 
    # docstring explaining the function
    # bucket_name = "third-bucket-lb"

    storage_client = storage.Client() # python class to create storage client

    # your python script from this machine will become like a client application to the gcs service of the gcp cloud

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE" # 
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket # return the created bucket object

result = create_bucket_class_location("third-bucket-lb") # call the function to create bucket
print(result)

# pip install google-cloud-storage
# python creating_bucket.py -- commplete location of the python file to run the script