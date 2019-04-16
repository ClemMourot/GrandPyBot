"""defines application routes and returns jsonified data to web page
generated by instantiating a GrandPyBot object based on the user input"""


from flask import Flask, render_template, request, jsonify
from app.grandpy_bot import GrandPyBot


app = Flask(__name__)


@app.route('/')
def page():
    """returns the html file"""
    return render_template('page.html')


@app.route('/answer')
def generate_answer():
    """returns the answer constructed when there's a user input"""
    bot = GrandPyBot(request.args.get('question'))
    return jsonify(bot.return_data())


if __name__ == "__main__":
    app.run()
