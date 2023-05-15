from flask import Flask, request, jsonify
from flask_cors import CORS
import chatbot
import saver
import os

current_directory = os.getcwd() + "\\data\\"
saver.current_directory = current_directory
db = saver.Saver(current_directory)
app = Flask(__name__)
CORS(app)

topics = os.listdir(db.path)
print(topics)
@app.route("/get_category")
def get_category():
    category = request.args.get("category").lower().replace("%20", " ")
    if category in topics:
        names = saver.get_file_names(category)
        print(names)
        return jsonify(names)
    else:
        return "404"

@app.route('/create')
def hello():
    name = request.args.get('name')
    return jsonify({name: "term"})


@app.route("/list")
def get():
    return jsonify(topics)

@app.route("/add")
def add():
    global topics
    topics = os.listdir(db.path)
    print(topics)
    name = request.args.get("name").lower()
    saver.create_directory(name)
    return ""

@app.route("/generate")
def generate():
    category = request.args.get("name")
    values = request.args.get("values").split(",")
    for i in values:
        print(i)
        set = chatbot.create_set(i)
        print(set['choices'][0]['message']['content'])
        db.create_new_set(category, i, set['choices'][0]['message']['content'])
    return values[0]
@app.route("/example")
def example():
    # create a dictionary with 2 terms and their definitions
    data = {
        "item1": {
            "term": "Roman Empire",
            "definition": "A period of ancient Roman civilization characterized by the rule of emperors in Rome, spanning from 27 BCE to 476 CE."
        },
        "item2": {
            "term": "Svelte",
            "definition": "A framework for building user interfaces with reactive components."
        }
    }
    # return the data as json
    return jsonify(data)
@app.route("/learn")
def learn():
    category = request.args.get("category").lower()
    set = request.args.get("set")
    data = db.get_set(category, set)
    return data

if __name__ == '__main__':
    app.run(debug=True)
