# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, render_template, request, session
from flask_session import Session
from longest_word.game import Game

app = Flask(__name__)
# Session configuration
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)


@app.route('/')
def home():
    game = Game()
    # Set initial score
    session["score"] = 0

    return render_template('home.html', grid=game.grid, score=session.get("score", "not set"))

@app.route('/new_game')
def new_game():
    game = Game()
    # Set initial score

    return render_template('home.html', grid=game.grid, score=session.get("score", "not set"))

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid, score = game.is_valid(word)
    session["score"] += score
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word, score=session.get("score", "not set"))
