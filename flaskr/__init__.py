"""The application factory"""
import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)    
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config:
        app.config.from_mapping(test_config) # will be used instead of the instance configuration. so the tests can be configured independently of any development values
    else:
        env_config = os.getenv("DEPLOY_SETTINGS", "config.DevelopmentConfig")
        app.config.from_object(env_config)
        # app.config.from_pyfile("config.py", silent=True) #  when deploying, use the above 2 lines to set real SECRETS and comment this line

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
