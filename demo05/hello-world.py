from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'name': 'world'})
@app.route('/<name>')
def hello_world(name):
    hello = requests.get('http://localhost/hello').text
    world = requests.get(f'http://localhost/world/{name}').text
    time = requests.get('http://localhost/time').text
    return f"{hello} {world}, the time is {time}"

if __name__ == "__main__":
    app.run(host='localhost', port=5003, debug=True)
