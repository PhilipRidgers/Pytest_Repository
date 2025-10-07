import pytest
from lib.present import *

def test_can_wrap():
    present = Present()
    present.wrap(3)
    assert present.unwrap() == 3

def test_is_already_wrapped():
    present = Present()
    present.wrap(3)
    with pytest.raises(Exception) as err:
        present.wrap(3)
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_nothing_to_unwrap():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."