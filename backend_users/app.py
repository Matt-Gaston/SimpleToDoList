import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


#my ORM classes
from dbmodels import Base, User


app = Flask(__name__)

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
CORS(app, origins=[FRONTEND_URL, "http://71.86.158.1","http://192.168.1.100"])

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("DB_HOST", "localhost")  # or 'db' for Docker Compose
DB_PORT = os.getenv("DB_PORT", 5432)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

db = SQLAlchemy(model_class=Base)
db.init_app(app)



@app.route("/api/users/")
def hello_world():
    return jsonify({"message": "Hello, testing World!"})


@app.route("/api/users/all")
def get_users():
    users = db.session.query(User).all()
    return jsonify([
        {
            "id": str(user.id),
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }
        for user in users
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)