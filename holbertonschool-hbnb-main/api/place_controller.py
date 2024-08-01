from flask import Blueprint, request, jsonify, render_template, redirect, url_for
 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from persistence.data_manager import DataManager
from datetime import datetime
from models.place import Place
from models.db import db
import json
import os
from flask_bcrypt import Bcrypt
from flask_cors import CORS


bcrypt = Bcrypt()



place_controller = Blueprint('place_controller', __name__)
#user_controller = Blueprint('user_controller', __name__, template_folder='templates')

dmanager = DataManager()

""""""
#post

@place_controller.route("/places" , methods=['POST'])
def place_post():
    plc = Place("name", "description", "country", "city", "price")  
    dmanager.save(plc)
    return "saved"

@place_controller.route("/places", methods=['GET'])
@jwt_required()
def user_get():
    return dmanager.get_all(Place)