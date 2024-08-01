from flask import Blueprint, request, jsonify, render_template, redirect, url_for
 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.user import User
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS


bcrypt = Bcrypt()



user_controller = Blueprint('user_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()

""""""
#post

@user_controller.route("/users" , methods=['GET'])
def user_post():
    first_name = "qureyshi"
    last_name = "qureyshi"
    email = "kamran@mail.com"
    age = "abfbge"
    password = "1998"

    usr = User(first_name=first_name, last_name=last_name, email=email, age=age, password=password)  
    dmanager.save(usr)
    return "saved"


"""
#get all

@user_controller.route("/users", methods=['GET'])
def user_get():
    return dmanager.get_all(User)
"""


"""

#get by id


@user_controller.route("/users/<user_id>", methods=['GET'])
def user_get(user_id):
    return dmanager.get(user_id, User)
"""




"""
#delete 

@user_controller.route("/users/<user_id>", methods=['GET'])
def user_get(user_id):
    dmanager.delete(user_id, User)
    return "deleted"

"""

"""
#update post

@user_controller.route("/users/<user_id>", methods=['GET'])
def user_get(user_id):
    entity = db.session.query(User).filter_by(id=user_id).first()
    entity.age = 4520
    return dmanager.update(entity)
"""
 

"""

@user_controller.route('/login', methods=['POST'])
def loginpost():
    #data = request.get_json()
    email = "kamran@mail.com"
    password = "1998"
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.email)  # Correctly use 'user.email'
        return jsonify(access_token=access_token), 200
    return 'Wrong username or password', 401


"""


"""""" 
@user_controller.route('/login', methods=['POST'])
def loginpost():
    # Extract email and password from the request body
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"msg": "Email and password are required"}), 400

    # Query the user based on the email
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password_hash, password):
        # Create a JWT token with the user's email
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Wrong username or password"}), 401



@user_controller.route('/login', methods=['GET'])
def login():
    return render_template("login.html")



















"""
"""

@user_controller.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

 
    

"""

@user_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'email': user.email, 'is_admin': user.is_admin})
        return jsonify(access_token=access_token), 200
    return "msg": "Bad email or password"

"""

















"""
@user_controller.route("/users" , methods=['POST'])
def user_post():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if '@' not in email:
            return jsonify({'error': 'Invalid email format'}), 400
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    if "User" in dataStore:
        for user_info in dataStore["User"].values():
            if user_info["email"] == email:
                return jsonify({'error': 'Email already exists'}), 400
    
    usr = User(email, first_name, last_name)
    dmanager.save(usr)
    return jsonify(usr.__dict__), 201 

@user_controller.route("/users", methods=['GET'])
def user_get():
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    return jsonify(dataStore["User"]), 200


@user_controller.route("/users/<user_id>", methods=['GET'])
def user_get_id(user_id):
    return dmanager.get(user_id, "User")

@user_controller.route("/users/<user_id>", methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    existing_data = dmanager.get(user_id, 'User')
    if not existing_data:
        return jsonify({'error': 'User not found'}), 404


     
    updated_user = User( data.get('email'), data.get('email'), data.get('email'))
    updated_user.id = user_id
    updated_user.created_at = existing_data["created_at"]
    dmanager.update(updated_user)
    return jsonify(updated_user.__dict__), 200



@user_controller.route("/users/<user_id>", methods=['DELETE'])
def user_delete(user_id):
    user = dmanager.get(user_id, 'User')
    if user is None:
        return jsonify({"error": "user not found"}), 404
    dmanager.delete(user_id, "User")
    return  jsonify({'message': 'User deleted'}), 204
    

"""
