import boto3
from botocore.exceptions import NoCredentialsError
from urllib.parse import urlparse
#Code from GPT4
def create_presigned_url(full_bucket, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    #This is to split the link into 2 Parts.
    parsed = urlparse(full_bucket)

    bucket_name = parsed.netloc
    key = parsed.path.lstrip('/')

    print(bucket_name)  # prints: d-id-talks-persistent-prod
    print(key)  # prints: google-oauth2|113737039728929273410/tlk_nn9gFufcLwrXjHOnDGuAu/1690301426334.mp4

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': key},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        return None

    # The response contains the presigned URL
    return response


#bucket_name = 'my_bucket'
#object_name = 'my_picture.jpg'
print(create_presigned_url('s3://d-id-talks-persistent-prod/google-oauth2|113737039728929273410/tlk_nn9gFufcLwrXjHOnDGuAu/1690301426334.mp4'))
