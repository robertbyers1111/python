#!/usr/bin/python3
import boto3
whatever = boto3.resource('s3')
for bucket in whatever.buckets.all():
    print(bucket.name())

