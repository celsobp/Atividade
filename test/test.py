from src.main import *
from unittest.mock import patch


def test_lado():
    assert lado() == 6

def test_dados():
    assert dados() == 2


def test_rolar(totadados, lados):
    with patch('random.randint', return_value=5):
        result = rolar(2, 6)

    assert result == 5