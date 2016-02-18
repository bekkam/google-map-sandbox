"""A flask app for practice"""

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_map():
    return render_template('map-draggable-directions-with-simple-init')


@app.route('/submit-addresses.json', methods=['GET'])
def get_addresses():
    """Return addresses"""

    start = request.args.get("start")
    end = request.args.get("end")
    return jsonify({"start_point": start, "end_point": end})



# map directions simple - no text directions
# map draggable directions - text directions, waypoints, draggable.
if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
