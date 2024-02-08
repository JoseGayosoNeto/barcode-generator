from flask import Flask
from ..routes.bar_code_routes import bar_code_blueprints

app = Flask(__name__)

app.register_blueprint(bar_code_blueprints)
