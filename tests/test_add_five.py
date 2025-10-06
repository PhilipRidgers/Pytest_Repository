# This imports the function we're testing.
from lib.add_five import *

# Function name has to start with "test", and the rest of the name should
# describe what the test verifies.
def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

# Pytest will run this example, and if this example doesn't work like you
# said it would, the test fails.