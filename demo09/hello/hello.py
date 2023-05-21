from flask import Flask, request
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/')
@app.route('/hello')
def hello():
    msg = {"msg": "Hello"}
    producer.send('test', msg)
    return "Hello"

if __name__ == "__main__":
    service_name = 'hello'
    service_port = 5000

    consul_service = ConsulService()
    consul_service.setup(service_name, service_port, request.host)

    app.run(host='0.0.0.0', port=service_port, debug=True)
