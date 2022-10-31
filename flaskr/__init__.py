"""The application factory"""
import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # should be overridden with a random value when deploying.
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config:
        app.config.from_mapping(test_config) # will be used instead of the instance configuration. so the tests can be configured independently of any development values
    else:
        app.config.from_pyfile("config.py", silent=True) #  when deploying, this can be used to set a real SECRET_KEY.

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from . import db, auth, blog
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
