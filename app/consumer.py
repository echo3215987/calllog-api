from kafka import KafkaConsumer

consumer = KafkaConsumer('daily')
for message in consumer:
    print (message)