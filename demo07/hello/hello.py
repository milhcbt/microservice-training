from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/hello') 
def hello():
    return "Hello"

if __name__ == "__main__":
    consul_client = consul.Consul(host='localhost', port=8500)

    app.run(host='0.0.0.0', port=5000, debug=True)
