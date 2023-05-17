from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def time():
    return str(datetime.now())

if __name__ == "__main__":
    app.run(host='localhost', port=5002, debug=True)
