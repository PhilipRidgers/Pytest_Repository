from lib.password_checker import *
import pytest

def test_password_is_long_enough():
    password = PasswordChecker()
    assert password.check("long enough") == True

def test_password_returns_error_message_when_too_short():
    password = PasswordChecker()
    with pytest.raises(Exception) as err:
        password.check("short")
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."
