import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Configure Flask app
app.config["SECRET_KEY"] = os.urandom(32).hex()
app.config["JWT_SECRET_KEY"] = app.config["SECRET_KEY"]

# Set up JWTManager
jwt = JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USERNAME')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Create all database tables
with app.app_context():
    db.create_all()
