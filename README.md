# Emotion detector
# Emotion Detection Web Application

## Overview

This project is a Flask-based web application that detects emotions from user-provided text using the IBM Watson NLP Emotion Prediction service. Users can enter text through a web interface, and the application returns emotion scores along with the dominant emotion.

## Features

* Detects the following emotions:

  * Joy
  * Anger
  * Fear
  * Disgust
  * Sadness
* User-friendly web interface
* Built with Flask
* Communicates with the IBM Watson NLP Emotion Prediction API

## Technologies Used

* Python 3
* Flask
* Requests
* HTML
* JavaScript
* Bootstrap

## Project Structure

```text
.
├── app.py
├── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/emotion-detector.git
```

2. Navigate to the project directory:

```bash
cd emotion-detector
```

3. Install the required package:

```bash
pip install flask requests
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5555
```

## Usage

1. Enter any English text into the input field.
2. Click **Run Sentimental Analysis**.
3. View the detected emotion scores and the dominant emotion.

## Note

This project uses the IBM Skills Network Watson NLP endpoint. The endpoint is intended for use within the IBM Skills Network lab environment. If the application is run locally, the API may not be reachable depending on network availability or access restrictions.

## Author

**Muhammad Usman Amjad**

BS Software Engineering
University of Agriculture Faisalabad
