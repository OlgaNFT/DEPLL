import pytest
from main import greet

def test_greet_output(capsys):
    greet("Tester")
    captured = capsys.readouterr()
    assert "Hello, Tester!" in captured.out
