from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

# 밑에는 
# instantiate the app
# app = Flask(__name__)
# app.config.from_object(__name__)


def create_app(config=None):
    app = Flask(__name__)
    # enable CORS
    # CORS(app)
    CORS(app, resources={r'/*': {'origins': '*'}})
    if app.config["ENV"] == 'production':
        print("env")
        app.config.from_object('config.ProductionConfig')
    else:
        print("prodeuct")
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from routes import (main_route, ping_route, support_route, lotto_his_route)
    app.register_blueprint(main_route.bp, url_prefis='/api')
    app.register_blueprint(ping_route.bp, url_prefix='/api/ping')
    app.register_blueprint(support_route.bp, url_prefix='/api/support')
    app.register_blueprint(lotto_his_route.bp, url_prefix='/api/lottohis')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
