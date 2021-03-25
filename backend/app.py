from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/support', methods=['GET'])
def all_plaza():
    return jsonify({
        'status': 'success',
        'supports': Support
    })


if __name__ == '__main__':
    app.run()

Support = [
    {
        'title': 'On the Road',
        'writer': 'Jack Kerouac',
        'content': 'gooood'
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'writer': 'J. K. Rowling',
        'content': 'gooood'
    },
    {
        'title': 'Green Eggs and Ham',
        'writer': 'Dr. Seuss',
        'content': 'gooood'
    }
]