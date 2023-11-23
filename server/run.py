
from flask import Flask
from flask_pymongo import PyMongo
from routes.auth import auth_routes  # Import your routes
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  
app.config['MONGO_URI'] = 'mongodb+srv://next:next@cluster0.xgfuv.mongodb.net/auth'  # Replace with your MongoDB URI

mongo = PyMongo(app)

# Register blueprints/routes
app.register_blueprint(auth_routes)  # Assuming auth_routes is your auth blueprint

if __name__ == "__main__":
    app.run(debug=True)
    