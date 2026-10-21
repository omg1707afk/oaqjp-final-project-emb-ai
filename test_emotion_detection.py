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
