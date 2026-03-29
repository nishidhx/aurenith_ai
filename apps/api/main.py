from flask import Flask
from routes.user_routes import user_bp
from models.user_model import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://neondb_owner:npg_yR6CqBOYcj4s@ep-proud-dew-amcbmnj8-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_bp)

@app.route("/")
def hello_world(): 
    return "<p>Hello</p>"

if __name__ == "__main__":
    app.run(debug=True)