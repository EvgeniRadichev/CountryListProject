from flask import Flask, jsonify
from networkx import DiGraph, shortest_path
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# define network of connected countries
countryList = ["CAN","USA","MEX","GTM","BLZ","SLV","HND","NIC","CRI","PAN"]
countryNet = DiGraph()
countryNet.add_nodes_from(countryList)
countryNet.add_edges_from([("USA","CAN"),("USA","MEX"),("MEX","GTM"),("MEX","BLZ"),
                  ("GTM","SLV"),("GTM","HND"),("HND","NIC"),("NIC","CRI"),
                  ("CRI","PAN")])

# home directory
@app.route("/")
def home():
    return "Nothing to find here! Try adding '/PAN' or '/BLZ' to the end of your request or URL string."

# route-finder for different country endpoints
@app.route("/<country>")
def get_country(country):
    if country in countryList:
        path = shortest_path(countryNet,"USA",country)
        return jsonify(path)
    else:
        return jsonify("Country identifier not found!")

if __name__ == "__main__":
    #app.run() # for development purposes only
    http_server = WSGIServer(('0.0.0.0',5000),app)
    http_server.serve_forever()