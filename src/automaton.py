class Automaton:
    def __init__(self):
        self._input = None

    def set_input(self, score_card):
        self._input = score_card

    def output(self):
        if self._input is None:
            return 0
        return self._input.score()
