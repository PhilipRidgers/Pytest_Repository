from lib.report_length import report_length

def test_string_is_correct_length():
    result = report_length("example")
    assert result == f"This string was 7 characters long."
