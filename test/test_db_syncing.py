import time
from faust import App
from datetime import datetime


app = App(
    'test_syncing',
    broker='kafka://kafka:9094',
    store='rocksdb://',
)

write_topic = app.topic(
    'write_orders',
    value_type=bytes,
    partitions=1,
)

read_topic = app.topic(
    'read_orders',
    value_type=bytes,
    partitions=1,
)

sample_table = app.Table(
    'sample_table',
    partitions=1,
)


@app.agent(write_topic)
async def putting(streams):
    async for payload in streams:
        print("Putting Data")
        sample_table['key'] = 'Some Value'


@app.agent(read_topic)
async def reading(streams):
    async for payload in streams:
        print("Requesting Data")
        print(sample_table['key'])


if __name__ == '__main__':
    app.main()
