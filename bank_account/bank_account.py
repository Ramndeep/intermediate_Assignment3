"""
Description: This file contains the main BankAccount class implementing the Strategy Pattern.
Author: Ramandeep Kaur
Date: 2 Novemeber 2024
"""

class BankAccount:
    """
    Represents a generic bank account with encapsulated attributes.

    Attributes:
        account_number (int): Unique identifier for the account.
        client_number (int): Unique identifier for the client.
        balance (float): The account balance.
        service_charge_strategy (ServiceChargeStrategy): Strategy for calculating service charges.
    """

    def __init__(self, account_number, client_number, balance=0.0, service_charge_strategy=None):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")

        self._account_number = account_number
        self._client_number = client_number
        self._balance = float(balance)
        self.service_charge_strategy = service_charge_strategy

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        """Deposit an amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw an amount from the account."""
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def calculate_service_charge(self):
        """Calculate the service charge using the assigned strategy."""
        if self.service_charge_strategy:
            return self.service_charge_strategy.calculate_charge(self)
        return 0.0  # Default to zero if no strategy is set

    def __str__(self):
        return f"BankAccount(account_number={self._account_number}, balance={self._balance})"
