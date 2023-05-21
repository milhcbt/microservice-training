from flask import Flask
import consul



app = Flask(__name__)

@app.route('/')
@app.route('/hello') 
def hello():
    return "Hello"


if __name__ == "__main__":
    # Create a consul client object
    client = consul.Consul(host='consul', port=8500)
    # Define the array of key-value pairs
    array = [
    {
    "Key": "traefik/http/routers/router01/entryPoints/0",
    "Value": "web"
    },
    {
    "Key": "traefik/http/routers/router01/service",
    "Value": "hello"
    },
    {
    "Key": "traefik/http/routers/router01/rule",
    "Value": "Path(`/hello`)"
    },
    {
    "Key": "traefik/http/services/hello/loadBalancer/servers/0/url",
    "Value": "http://hello:5000/"
    },
    ]
    # Loop through the array and put each key-value pair into consul KV
    for item in array:
        key = item["Key"]
        value = item["Value"]
        client.kv.put(key, value)

    app.run(host='0.0.0.0', port=5000, debug=True)
