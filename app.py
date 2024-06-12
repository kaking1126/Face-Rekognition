from flask import Flask, render_template, Response, jsonify
from camera import VideoCamera
from aws_rekonition import rekonition
import json
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('stream.html')


def gen(camera):
    while True:
        frame = camera.get_frame()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face_detail')
def face_detail():
    cap = open("opencv_frame.png", "rb")
    face_detail = rekonition(cap.read())
    return jsonify(face_detail)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
