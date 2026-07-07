from flask import Flask, render_template, request
from emotion_detection import emotion_detector
app = Flask(__name__)
wsgi_app = app.wsgi_app
@app.route('/')
def home():
    return render_template("index.html")
@app.route("/emotionDetector")
def detect():
    text = request.args.get("textToAnalyze")
    return emotion_detector(text)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
