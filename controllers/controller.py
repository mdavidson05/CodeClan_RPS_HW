from app import app
from models.game_list import *
from models.player_list import *
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('index.html', title ="Home", gamers = game_list, player_list=players) 

@app.route('/game', methods = ['POST'])
def game():
    
    player_1 = request.form["title"]
    player_2 = request.form["p2"]

    print(player_1)
    print(player_2)
    print(request.form)

    game = Game(player_1,player_2)

    add_to_game_list(game)
    determine_winner(game)

    return render_template('index.html', title ="Results", gamers = game_list, results=result)

@app.route('/welcome', methods = ['GET'])
def results():
    return render_template('welcome.html', title = "welcome")