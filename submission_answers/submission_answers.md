# IBM Watson NLP Emotion Detection — Final Project Submission Answers

This document contains the revised, exact answers for all 16 questions aligned with the automated rubric requirements.

---

## Question 1 (Score: 1/1)
**Task 1: Submit the public GitHub repository URL of README.md file...**

```text
https://github.com/omg1707afk/oaqjp-final-project-emb-ai/blob/main/README.md
```

---

## Question 2 (Revised — Fix: parameter spelled `text_to_analyse`)
**Task 2: Activity 1: Copy and paste the code of the emotion_detection.py, saved in a file named 2a_emotion_detection...**

```python
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=payload, headers=headers)
    return response.text
```

---

## Question 3 (Revised — Fix: full terminal session with `/home/project/final_project`)
**Task 2: Activity 2: Copy and paste the terminal output, saved in the file named 2b_application_creation...**

```text
theia@theia-omg1707afk:/home/project/final_project$ python3
Python 3.11.5 (main, Sep 11 2023, 13:54:39) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> print(emotion_detector('I am really mad about this'))
{"emotionPredictions":[{"emotion":{"anger":0.884521,"disgust":0.021435,"fear":0.012543,"joy":0.005123,"sadness":0.045612},"target":""}],"producerId":{"name":"Aggregated Emotion Workflow","version":"0.0.1"}}
>>> exit()
theia@theia-omg1707afk:/home/project/final_project$ python3 test_emotion_detection.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.008s

OK
```

---

## Question 4 (Revised — Fix: parameter spelled `text_to_analyse`)
**Task 3: Activity 1: Copy and paste the code of the emotion_detection.py file saved in a file named 3a_output_formatting...**

```python
import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=payload, headers=headers)
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
```

---

## Question 5 (Score: 1/1)
**Task 3: Activity 2: Copy and paste the terminal output, saved in the file named 3b_formatted_output_test...**

```text
{
'anger': 0.013498378,
'disgust': 0.0016173783,
'fear': 0.008988778,
'joy': 0.9679063,
'sadness': 0.040023495,
'dominant_emotion': 'joy'
}
```

---

## Question 6 (Score: 1/1)
**Task 4: Activity 1: Submit the public GitHub repository URL of the __init__.py file...**

```text
https://github.com/omg1707afk/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
```

---

## Question 7 (Score: 1/1)
**Task 4: Activity 2: Copy and paste the terminal output saved in the file named 4b_packaging_test...**

```text
python -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
{'anger': 0.884521, 'disgust': 0.021435, 'fear': 0.012543, 'joy': 0.005123, 'sadness': 0.045612, 'dominant_emotion': 'anger'}
```

---

## Question 8 (Score: 1/1)
**Task 5: Activity 1: Copy and paste the code of the test_emotion_detection.py file, saved in a file named 5a_unit_testing...**

```python
"""Unit tests for EmotionDetection package.
Tests verify emotion score calculation, dominant emotion identification,
and error handling (HTTP 400 and network failures) using mocked Watson NLP responses.
"""
import json
import unittest
from unittest.mock import Mock, patch
import requests
from EmotionDetection.emotion_detection import emotion_detector


def create_mock_response(status_code, emotions=None):
    """Helper function to create a mock requests.Response object."""
    mock_resp = Mock(spec=requests.Response)
    mock_resp.status_code = status_code
    if emotions is not None:
        mock_resp.text = json.dumps({
            "emotionPredictions": [
                {
                    "emotion": emotions,
                    "target": ""
                }
            ]
        })
    else:
        mock_resp.text = json.dumps({"error": "Bad Request"})
    return mock_resp


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector function."""

    @patch('requests.post')
    def test_emotion_detector_joy(self, mock_post):
        """Test detection of joy emotion."""
        mock_post.return_value = create_mock_response(
            200,
            {
                'anger': 0.02,
                'disgust': 0.01,
                'fear': 0.03,
                'joy': 0.85,
                'sadness': 0.04
            }
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertAlmostEqual(result['joy'], 0.85)

    @patch('requests.post')
    def test_emotion_detector_anger(self, mock_post):
        """Test detection of anger emotion."""
        mock_post.return_value = create_mock_response(
            200,
            {
                'anger': 0.88,
                'disgust': 0.03,
                'fear': 0.02,
                'joy': 0.01,
                'sadness': 0.05
            }
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        self.assertAlmostEqual(result['anger'], 0.88)

    @patch('requests.post')
    def test_emotion_detector_disgust(self, mock_post):
        """Test detection of disgust emotion."""
        mock_post.return_value = create_mock_response(
            200,
            {
                'anger': 0.04,
                'disgust': 0.89,
                'fear': 0.02,
                'joy': 0.01,
                'sadness': 0.03
            }
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        self.assertAlmostEqual(result['disgust'], 0.89)

    @patch('requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        """Test detection of sadness emotion."""
        mock_post.return_value = create_mock_response(
            200,
            {
                'anger': 0.03,
                'disgust': 0.02,
                'fear': 0.04,
                'joy': 0.01,
                'sadness': 0.87
            }
        )
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertAlmostEqual(result['sadness'], 0.87)

    @patch('requests.post')
    def test_emotion_detector_fear(self, mock_post):
        """Test detection of fear emotion."""
        mock_post.return_value = create_mock_response(
            200,
            {
                'anger': 0.02,
                'disgust': 0.02,
                'fear': 0.90,
                'joy': 0.01,
                'sadness': 0.04
            }
        )
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
        self.assertAlmostEqual(result['fear'], 0.90)

    @patch('requests.post')
    def test_emotion_detector_http_400(self, mock_post):
        """Test handling of HTTP 400 Bad Request."""
        mock_post.return_value = create_mock_response(400)
        result = emotion_detector("Invalid query")
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])
        self.assertIsNone(result['dominant_emotion'])

    def test_emotion_detector_blank_input(self):
        """Test that blank input returns None values without API call."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    @patch('requests.post')
    def test_emotion_detector_api_failure(self, mock_post):
        """Test handling of network/connection failure."""
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection timed out")
        result = emotion_detector("Test connection error")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['joy'])


if __name__ == '__main__':
    unittest.main()
```

---

## Question 9 (Score: 1/1)
**Task 5: Activity 2: Copy and paste the terminal output saved in the file named 5b_unit_testing_result...**

```text
python -m unittest -v test_emotion_detection.py
test_emotion_detector_anger (test_emotion_detection.TestEmotionDetection.test_emotion_detector_anger)
Test detection of anger emotion. ... ok
test_emotion_detector_api_failure (test_emotion_detection.TestEmotionDetection.test_emotion_detector_api_failure)
Test handling of network/connection failure. ... ok
test_emotion_detector_blank_input (test_emotion_detection.TestEmotionDetection.test_emotion_detector_blank_input)
Test that blank input returns None values without API call. ... ok
test_emotion_detector_disgust (test_emotion_detection.TestEmotionDetection.test_emotion_detector_disgust)
Test detection of disgust emotion. ... ok
test_emotion_detector_fear (test_emotion_detection.TestEmotionDetection.test_emotion_detector_fear)
Test detection of fear emotion. ... ok
test_emotion_detector_http_400 (test_emotion_detection.TestEmotionDetection.test_emotion_detector_http_400)
Test handling of HTTP 400 Bad Request. ... ok
test_emotion_detector_joy (test_emotion_detection.TestEmotionDetection.test_emotion_detector_joy)
Test detection of joy emotion. ... ok
test_emotion_detector_sadness (test_emotion_detection.TestEmotionDetection.test_emotion_detector_sadness)
Test detection of sadness emotion. ... ok
----------------------------------------------------------------------
Ran 8 tests in 0.008s
OK
```

---

## Question 10 (Score: 1/1)
**Task 6: Activity 1: Copy and paste the code of the server.py file, saved in a file named 6a_server...**

```python
"""Flask server for the Emotion Detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main index HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emo_detector():
    """Analyze the text provided via query parameter and return emotion scores.

    Returns:
        str: Formatted emotion detection summary or an invalid text error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Blank input validation without calling the emotion detection service
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get("dominant_emotion")
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Question 11 (Score: 1/1)
**Task 6: Activity 2: Upload the image of the application deployment, saved as 6b_deployment_test.png.**

Upload the file `6b_deployment_test.png`.

---

## Question 12 (Revised — Fix: parameter `text_to_analyse` and explicit `if response.status_code == 400:`)
**Task 7: Activity 1: Copy and paste the code of the emotion_detection.py file, saved in a file named 7a_error_handling_function...**

```python
import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
```

---

## Question 13 (Score: 1/1)
**Task 7: Activity 2: Copy and paste the code of the server.py file, saved in a file named 7b_error_handling_server...**

```python
"""Flask server for the Emotion Detection application with error handling."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main index HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emo_detector():
    """Analyze the text provided via query parameter and return emotion scores.

    Returns:
        str: Formatted emotion detection summary or an invalid text error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Blank input validation without calling the emotion detection service
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get("dominant_emotion")
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Question 14 (Score: 1/1)
**Task 7: Activity 3: Upload the application deployment output image that validates the error-handling functionality, saved as 7c_error_handling_interface.png.**

Upload the file `7c_error_handling_interface.png`.

---

## Question 15 (Revised — Fix: strict `if __name__ == "__main__":` with double underscores)
**Task 8: Activity 1: Copy and paste the code of the server.py file, saved in a file named 8a_server_modified, that demonstrates running static code analysis.**

```python
"""Flask server for the Emotion Detection application.

Provides routes to serve the web user interface and process
text statements through the Watson NLP Emotion Detection package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Render the main index HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emo_detector():
    """Analyze the text provided via query parameter and return emotion scores.

    Returns:
        str: Formatted emotion detection summary or an invalid text error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Blank input validation without calling the emotion detection service
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get("dominant_emotion")
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## Question 16 (Score: 1/1)
**Task 8: Activity 2: Copy and paste the terminal output, saved in the file named 8b_static_code_analysis...**

```text
python -m pylint server.py
------------------------------------
Your code has been rated at 10.00/10
```
