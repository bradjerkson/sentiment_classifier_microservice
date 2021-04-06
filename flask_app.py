import json

from transformers import pipeline
from flask import Flask, request, jsonify


app = Flask(__name__)
model = pipeline("sentiment-analysis")

@app.route("/analysis", methods=['POST'])
def default():
    """
    Listens for a POST request, and feeds request into classifier. Returns result.
    """
    print("starting")

    input = request.get_json(force=True)
    print("Received: ", input)
    #Handle JSON input that's stringified
    if(type(input) is not dict):
        supplied_text = json.loads(input)
    else:
        supplied_text = input

    label, confidence_score = classify_sentiment(supplied_text['text'])
    print("Labels: ", label, confidence_score)
    response = construct_response(label, confidence_score)
    print("Responding: ", response)
    return response


def classify_sentiment(supplied_text):
    """
    utilises transformers pipeline to classify sentiment of text
    """
    prediction = model(supplied_text)[0]
    label = prediction['label']
    confidence_score = prediction['score']
    return label, confidence_score

def construct_response(label, confidence_score):
    """
    formats a JSON response object to return to client
    """
    response = {}
    response['label'] = label
    response['confidence_score'] = confidence_score
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
