"""
Secrets for AWS keys , imported into settings.py
"""
AWS_ACCESS_KEY_ID = 'string'
AWS_SECRET_ACCESS_KEY = 'string'
AWS_STORAGE_BUCKET_NAME = 'my_bucket_name'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
