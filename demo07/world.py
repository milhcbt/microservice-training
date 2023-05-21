from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'name': 'world'})
@app.route('/<name>')
def world(name):
    return name

if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
