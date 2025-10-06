from lib.string_builder import StringBuilder

def test_empty_string():
    empty_string = StringBuilder()
    assert empty_string.output() == ""

def test_one_string():
    one_string = StringBuilder()
    one_string.add("This is a test.")
    result = one_string.output()
    assert result == "This is a test."

def test_len_one_string():
    one_string = StringBuilder()
    one_string.add("test")
    assert one_string.size() == 4
    

def test_multi_strings():
    multi_string = StringBuilder()
    multi_string.add("This is ")
    multi_string.add("a test.")
    result = multi_string.output()
    assert result == "This is a test."

def test_len_one_string():
    multi_string = StringBuilder()
    multi_string.add("This is")
    multi_string.add("a test.")
    assert multi_string.size() == 14