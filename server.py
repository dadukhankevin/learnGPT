from flask import Flask, request, jsonify
import tinydb
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

topics = ["History", "Science", "German"]
existing = [{
    'World History': {
        'description': 'a study set about world history',
        'score': '60%',
        'data': {'term': 'definition'}
    },
    "Quantum Physics": {
        "description": "Cool magic",
        "score": "50%",
        'data': {'term': 'definition'}
    }
}]*5


@app.route('/create')
def hello():
    name = request.args.get('name')
    return jsonify({name: "term"})


@app.route("/list")
def get():
    return jsonify(topics)

@app.route("/add")
def add():
    name = request.args.get("name")
    topics.append(name)
    return ""


if __name__ == '__main__':
    app.run(debug=True)
