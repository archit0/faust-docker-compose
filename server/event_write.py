import json
from datetime import datetime
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer_instance = KafkaProducer(bootstrap_servers=['kafka:9094'])

while True:
    key = input("Enter key name: ")
    value = input("Enter value name: ")


    key_bytes = bytes(json.dumps(key), encoding='utf-8')
    value_bytes = bytes(json.dumps(value), encoding='utf-8')

    topic_name = 'event_topic_write2'

    producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
    producer_instance.flush()

    print('Message published successfully at timestamp - {}'.format(datetime.now()))
