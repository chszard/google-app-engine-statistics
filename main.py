import os
from flask import Flask, render_template, url_for, jsonify, json
from markupsafe import Markup

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.route('/<filename>')
def route_using_filename(filename):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    target_file = filename + ".json"
    json_url = os.path.join(SITE_ROOT, "static/data/json", target_file)
    data = json.load(open(json_url))
    return render_template(filename + ".html", data=Markup(json.dumps(data)))