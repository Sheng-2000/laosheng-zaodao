#!/usr/bin/env python3
"""Sync local files to Tencent COS bucket."""
import os
import sys
from qcloud_cos import CosConfig, CosS3Client

secret_id = os.environ['SECRET_ID']
secret_key = os.environ['SECRET_KEY']
bucket = os.environ['BUCKET']
region = os.environ['REGION']

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)

# Exclude patterns
EXCLUDE = {'.git', '.github', '.codebuddy', '.workbuddy'}
EXCLUDE_FILES = {'sync_github.sh', '生成规范.md', 'template.html'}

def should_upload(filepath):
    parts = filepath.replace('\\', '/').split('/')
    for ex in EXCLUDE:
        if ex in parts:
            return False
    filename = os.path.basename(filepath)
    return filename not in EXCLUDE_FILES

# Get all objects currently in bucket
existing_keys = set()
marker = ''
while True:
    resp = client.list_objects(Bucket=bucket, Prefix='', Marker=marker, MaxKeys=1000)
    if 'Contents' in resp:
        for obj in resp['Contents']:
            existing_keys.add(obj['Key'])
    if resp.get('IsTruncated'):
        contents = resp.get('Contents', [])
        marker = contents[-1]['Key'] if contents else ''
    else:
        break

# Upload all local files
uploaded_keys = set()
for root, dirs, files in os.walk('.'):
    # Filter out excluded directories
    dirs[:] = [d for d in dirs if d not in EXCLUDE]
    for f in files:
        filepath = os.path.join(root, f)
        if not should_upload(filepath):
            continue
        key = filepath[2:]  # remove './'
        uploaded_keys.add(key)
        content_type = 'text/html' if f.endswith('.html') else \
                       'text/css' if f.endswith('.css') else \
                       'application/javascript' if f.endswith('.js') else \
                       'application/json' if f.endswith('.json') else \
                       'image/png' if f.endswith('.png') else \
                       'image/jpeg' if f.endswith(('.jpg', '.jpeg')) else \
                       'image/svg+xml' if f.endswith('.svg') else \
                       'application/octet-stream'
        try:
            client.put_object(
                Bucket=bucket,
                Key=key,
                Body=open(filepath, 'rb'),
                ContentType=content_type
            )
            print(f'  UP: {key}')
        except Exception as e:
            print(f'  FAIL: {key} - {e}', file=sys.stderr)

# Delete objects in bucket that no longer exist locally
to_delete = existing_keys - uploaded_keys
if to_delete:
    objects = [{'Key': k} for k in to_delete]
    client.delete_objects(Bucket=bucket, Delete={'Object': objects, 'Quiet': 'true'})
    for k in to_delete:
        print(f'  DEL: {k}')

print(f'Done! Uploaded {len(uploaded_keys)}, Deleted {len(to_delete)}')
