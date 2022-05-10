# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
from main.app import app, engine
from flask import request, jsonify
from sqlalchemy.orm import Session

from main.models import Customer
from flask_jwt_extended import create_access_token


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    try:
        session = Session(engine)
        user_obj = session.query(Customer).get({"username": username, "password": password})
        if user_obj is None:
            jsonify({"msg": "Username not found"}), 401
    except:
        print("problem")
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user_obj.id)
    return jsonify(access_token=access_token)


@app.route("/signup", methods=["POST"])
def signup():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    try:
        session = Session(engine)
        user = Customer(username=username, password=password)
        session.add(user)
        session.commit()
        session.close()
        user_id = user.id
        print(user_id)
    except:
        print("problem")
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token)
