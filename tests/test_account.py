import pytest
from bank_account import BankAccount


def test_initial_balance():
    account = BankAccount("Alice", 100)
    assert account.get_balance() == 100


def test_withdraw_insufficient_balance():
    account = BankAccount("Bob", 50)
    with pytest.raises(ValueError, match="Insufficient balance"):
        account.withdraw(100)
