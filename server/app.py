import time
import asyncio
from datetime import datetime
from faust import App


app = App(
    'app_main',
    broker='kafka://kafka:9094',
    store='rocksdb://',
    version=1,
)

PARTITITONS = 2


event_topic = app.topic(
    'event_topic_write2',
    internal=True,  # when internal=True, faust is responsible for creation and deletion of topics (default=False, kafka creates topic with default attributes for partition and others)
    partitions=PARTITITONS,
)

event_table = app.Table(
    'event_table2',
    partitions=PARTITITONS,
)


@app.agent(event_topic)
async def event_topic_write(streams):
    async for payload in streams.events():
        print("Got data", payload)
        event_table[payload.key] = payload.value


@app.page('/event/{key}/')
@app.table_route(table=event_table, match_info='key')
async def get_event(self, request, key):
    print("Im here")
    return self.json({
        key: event_table[key],
    })



if __name__ == '__main__':
    app.main()
