from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models.user import User
from api.user_controller import user_controller
from api.country_controller import country_controller
from api.place_controller import place_controller
from models.db import db


app = Flask(__name__)
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_SECRET_KEY'] = 'c303282d-f2e6-46ca-a04a-35d3d873712d'  




jwt = JWTManager(app)
bcrypt = Bcrypt(app)
# Creating an SQLAlchemy instance

db.init_app(app)
# Settings for migrations
migrate = Migrate(app, db)
CORS(app) 
bcrypt.init_app(app)
jwt.init_app(app)


 



@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


"""
@app.route("/users", methods=['GET'])
def user_get():
    
    first_name = "firbfst"
    last_name = "last_bffbname"
    age = "abfbge"

    # create an object of the Profile class of models
    # and store data as a row in our datatable
    p = User(first_name=first_name, last_name=last_name, age=age)
    db.session.add(p)
    db.session.commit()
    return "User"

"""

app.register_blueprint(user_controller)
app.register_blueprint(country_controller)
app.register_blueprint(place_controller)

if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5000, debug=True)
   #app.debug = True



























"""


from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy

from persistence.ipersistence_manager import IPersistenceManager
from persistence.data_manager import DataManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)


class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin




@app.route("/")
def index():
    #from models.user import User
    #std = User("654448", "jhjdjbkcnj@", "hhgknkj", "jjbjhjkk")
    #db.session.add(std)
    #db.session.commit()
    #db.session.close()
    return "home"
    
from models.user import User 

from api.user_controller import user_controller
from api.amenity_controller import amenity_controller
from api.place_controller import place_controller
from api.review_controller import review_controller
from api.city_controller import city_controller
from api.country_controller import country_controller
import json

app.register_blueprint(user_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)
app.register_blueprint(city_controller)
app.register_blueprint(country_controller)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
       
"""