import requests
import json
def emotion_detector(textToAnalyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    input_json = { 
        "raw_document": { 
        "text": textToAnalyze
        }
    }
    response = requests.post(URL,json = input_json, headers = headers)
    response_dir = response.json()
    emotion = response_dir["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion, key = emotion.get)
    return {
        "anger": emotion["anger"],
        "disgust": emotion["disgust"],
        "fear": emotion["fear"],
        "joy": emotion["joy"],
        "sadness": emotion["sadness"],
        "dominant_emotion": dominant_emotion
    }