import json
from datetime import datetime
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer_instance = KafkaProducer(bootstrap_servers=['192.168.31.10:9094'])

for i in range(0, 10):

    key_bytes = bytes(str(datetime.now()), encoding='utf-8')
    value = {
        'index': i,
        'timestamp': str(datetime.now()),
    }
    value_bytes = bytes(json.dumps(value), encoding='utf-8')

    topic_name = 'sample_topic'

    producer_instance.send(topic_name, key=None, value=value_bytes)
    producer_instance.flush()

    print('Message published successfully at timestamp - {}'.format(datetime.now()))
