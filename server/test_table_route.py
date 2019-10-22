import json
import time
import requests

from kafka import KafkaProducer

producer_instance = KafkaProducer(
    bootstrap_servers=['kafka:9094'],
)

HOST = "http://localhost"
PORT = "6067"
TOPIC = "event_topic_write2"
ROUTE = "event"
MAX_NUM = 10000

def put_data(num_events, from_num=0, topic_name=TOPIC):
    print(f"Adding {num_events} entries to topic: {topic_name}")
    start_time = time.time()
    for key in range(from_num, from_num+num_events):
        key_bytes = bytes(json.dumps(str(key)), encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=key_bytes)
        producer_instance.flush()
    end_time = time.time()
    print(f"Done adding data for {num_events} events in {end_time-start_time} seconds")


def get_data(num_events, from_num=0, route_name=ROUTE, topic_name=TOPIC):
    print(f"Retrieving {num_events} entries from topic: {topic_name} through route: {route_name}")
    start_time = time.time()
    for key in range(from_num, from_num+num_events):
        response = get_value(key, route_name)
        assert response == {str(key): str(key)}
    end_time = time.time()
    print(f"Done retrieving data for {num_events} events in {end_time-start_time} seconds")


def get_value(key, route_name=ROUTE):
    url = HOST+':'+PORT+'/'+route_name+'/'+str(key)+'/'
    response = requests.get(url=url)
    return response.json()


if __name__ == '__main__':
    put_data(MAX_NUM)
    get_data(MAX_NUM)
