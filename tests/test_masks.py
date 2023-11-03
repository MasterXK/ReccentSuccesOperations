import pytest

from src.masks import create_account_mask, create_card_mask


@pytest.fixture
def card():
    return 7000792289606361


@pytest.fixture
def account():
    return 73654108430135874305


def test_create_card_mask(card):
    assert create_card_mask(card) == "7000 79** **** 6361"


def test_create_account_mask(account):
    assert create_account_mask(account) == "**4305"
