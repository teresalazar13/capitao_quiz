import requests
from flask import Flask
from random import shuffle

app = Flask(__name__)


@app.route('/')
def hello_world():
    req = requests.get('https://opentdb.com/api.php?amount=1&type=multiple', )
    dic = req.json()
    category = dic.get("results")[0].get("category")
    difficulty = dic.get("results")[0].get("difficulty")
    question = dic.get("results")[0].get("question")
    incorrect_answers = dic.get("results")[0].get("incorrect_answers")
    correct_answer = dic.get("results")[0].get("correct_answer")

    options = incorrect_answers + [correct_answer]

    shuffle(options)

    text = question + "\n"
    abcd = "ABCD"

    for i in range(4):
        text += abcd[i] + " - " + options[i] + "\n"
    print(text)

    return text


if __name__ == '__main__':
    app.run()
