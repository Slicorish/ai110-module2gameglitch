from app import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_outcome():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low_outcome():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_too_high_hints_to_go_lower():
    # Regression test: guessing above the secret must tell the player
    # to go LOWER, not higher. This is the exact bug that was reported.
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_guess_too_low_hints_to_go_higher():
    # Regression test: guessing below the secret must tell the player
    # to go HIGHER, not lower. This is the exact bug that was reported.
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()
