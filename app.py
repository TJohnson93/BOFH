import random
import flask from Flask, request, make_response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    res = processRequest(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(request):

    # Read each line from file
    with open('bohf_list', 'r') as lines
    excuses = []

    # Add each to Python list
    for line in lines:
        excuses.append(line)

    # Return a random excuse
    return random.choice(excuses)