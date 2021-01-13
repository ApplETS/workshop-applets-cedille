#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from os import environ
from openapi_server.config import DevelopmentConfig, ProductionConfig
from openapi_server.db import db


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')

    # Load the config
    if environ.get("FLASK_ENV") == "production":
        app.app.config.from_object(ProductionConfig)
    else:
        app.app.config.from_object(DevelopmentConfig)

    # Initialize database
    db.init_app(app.app)

    with app.app.app_context():
        db.create_all()

    app.app.json_encoder = encoder.JSONEncoder

    app.add_api('openapi.yaml',
                arguments={'title': 'TODO API'},
                pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
