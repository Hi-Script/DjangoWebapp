from storages.backends.s3boto3 import S3Boto3Storage


class MediaStore(S3Boto3Storage):
    bucket_name = 'mysitehome'
    location = "media"
    file_overwrite = False
    custom_domain = '{}.s3.amazonaws.com'.format('mysitehome')


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'

    