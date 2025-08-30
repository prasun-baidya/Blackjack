import pytest
from main import deal_card, calculate_score, compare_scores

# test_main.py


def test_deal_card_returns_valid_card():
    valid_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for _ in range(100):
        card = deal_card()
        assert card in valid_cards

def test_calculate_score_blackjack():
    assert calculate_score([11, 10]) == 0
    assert calculate_score([10, 11]) == 0

def test_calculate_score_ace_conversion():
    # 11 + 9 + 5 = 25, should convert ace to 1, so 1+9+5=15
    assert calculate_score([11, 9, 5]) == 15

def test_calculate_score_no_ace_no_blackjack():
    assert calculate_score([10, 9]) == 19

def test_calculate_score_over_21_with_ace():
    # 11 + 10 + 2 = 23, should convert ace to 1, so 1+10+2=13
    assert calculate_score([11, 10, 2]) == 13

def test_calculate_score_over_21_without_ace():
    assert calculate_score([10, 10, 5]) == 25

def test_compare_scores_draw():
    assert compare_scores(18, 18) == "Draw"

def test_compare_scores_computer_blackjack():
    assert compare_scores(18, 0) == "Lose, opponent has Blackjack"

def test_compare_scores_user_blackjack():
    assert compare_scores(0, 18) == "Win with a Blackjack"

def test_compare_scores_user_bust():
    assert compare_scores(22, 18) == "You went over. You lose"

def test_compare_scores_computer_bust():
    assert compare_scores(18, 22) == "Opponent went over. You win"

def test_compare_scores_user_win():
    assert compare_scores(20, 18) == "You win"

def test_compare_scores_user_lose():
    assert compare_scores(18, 20) == "You lose"