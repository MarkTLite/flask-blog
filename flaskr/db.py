"""Connect to the Database
In web applications this connection is typically tied to the request.
It is created at some point when handling a request, and closed before the response is sent."""

import sqlite3, click

from flask import Flask, current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row # tells the connection to return rows that behave like dicts to allow accessing columns by name

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close() 

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Register with the Application in __init__.py
def init_app(app: Flask):
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()
    # app.cli.add_command(init_db_command) # call this cli command once in the production lifetime
