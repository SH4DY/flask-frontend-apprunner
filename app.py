from flask import Flask
from flask import render_template
import boto3
app = Flask(__name__)

@app.route('/')
def hello_world():
    contents = show_image("my-flask-bucket")
    return render_template('collection.html', contents=contents)

def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            # print(f'Item:  {item}')
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls