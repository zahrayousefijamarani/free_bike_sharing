from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy import Date, func

from main.app import app, engine
from flask import request, jsonify
from sqlalchemy.orm import Session

from main.haversine import haversine
from main.models import Customer, Bike, Ride


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/get_ride", methods=["GET"])
@jwt_required()
def getRide():
    current_user = get_jwt_identity()
    bike_id = request.json.get("bike_id", None)
    try:
        bike_id = int(bike_id)
    except:
        print("problem")
        return jsonify({"msg": "Format of ID is not correct"}), 401

    session = Session(engine)
    bike_obj = session.query(Bike).get({"id": bike_id})
    if bike_obj is None:
        session.close()
        return jsonify({"msg": "Bike not found"}), 401
    if bike_obj.status != "available":
        session.close()
        return jsonify({"msg": "Bike is not available"}), 401

    user_obj = session.query(Customer).get({"id": current_user})
    if haversine(bike_obj.loc_x, bike_obj.loc_y, user_obj.loc_x, user_obj.loc_y) < 100:
        user_obj.status = "riding"
        bike_obj.status = "busy"
        ride = Ride(customer_id=user_obj.id, bike_id=bike_obj.id, status="ongoing", date=func.current_date())
        session.add(ride)
        session.commit()
        session.close()
        return jsonify({"msg": "ride_id:" + str(ride.id)}), 200
    session.close()
    return jsonify({"msg": "Bike is far from you"}), 401


@app.route("/end_ride", methods=["GET"])
@jwt_required()
def endRide():
    current_user = get_jwt_identity()
    ride_id = request.json.get("ride_id", None)
    bike_loc_x = request.json.get("loc_x", None)
    bike_loc_y = request.json.get("loc_y", None)
    try:
        ride_id = int(ride_id)
    except:
        print("problem")
        return jsonify({"msg": "Format of ID is not correct"}), 401
    session = Session(engine)
    ride_obj = session.query(Ride).get({"id": ride_id})
    if ride_obj.customer_id != current_user:
        session.close()
        return jsonify({"msg": "You are not the rider"}), 401

    user_obj = session.query(Customer).get({"id": current_user})
    bike_obj = session.query(Bike).get({"id": ride_obj.bike_id})

    user_obj.status = "free"
    bike_obj.status = "available"
    ride_obj.status = "finished"
    ride_obj.distance = haversine(bike_obj.loc_x, bike_obj.loc_y, bike_loc_x, bike_loc_y)
    session.commit()
    session.close()
    return jsonify({"msg": "end of riding"}), 200
