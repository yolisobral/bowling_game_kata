import pytest

from src.automaton import Automaton
from src.scoreCard import ScoreCard

cases = [
pytest.param("12345123451234512345", 60, marks=pytest.mark.state_n),
pytest.param("9-9-9-9-9-9-9-9-9-9-", 90, marks=pytest.mark.state_n),
pytest.param("9-3561368153258-7181", 82, marks=pytest.mark.state_n),
pytest.param("9-3/613/815/-/8-7/8-", 121, marks=pytest.mark.spare),
pytest.param("X9-9-9-9-9-9-9-9-9-", 100, marks=pytest.mark.strike),
pytest.param("X9-X9-9-9-9-9-9-9-", 110, marks=pytest.mark.strike),
pytest.param("XX9-9-9-9-9-9-9-9-", 120, marks=pytest.mark.strike),
pytest.param("XXX9-9-9-9-9-9-9-", 141, marks=pytest.mark.strike),
pytest.param("9-3/613/815/-/8-7/8/8", 131, marks=pytest.mark.extra_rolls),
pytest.param("5/5/5/5/5/5/5/5/5/5/5", 150, marks=pytest.mark.extra_rolls),
pytest.param("9-9-9-9-9-9-9-9-9-XXX", 111, marks=pytest.mark.extra_rolls),
pytest.param("8/549-XX5/53639/9/X", 149, marks=pytest.mark.extra_rolls),
pytest.param("X5/X5/XX5/--5/X5/", 175, marks=pytest.mark.extra_rolls),
pytest.param("XXXXXXXXXXXX", 300, marks=pytest.mark.extra_rolls),
]

@pytest.mark.parametrize("pins,total", cases)
def test_score_cases(pins, total):
    automata = Automaton()
    score_card = ScoreCard(pins)
    automata.set_input(score_card)
    assert automata.output() == total