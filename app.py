# basic flask app
import os
import flask
import requests
from flask import jsonify

app = flask.Flask(__name__)

suffix = ".herokuapp.com/"


@app.route('/votes', methods=['POST'])
def vote():
    # get request headers and data
    api = "https://localhost:17995/api/v2/votes"
    data = flask.request.get_json()
    # send request to vote server
    if requests.get("https://erza-scarlet-26.herokuapp.com/").status_code == 200:
        api = "https://erza-scarlet-26.herokuapp.com/api/v2/votes"
    elif requests.get("https://erza-ai.herokuapp.com/").status_code == 200:
        api = "https://erza-ai.herokuapp.com/api/v2/votes"
    elif requests.get("https://erza-ai-backup.herokuapp.com/").status_code == 200:
        api = "https://erza-ai-backup.herokuapp.com/api/v2/votes"
    elif requests.get("https://erza-ai.up.railway.app/").status_code == 200:
        api = "https://erza-ai.up.railway.app/"
    data = requests.post(api, headers={"Authorization": "090807060504030201"}, json=data)
    return jsonify({'message': "vote recorded"}), 200


