import boto3
from botocore.exceptions import NoCredentialsError
#Code from GPT4
def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except NoCredentialsError:
        return None

    # The response contains the presigned URL
    return response

bucket_name = 'my_bucket'
object_name = 'my_picture.jpg'
print(create_presigned_url(bucket_name, object_name))