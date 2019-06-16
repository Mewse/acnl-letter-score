from bottle import route, run, template, request
from score import score_message

@route('/')
def index():
    return template("index", message = "", score=None)

@route("/score")
def score():
    message = request.query.get("message")
    print(message)
    score = score_message(message)
    return template("index", score=score, message=message)

run(host='0.0.0.0', port=80, debug=False)
