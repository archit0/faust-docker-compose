from kafka.admin import KafkaAdminClient, NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="kafka:9094", client_id='test')

topic_list = []
topic_list.append(NewTopic(name=input("Enter topic name: "), num_partitions=int(input("Enter partitions: ")), replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
