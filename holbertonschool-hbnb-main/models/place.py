from models.base_model import BaseModel
from datetime import datetime
from .db import db
import uuid
import json
 

class Place(BaseModel, db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    description  = db.Column(db.String(20), unique=False, nullable=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=False, nullable=False)
    price = db.Column(db.String(20), unique=False, nullable=False)
    

    def __init__(self, name, description, country, city, price):
        super().__init__()
        self.name = name
        self.description = description
        self.country = country
        self.city = city
        self.price = price
 
 
    def to_dict(self):
        return {
            'db_id': self.db_id,
            'name': self.name,
            'description': self.description,
            'country': self.country,
            'city': self.city,
            'price': self.price,
            'id' : self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }