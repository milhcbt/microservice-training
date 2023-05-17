#flask code that return "hello world" + the name of the user + current time.
from flask import Flask
from datetime import datetime
app = Flask(__name__)
@app.route('/hello/', defaults={'name': 'world'})
@app.route('/hello/<name>')
def hello(name):
    return "Hello %s, the time is %s" % (name, datetime.now())
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)

