from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "65382K6280Y2790E"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zbdkquvmxzckhq:6e785fa03d668d114af64f9bd8c439aaf15546c88cbb3b6cc0ca0785561be927@ec2-54-221-243-211.compute-1.amazonaws.com:5432/d5n09via8sdn3c"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views