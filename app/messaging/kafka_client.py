from kafka import KafkaProducer, KafkaConsumer

class KafkaClient:
    def __init__(self, servers):
        self.producer = KafkaProducer(bootstrap_servers=servers)
        self.consumer = KafkaConsumer(bootstrap_servers=servers)
    def send(self, topic, value):
        self.producer.send(topic, value.encode('utf-8'))

    def consume(self, topic):
        self.consumer.subscribe([topic])
        for message in self.consumer:
            print(message.value)
