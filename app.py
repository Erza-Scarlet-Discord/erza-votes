# basic flask app
import flask
import requests
from flask import jsonify

app = flask.Flask(__name__)

suffix = ".herokuapp.com"


@app.route('/votes', methods=['POST'])
def vote():
    # get request headers and data
    api = "https://localhost:17995/api/v2/votes"
    headers = flask.request.headers
    data = flask.request.get_data()
    # send request to vote server
    if requests.get("https://erza-scarlet-26" + suffix).status_code == 200:
        api = "https://erza-scarlet" + suffix + "api/v2/votes"
    elif requests.get("https://erza-ai" + suffix).status_code == 200:
        api = "https://erza-ai" + suffix + "api/v2/votes"
    elif requests.get("https://erza-ai-backup" + suffix).status_code == 200:
        api = "https://erza-ai-backup" + suffix + "api/v2/votes"

    requests.post(api, headers=headers, data=data)
    return jsonify({'message': "vote recorded"}), 200
