# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the Flask Dependency
from flask import Flask, jsonify

# Set up the Database, access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into classes
Base = automap_base()

# Reflect the database into tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Set up Flask
app = Flask(__name__)

# Set up routes
@app.route("/")

# Create function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
# Open Terminal Run Flask type:
    # flask run
        # Output - Running on:
            # http://127.0.0.1:5000/

# Precipitation Route
@app.route("/api/v1.0/precipitation")

# Precipitation Function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# Run Flask
    # http://127.0.0.1:5000/api/v1.0/precipitation

# Stations Route
@app.route("/api/v1.0/stations")

# Stations Function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Run Flask
    # http://127.0.0.1:5000/api/v1.0/stations

# Monthly Temperature Route
@app.route("/api/v1.0/tobs")

# Temperature Function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Run Flask
    # http://127.0.0.1:5000/api/v1.0/tobs

# Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Statistics Function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# Run Flask
    # http://127.0.0.1:5000/api/v1.0/temp/start/end
    # Add Dates
        # http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30