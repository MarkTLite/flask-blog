"""Connect to the Database
In web applications this connection is typically tied to the request.
It is created at some point when handling a request, and closed before the response is sent."""

import sqlite3, click

from flask import current_app, g

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