from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# request directories
pan = ["USA","MEX","GTM","HND","NIC","CRI","PAN"]
blz = ["USA","MEX","BLZ"]

# home directory
@app.route("/")
def home():
    return "Nothing to find here! Try adding '/PAN' or '/BLZ' to the end of your request or URL string."

# GET request for PAN countries
@app.route("/PAN")
def get_pan():
    return jsonify(pan)

# GET request for BLZ countries
@app.route("/BLZ")
def get_blz():
    return jsonify(blz)

if __name__ == "__main__":
    # app.run() # for development purposes only
    http_server = WSGIServer(('127.0.0.1',5000),app)
    http_server.serve_forever()