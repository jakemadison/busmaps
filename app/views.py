from flask import Flask, render_template, jsonify, g, request
from app import app
import grab_data


@app.route('/')
@app.route('/index')
@app.route('/<int:route>')
@app.route('/index/<int:route>')
def index(route=99):
    g.route = route
    g.stopNumber = 0
    g.allstops = False
    return render_template("index.html")

@app.route('/stop/')
@app.route('/stop/<int:stop>')
def get_stop(stop=51195):
    g.route = 0
    g.stopNumber = stop
    g.allstops = False
    return render_template("index.html")


@app.route('/all')
def all_busses():
    g.allstops = True
    g.route = 0
    g.stopNumber = 0
    return render_template("index.html")

@app.route('/get_locs', methods=['GET', 'POST'])
def get_locations():

    route = request.args.get('route', '099')
    stop = request.args.get('stop', None)
    allstops = request.args.get('allstops', None)

    locations = grab_data.get_bus_loc(route, stop, allstops=allstops)
    return jsonify(locations=locations)