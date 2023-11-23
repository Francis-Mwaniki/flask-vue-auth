""" use pymongo to create a User class"""
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
import requests

mongo = PyMongo()

class User:
    def __init__(self, username, email, password, reset_token=None):
        self.username = username
        self.email = email
        self.password = password
        self.reset_token = reset_token
    
    def json(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'reset_token': self.reset_token
        }
        
        
