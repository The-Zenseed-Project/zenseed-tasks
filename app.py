from flask import Flask
from extensions import db, migrate
from routes import auth_bp, tasks_bp, projects_bp
import yaml

def create_app():
    app = Flask(__name__)
    with open('settings.yaml', 'r') as f:
        settings = yaml.safe_load(f)
    app.config.update(settings['flask_config'])
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(projects_bp)
    return app
