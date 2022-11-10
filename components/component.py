import abc


class Component(abc.ABC):

    def __init__(self, start_pos):
        self.start_pos = start_pos

    @abc.abstractmethod
    def get_next_pos(self, curr_pos: int):
        pass
