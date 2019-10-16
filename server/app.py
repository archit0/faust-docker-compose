import time
from faust import App
from datetime import datetime


app = App(
    'app_main',
    broker='kafka://kafka:9094',
    store='rocksdb://',
    table_standby_replicas=2,
)

read_topic = app.topic(
    'rr',
    partitions=2,
)

write_topic = app.topic(
    'ww',
    partitions=2,
)


table = app.Table(
    'test2_table',
    partitions=2,
)


@app.agent(read_topic)
async def read_topic_agent(streams):
    async for payload in streams:
        print("PRINTING ALL KEYS IN TABLE")
        for each_key in table:
            print(each_key)


@app.agent(write_topic)
async def write_topic_agent(streams):
    async for payload in streams:
        print("SETTING DATA", payload)
        table[payload['value']] = True


if __name__ == '__main__':
    app.main()
