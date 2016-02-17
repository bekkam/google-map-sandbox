"""A flask app for practice"""

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_map():
    return render_template('directions-result.html')


# map directions simple - no text directions
# map draggable directions - text directions, waypoints, draggable.
if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
