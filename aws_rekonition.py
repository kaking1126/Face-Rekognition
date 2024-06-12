import sys
import os
from flask import Flask, request, render_template
import base64
import boto3
import json


def rekonition(cap):
    client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id='AccessKey',
                          aws_secret_access_key='SecretKey')
    response = client.detect_faces(Image={'Bytes': cap}, Attributes=[
        'ALL'
    ])
    face_detail = json.dumps(response['FaceDetails'])
    return face_detail
