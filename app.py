import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False


@app.route('/vote', methods=['POST'])
def index():
    if request.method == "POST":
        data = request.get_json()
        main = requests.get("https://erza-ai.herokuapp.com")
        backup = requests.get("https://erza-ai-backup.herokuapp.com")
        es26 = requests.get("https://erza-scarlet-26.herokuapp.com")
        api = None
        if main.status_code == 200:
            print("erza-ai is up and running")
            api = "https://erza-ai.herokuapp.com/"
        elif backup.status_code == 200:
            print("erza-ai-backup is up and running")
            api = "https://erza-ai-backup.herokuapp.com/"
        elif es26.status_code == 200:
            print("es26 is up and running")
            api = "https://erza-scarlet-26.herokuapp.com/"
        else:
            print("[w] : none of them are up and running")
            print(es26, main, backup)

        if api:
            requests.post(api + "api/v2/votes", json=data, headers=request.headers)
            
        return jsonify(code=working, message=f"POST to {api}"), 200


if __name__ == '__main__':
    app.run()
