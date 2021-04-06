import json
import pytest
import requests

from transformers import pipeline

LOCALHOST_URL = "http://127.0.0.1:80/"
LOCALHOST_REQUEST = "analysis"

class Tester:
    def __init__(self, url, message, type):
        self.set_url(url)
        self.set_message(message)
        self.set_content_type(type)
    def set_message(self, message):
        self.message = {"text": message}
    def set_content_type(self, type):
        self.content_type = {'Content-type': type}
    def set_url(self, url):
        self.url = url
    def post_request(self):
        response = requests.post(self.url, json=self.message,
                                headers=self.content_type)
        return response

@pytest.mark.skip()
def test_sentiment_text(message):
    type = "application/json"
    test_request = Tester(LOCALHOST_URL + LOCALHOST_REQUEST, message, type)
    response = test_request.post_request()
    print((response.json()))
    #string = response.json()
    return response.json()
    #return json.loads(string)


def test_positive_sentiment_text():
    """
    Given: We have sentiment classifier and a flask API
    When: We provide a positive-sentiment text string...
    Then: We receive a POSITIVE label
    """
    message = "I love going to the park!"
    response = test_sentiment_text(message)
    assert response['label'] == 'POSITIVE'

def test_negative_sentiment_text():
    """
    Given: We have sentiment classifier and a flask API
    When: We provide a negative-sentiment text string...
    Then: We receive a NEGATIVE label
    """
    message = "I am having an awful day!"
    response = test_sentiment_text(message)
    assert response['label'] == 'NEGATIVE'
