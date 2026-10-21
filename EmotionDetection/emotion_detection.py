"""Module for emotion detection using Watson NLP Emotion Predict API."""
import json
import requests


def emotion_detector(text_to_analyze):
    """Detect emotions in the given text using Watson NLP Emotion Predict service.

    Args:
        text_to_analyze (str): Text to be analyzed.

    Returns:
        dict: Emotion scores for anger, disgust, fear, joy, sadness,
              and dominant_emotion. Returns None values for invalid input
              or HTTP 400 responses.
    """
    error_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyze or not str(text_to_analyze).strip():
        return error_response

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=5)
        if response.status_code != 200:
            return error_response

        formatted_response = json.loads(response.text)
        emotion_predictions = formatted_response.get('emotionPredictions', [])
        if not emotion_predictions:
            return error_response

        emotions = emotion_predictions[0].get('emotion', {})
        emotion_scores = {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness')
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }
    except (requests.exceptions.RequestException, KeyError, IndexError,
            json.JSONDecodeError, TypeError, ValueError):
        return error_response
