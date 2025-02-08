from flask import Flask
from flask_sqlalchemy import sqlalchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://database.db"
db = sqlalchemy(app)

@app.route("/hello-world", methods=["GET"])
def Hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)