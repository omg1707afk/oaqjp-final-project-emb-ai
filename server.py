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
