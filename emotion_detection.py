"""Emotion detection module for earlier IBM lab activities.

Supports both direct invocation and import from earlier lab exercises.
"""
from EmotionDetection.emotion_detection import emotion_detector

if __name__ == '__main__':
    statement = "I am glad this happened"
    print(f"Analyzing text: '{statement}'")
    response = emotion_detector(statement)
    print("Result:", response)
