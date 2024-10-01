from src.main import *
from unittest.mock import patch


def test_lado():
    assert lado() == {"teste": False, "num_lados": 5}

def dados():
    assert dados() == 0


def rolar(totaldados, lados):
    totaldados = 2
    lados = 10
    with patch('random.randint', return_value=7):
        result = rolar(totalDados, lados)

    assert result == {"teste": True, "soma": 14}