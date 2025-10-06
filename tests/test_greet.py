from lib.greet import *

def test_greet_gives_correct_name():
    result = greet("Philip")
    assert result == "Hello, Philip!"