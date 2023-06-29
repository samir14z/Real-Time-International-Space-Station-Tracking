from kafka import KafkaProducer
import requests
import json
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

while True:
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    print(data)
    producer.send('my-topic', json.dumps(data).encode('utf-8'))

    time.sleep(5)
    
