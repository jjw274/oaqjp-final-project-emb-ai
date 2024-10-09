import requests
import json

def emotion_detector(text_to_analyze):

    if not text_to_analyze.strip():  # Check if the input text is empty or blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }, 400
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    # Define the input data format
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request to the Watson NLP API
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Convert the response to JSON format
    response_json = response.json()
    
    # Extract emotion scores
    emotions = response_json['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }, 200
