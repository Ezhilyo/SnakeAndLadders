from components.component import Component
from move_type import MoveType


class Snake(Component):

    def __init__(self, start_pos, end_pos):
        super().__init__(start_pos)
        self.end_pos = end_pos

    def get_next_pos(self, curr_pos: int):
        if curr_pos != self.start_pos:
            raise Exception("Invalid move")
        return self.end_pos

    def get_type(self):
        return MoveType.SNAKE
