import time
from faust import App
from datetime import datetime


app = App(
    'app_main',
    broker='kafka://kafka:9094',
    store='rocksdb://',
)

topic = app.topic(
    'sample_topic',
    value_type=bytes,
    partitions=1,
)


@app.agent(topic)
async def read_topic(streams):
    async for payload in streams:
        print("RECEIVED:", payload)
        print("DONE")


if __name__ == '__main__':
    app.main()
