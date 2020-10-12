import cv2
from flask import Flask, render_template

app = Flask(__name__)


@app.route(methods=['POST'])
def main(link):
    cap = cv2.VideoCapture(link)
    while cap.isOpened():
        _, frame = cap.read()
        if not _:
            break

        frame = cv2.flip(frame, 1)
        cv2.imshow('Capture', frame)

    return render_template('resultsform.html', link=_)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


