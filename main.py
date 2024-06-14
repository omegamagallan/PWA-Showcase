from flask import Flask, render_template, send_file
from flask_socketio import SocketIO
from flask_cors import CORS
from data import Data


app = Flask(__name__)
global data


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/code")
def code():
    return render_template("code.html", default_code=data.plotly_default_code)


@app.route("/osc")
def osc():
    return render_template("osc_communication.html")


@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')


@app.route('/serviceworker.js')
def serve_sw():
    return send_file('js/serviceworker.js', mimetype='application/javascript')


@app.route('/osc.min.js')
def serve_osc_browser():
    return send_file('js/osc.min.js', mimetype='application/javascript')


if __name__ == '__main__':
    data = Data(app.static_folder)
    app.config['SECRET_KEY'] = data.key
    CORS(app)
    socketio = SocketIO(app, cors_allowed_origins='*')
    app.run()
