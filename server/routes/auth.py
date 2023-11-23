from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user, reset_user_password, update_password
import os
import requests
import resend


resend.api_key = "re_chB8ktT1_EgTTewUqXk15U57vBzrnQ3AA"

# auth_routes = Blueprint('auth', __name__)
auth_routes = Blueprint('auth_routes', __name__)

""" get request """
@auth_routes.route('/test', methods=['GET'])
def test():
    r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "fmwaniki986@gmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
   })

    return jsonify(r)


@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    response = register_user(data.get('username'), data.get('email'), data.get('password'))
    return jsonify(response)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    response = login_user(data.get('email'), data.get('password'))
    return jsonify(response)

@auth_routes.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    response = reset_user_password(data.get('email'))
    return jsonify(response)


@auth_routes.route('/update-password', methods=['POST'])
def update_password_handler():
    data = request.json
    reset_token = data.get('reset_token')
    new_password = data.get('new_password')

    # Call the update_password function with the required arguments
    response = update_password(reset_token, new_password)
    return jsonify(response)