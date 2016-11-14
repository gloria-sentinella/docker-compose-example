from flask import Flask
from .task import add_metrics
app = Flask(__name__)

@app.route('/')
def hello_world():
    add_metrics.delay()
    return 'Flask Dockerized'
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')