from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///caddycore.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    from .routes.analyze import analyze_bp
    app.register_blueprint(analyze_bp)
    from .routes.summary import summary_bp
    app.register_blueprint(summary_bp)
    from .routes.rounds import rounds_bp
    app.register_blueprint(rounds_bp)
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    from .routes.tees import tees_bp
    app.register_blueprint(tees_bp)

    return app
