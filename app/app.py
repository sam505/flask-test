import cv2
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    count = 0
    # link = request.args.get("link")
    cap = cv2.VideoCapture('demo.mp4')
    while cap.isOpened():
        count += 1
        _, frame = cap.read()
        if not _:
            break

        frame = cv2.flip(frame, 1)
        cv2.imshow('Capture', frame)
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

    return jsonify(status=_, frames='{} frames'.format(count))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


