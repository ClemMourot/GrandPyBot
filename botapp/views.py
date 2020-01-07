"""defines application routes and returns jsonified data to web page
generated by instantiating a GrandPyBot object based on the user input"""


from flask import Flask, render_template, request, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import flask_login as login
from flask_migrate import Migrate

from botapp.grandpy_bot import GrandPyBot
from botapp.app import create_production_app
from botapp.models.logging import Logging, LoggingView
from botapp.models.user import User
from botapp.models.admin import AdminIndexView


app, db = create_production_app()

admin = Admin(app, name='GrandPy Bot', index_view=AdminIndexView(), template_mode='bootstrap3', base_template='custom-admin.html')
admin.add_view(LoggingView(Logging, db.session))

@app.route('/')
def page():
    """returns the html file"""
    return render_template('page.html')


@app.route('/answer')
def generate_answer():
    """returns the answer constructed when there's a user input"""
    bot = GrandPyBot(request.args.get('question'))
   
    # instantiates GrandPyBot object with the user input value
    return jsonify(bot.return_data())  # returns data in json


if __name__ == "__main__":
    app.run()
