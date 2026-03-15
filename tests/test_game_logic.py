# SIMPLIFIED TESTS
# from logic_utils import check_guess

# def test_winning_guess():
#     # If the secret is 50 and guess is 50, it should be a win
#     outcome, message = check_guess(50, 50)
#     assert outcome == "Win"

# def test_guess_too_high():
#     # If secret is 50 and guess is 60, hint should be "Too High"
#     outcome, message = check_guess(60, 50)
#     assert outcome == "Too High"

# def test_guess_too_low():
#     # If secret is 50 and guess is 40, hint should be "Too Low"
#     outcome, message = check_guess(40, 50)
#     assert outcome == "Too Low"

# MORE COMPLEX TESTS
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests targeting the swapped-hint bug (guess > secret said "Go HIGHER!" instead of "Go LOWER!")
def test_too_high_message_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say Go LOWER, got: {message}"

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say Go HIGHER, got: {message}"
