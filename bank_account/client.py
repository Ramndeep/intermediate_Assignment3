"""
Description: This file contains the Client class with validation logic.
Author: Ramandeep Kaur
Date: 2 Novemeber 2024
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Represents a client with personal details and validation.
    
    Attributes:
        client_number (int): Unique identifier for the client.
        first_name (str): First name of the client.
        last_name (str): Last name of the client.
        email_address (str): Email address of the client.
    """

    def __init__(self, client_number, first_name, last_name, email_address):
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        if not first_name.strip():
            raise ValueError("First name cannot be blank.")
        if not last_name.strip():
            raise ValueError("Last name cannot be blank.")

        self._client_number = client_number
        self._first_name = first_name.strip()
        self._last_name = last_name.strip()

        # Validate email address
        try:
            self._email_address = validate_email(email_address).email
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email address: {e}")

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def __str__(self):
        return f"Client(client_number={self._client_number}, name={self.full_name})"
