import cv2
from flask import Flask, render_template, request, jsonify
import jwt
import requests


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    count = 0
    data = request.get_json()
    video = data["video_link"]
    # try:
    cap = cv2.VideoCapture(video)
    while cap.isOpened():
        count += 1
        _, frame = cap.read()
        if not _:
            break

        frame = cv2.flip(frame, 1)
    message = 'Video finished streaming without errors'

    cap.release()

    # except:
    #     message = 'There was an error capturing the video'

    return jsonify(student_id=data['student_id'],
                   exam_id=data['exam_id'],
                   results='{}%'.format(90),
                   frames='{} frames'.format(count),
                   message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


