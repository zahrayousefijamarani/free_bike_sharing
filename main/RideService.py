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
        return jsonify({"msg": "Bike is for you"}), 200
    session.close()
    return jsonify({"msg": "Bike is far from you"}), 401
