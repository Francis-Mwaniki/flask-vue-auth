
from model.user import User
import os
import requests
import resend


resend.api_key = "re_chB8ktT1_EgTTewUqXk15U57vBzrnQ3AA"

def register_user(username, email, password):
    from run import mongo
    users_collection = mongo.db.users

    # Check if user exists
    existing_user = users_collection.find_one({'email': email})
    if existing_user:
        return "User already exists"

    # Create new user
    user = User(username, email, password)
    users_collection.insert_one(user.json())
    
    try:
        r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "fmwaniki986@gmail.com",
            "subject": "Welcome to my app!",
            "html": "<strong>Thanks for signing up!</strong>",
   })
        

        
        print(r)
        return 'ok'
    except Exception as e:
        print(e.message)
    from run import mongo
    users_collection = mongo.db.users

    # Add your code here to reset the user's password
    return 'ok'
        
def login_user(email, password):
    from run import mongo
    users_collection = mongo.db.users

    user = users_collection.find_one({'email': email})
    if user and user['password'] == password: 
        return 'ok'
    else:
        return 'Invalid credentials'

def reset_user_password(email):
    from run import mongo
    users_collection = mongo.db.users
    # Check if user exists
    user = users_collection.find_one({'email': email})
    if not user:
        return 'User does not exist'

    # Generate reset token and update user's document
    reset_token = os.urandom(24).hex()
    users_collection.update_one({'email': email}, {'$set': {'reset_token': reset_token}})
  
    # Send email with reset token
    print(f'email: {email}, reset_token: {reset_token}')
    try:
       r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": 'fmwaniki986@gmail.com',
           "subject": "reset_token",
            "html": f"<strong>Reset token: {reset_token}</strong>",
   })
       return 'ok'  
        
    except Exception as e:
        print(e.message)
        return {e.message}, 500
        
    

""" update password """
def update_password(reset_token, new_password):
    print(reset_token, new_password)
    from run import mongo
    users_collection = mongo.db.users
    user = users_collection.find_one({'reset_token': reset_token})
    if not user:
        return 'User does not exist'
    if user:
        print(user)
    users_collection.update_one({'reset_token': reset_token}, {'$set': {'password': new_password}})
    return 'ok'