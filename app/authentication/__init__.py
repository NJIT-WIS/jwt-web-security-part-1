"""These are the routes to login, register, and protect a route"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, current_user

from app.db import db
from app.db.models import User

authentication = Blueprint('authentication', __name__)


@authentication.route('/register', methods=['POST'])
def register():
    # Check if there are any users.  The first user will be made an admin
    data = request.get_json()
    username = data['data']['attributes']['username']
    password = data['data']['attributes']['password']

    if User.query.count() == 0:
        user = User(username=username, password=password, is_admin=1)
    else:
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username, password=password, is_admin=0)
        else:
            return jsonify("Already Registered"), 200
    db.session.add(user)
    db.session.commit()
    return jsonify("Created User"), 201


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@authentication.route("/auth", methods=["POST"])
def login():
    data = request.get_json()
    username = data['data']['attributes']['username']
    password = data['data']['attributes']['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        response = {"error": {"message": "access denied"}}
        return jsonify(response), 302
    else:
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)


@authentication.route("/user_info", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        username=current_user.username,
    )


