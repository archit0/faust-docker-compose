from faust import App
from faust.sensors.statsd import StatsdMonitor

app = App(
    'app_main',
    broker='kafka://kafka:9094',
    store='rocksdb://',
    monitor=StatsdMonitor(host='monitor'),
)

PARTITITONS = 2

# when internal=True, faust is responsible for creation and deletion of topics
# (default=False, kafka creates topic with default attributes for partition and others)
event_topic = app.topic(
    'event_topic_write2',
    internal=True,
    partitions=PARTITITONS,
)

global_topic = app.topic(
    'global_topic2',
    internal=True,
    partitions=PARTITITONS,
)

event_table = app.Table(
    'event_table2',
    partitions=PARTITITONS,
)

pseudo_global_table = app.Table(
    'global_event2',
    partitions=PARTITITONS,
)


@app.agent(event_topic)
async def event_topic_write(streams):
    async for payload in streams.events():
        print(f"Got data: {payload}")
        event_table[payload.key] = payload.value
        print(f"Local Table*************")
        for each_key in event_table:
            print(f"{each_key}: {event_table[each_key]}")
        # Uncomment below loop for pseudo_global_table implementation
        # for partition in range(PARTITITONS):
        #     await global_topic.send(key=payload.key, value=payload.value, partition=partition)


@app.agent(global_topic)
async def global_sync(streams):
    async for payload in streams.events():
        print(f"Pseudo-Global Table*************")
        pseudo_global_table[payload.key] = payload.value
        for each_key in pseudo_global_table:
            print(f"{each_key}: {pseudo_global_table[each_key]}")


@app.page('/event/{key}/')
@app.table_route(table=event_table, match_info='key')
async def get_event(self, request, key):
    print(f"Im here {key}")
    return self.json({
        key: event_table[key],
    })


if __name__ == '__main__':
    app.main()
