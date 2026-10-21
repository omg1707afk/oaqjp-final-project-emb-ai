# Final Project

Emotion Detection web application built using Python, Flask, and the Watson NLP Emotion Prediction API. This application analyzes text statements to detect five primary emotions: anger, disgust, fear, joy, and sadness, and determines the dominant emotion.

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Running Unit Tests](#running-unit-tests)
- [Running Static Code Analysis](#running-static-code-analysis)
- [Running the Web Application](#running-the-web-application)
- [API Reference](#api-reference)

## Project Overview
This project is part of the IBM AI Developer Professional Certificate final assessment. It packages Watson NLP Emotion Prediction service into a reusable Python module and deploys a web application served using Flask.

## Project Structure
```text
oaqjp-final-project-emb-ai/
├── README.md
├── requirements.txt
├── emotion_detection.py
├── test_emotion_detection.py
├── server.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── mywebscript.js
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
└── submission_answers/
    └── submission_answers.md
```

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/omg1707afk/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Unit Tests
Execute the unit tests using Python's `unittest` framework:
```bash
python -m unittest test_emotion_detection.py
```

## Running Static Code Analysis
Verify code quality using `pylint`:
```bash
python -m pylint server.py
```

## Running the Web Application
Start the Flask development server:
```bash
python server.py
```
Open your web browser and navigate to:
```text
http://localhost:5000/
```

## API Reference
- **Route:** `/emotionDetector`
- **Method:** `GET`
- **Query Parameter:** `textToAnalyze`
- **Valid Response Format:**
  `For the given statement, the system response is 'anger': <val>, 'disgust': <val>, 'fear': <val>, 'joy': <val> and 'sadness': <val>. The dominant emotion is <b><dominant_emotion></b>.`
- **Invalid/Blank Input Response:**
  `Invalid text! Please try again!`
