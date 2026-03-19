from flask import Flask, render_template
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from models import db
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

app.register_blueprint(alumnos)
app.register_blueprint(maestros)
app.register_blueprint(cursos)

 
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
