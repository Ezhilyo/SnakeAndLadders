from move_type import MoveType


class Move:

    def __init__(self, player, die_num, first_pos, final_pos, move_type: MoveType):
        self.player = player
        self.die_num = die_num
        self.first_pos = first_pos
        self.final_pos = final_pos
        self.move_type = move_type
        print(f"{player.name} got a {move_type.value} and moved from {first_pos} to {final_pos}")
