from lib.check_codeword import *

def test_check_codewords_checks_outputs_correctly():
    correct = check_codeword("horse")
    almost = check_codeword("horze")
    wrong = check_codeword("phorse")

    assert correct == "Correct! Come in."
    assert almost == "Close, but nope."
    assert wrong == "WRONG!"

