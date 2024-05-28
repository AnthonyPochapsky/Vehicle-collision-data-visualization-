import DataRetrieval
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/fetchdata")
def send_json():
    return jsonify(DataRetrieval.getData())

if __name__ == "__main__":
    app.run(debug=True)