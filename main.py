

from board import Board
from player import Player

players = [Player(1, "a"), Player(2, "b"), Player(3, "c"), Player(4, "d")]
b = Board(100, 100, 6, 7)

b.initialize_board(players)
print(b.board)
won_player = b.start_game(players)
print(f"player {won_player.name} won")
