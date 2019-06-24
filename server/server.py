from bottle import route, run, template, request, post, static_file
from score import score_message
import json

@route('/')
def index():
    return static_file("index.html", root='./client/build/')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./client/build/static')

@post("/score")
def score():
    message = request.json.get("message")
    print(message)
    score, breakdown = score_message(message)
    breakdown["total"] = score
    return json.dumps(breakdown)

run(host='0.0.0.0', port=80, debug=False)
