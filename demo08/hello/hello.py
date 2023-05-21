from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello"

if __name__ == "__main__":
    service_name = 'hello'
    service_port = 5000

    consul_service = ConsulService()
    consul_service.setup(service_name, service_port, request.host)

    app.run(host='0.0.0.0', port=service_port, debug=True)
