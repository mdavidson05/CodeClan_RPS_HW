from models.player import *

player1_move = "list"
player2_move = "test"

def input_to_list(player1_input,player2_input):
    player1_move = player1_input
    player2_move = player2_input
    
player1 = Player("Player 1", player1_move)
player2 = Player("Player 2", player2_move)
players = [player1, player2]

# def input_to_list(player1_input,player2_input):
#     player1_move = player1_input
#     player2_move = player2_input


def add_new_player(player):
        players.append(player)