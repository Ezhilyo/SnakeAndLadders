from typing import List

from components.cell import Cell
from components.ladder import Ladder
from components.snake import Snake
from move import Move
from player import Player
import random


class Board:

    def __init__(self, length: int, final_pos: int, no_of_ladders: int, no_of_snakes: int):
        self.moves = []
        self.board = {}
        self.length = length
        self.player_pos = {}
        self.final_pos = final_pos
        self.no_of_snakes = no_of_snakes
        self.no_of_ladders = no_of_ladders

    def initialize_board(self, players: List[Player]):
        for i in range(self.no_of_ladders):
            lad_start, ladd_end = sorted(random.sample(range(100), 2))
            self.board.update({lad_start: Ladder(lad_start, ladd_end)})
        i = 0
        while i < self.no_of_snakes:
            sn_start, sn_end = reversed(sorted(random.sample(range(100), 2)))
            if not self.board.get(sn_start) and not sn_start == self.final_pos-1:
                self.board.update({sn_start: Snake(sn_start, sn_end)})
                i += 1
        for i in range(100):
            if not self.board.get(i):
                self.board.update({i: Cell(i, i)})

        for player in players:
            self.player_pos.update({player: 1})

    def start_game(self, players: List[Player]):
        while True:
            for player in players:
                dice = random.randint(1, 6)
                latest_pos = self.move(player, dice)
                if latest_pos == self.final_pos-1:
                    return player

    def move(self, player: Player, die_num: int):
        player_curr_pos = self.player_pos.get(player)
        if player_curr_pos+die_num > self.length:
            return None
        new_pos = player_curr_pos+die_num
        if new_pos >= 100:
            return player_curr_pos
        print(f"player {player.name} moved from {player_curr_pos} to {new_pos}")
        moved_pos = self.board.get(new_pos).get_next_pos(new_pos)
        if new_pos != moved_pos:
            self.moves.append(Move(player, die_num, new_pos, moved_pos, self.board.get(new_pos).get_type()))
        self.player_pos.update({player: moved_pos})
        return moved_pos

