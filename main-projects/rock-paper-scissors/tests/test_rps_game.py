import builtins
import runpy
import sys
from pathlib import Path

### Writing a pytest test for interactive Python script.
### This uses mocking to control user input and randomness.

# Ensure project root is on the right Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


# Test user win handled
def test_user_wins_round(monkeypatch, capsys):
    """
    User chooses rock, computer chooses scissors.
    Expect a win message.
    """

    inputs = iter(["rock", "n"])  # user choice  # stop playing

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr("random.choice", lambda _: "scissors")

    runpy.run_module("rps_game")  # Test module

    captured = capsys.readouterr()  # Check test output
    assert "You win!" in captured.out


# Test for draw handled
def test_draw_round(monkeypatch, capsys):
    """
    User and computer choose the same option.
    Expect a draw message.
    """

    inputs = iter(["paper", "n"])  # user choice  # stop playing

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr("random.choice", lambda _: "paper")

    runpy.run_module("rps_game")  # Test module

    captured = capsys.readouterr()  # Check test output
    assert "It's a draw!" in captured.out


# Test for invalid input handling
def test_invalid_inp_then_valid_choice(monkeypatch, capsys):
    # Set possible inputs
    inputs = iter(
        ["banana", "rock", "n"]  # invalid input  # valid input after retry  # stop game
    )

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))  # Simulate user inp
    monkeypatch.setattr("random.choice", lambda _: "scissors")  # Simulate computer inp

    runpy.run_module("rps_game")  # Test module

    captured = capsys.readouterr()  # Check test output
    assert "Invalid choice. Please enter another option" in captured.out
    assert "You win!" in captured.out
