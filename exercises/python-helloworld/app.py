from datetime import datetime
from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def status():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        filename='metrics_log.log', 
        encoding='UFT-8', 
        level=logging.DEBUG, 
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.debug("status called: " + str(datetime.timestamp(datetime.now())))

    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route('/metrics')
def metrics():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        filename='metrics_log.log', 
        encoding='UFT-8', 
        level=logging.DEBUG, 
        datefmt='%Y-%m-%d %H:%M:%S')
        
    logging.debug("metrics called: " + str(datetime.timestamp(datetime.now())))

    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    

    app.run(host='0.0.0.0')