from components.component import Component


class Cell(Component):

    def __init__(self, start_pos, end_pos):
        super().__init__(start_pos)
        self.end_pos = end_pos

    def get_next_pos(self, curr_pos):
        if curr_pos != self.start_pos:
            raise Exception("Invalid move")
        return self.end_pos
