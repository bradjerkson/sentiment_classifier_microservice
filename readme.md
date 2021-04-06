# Novel Sentiment Classifier

## Starting Flask/Classifier Microservice

Requirements:
- Docker

```
  docker-compose up
  #docker-compose up -d to run this detached

  ./test_service.sh
```

Note: once the Docker container is attached & running, there may be up to a 60
second delay for the Flask service to launch on older hardware.

## Extension: Running Unit Testing

Requirements:
- Python 3.8 or later
```
  pip3 install -r requirements.txt
  pytest testing.py
```
