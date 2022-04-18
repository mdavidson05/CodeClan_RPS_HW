from models.game import *
from models.player_list import *
from models.game_list import *

# game = Game(player1,player2)
game_list = []
result = []
def add_to_game_list(game):
        game_list.clear()
        game_list.append(game)


def determine_winner(match):
        for players in game_list:
                print(players.player1)
                print(players.player2)

                if players.player1 == "rock" and players.player2 == "paper":
                        result.clear()
                        result.append("Player 2 wins")

                elif players.player1 == "paper" and players.player2 == "rock":
                        result.clear()
                        result.append("Player 1 wins")

                elif players.player1 == "scissors" and players.player2 == "rock":
                        result.clear()
                        result.append("Player 2 wins")

                elif players.player1 == "rock" and players.player2 == "scissors":
                        result.clear()
                        result.append("Player 1 wins")

                elif players.player1 == "scissors" and players.player2 == "paper":
                         result.clear()
                         result.append("Player 1 wins")

                elif players.player1 == "paper" and players.player2 == "scissors":
                         result.clear()
                         result.append("Player 2 wins")
                
                elif players.player1 == "paper" and players.player2 == "rock":
                        result.clear()
                        result.append("Player 1 wins")

                elif players.player1 == "rock" and players.player2 == "paper":
                        result.clear()
                        result.append("Player 2 wins")
                
                elif players.player1 == players.player2:
                        result.clear()
                        result.append("Draw")

                else:
                        print("Try again")

        

