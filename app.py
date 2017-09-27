import os
import random
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    res = processRequest(req)
    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/')
def home():
    excuse = processRequest()

    return render_template('home.html', excuse=excuse)

def processRequest():

    excuses = []

    # Read each line from file
    with open('bohf_list.txt', 'r') as lines:

        # Add each to Python list
        for line in lines:
            excuses.append(line)

    # Return a random excuse
    return random.choice(excuses)

if __name__ == '__main__':
    # port = int(os.getenv('PORT', 5000))
    # print('Starting app on port %d' % port)
    # app.run(debug=True, port=port, host='127.0.0.1')
    app.run(host='127.0.0.1', debug=True)
