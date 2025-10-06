from lib.counter import *

def initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counts_single_number():
    count = Counter()
    count.add(6)
    result = count.report()
    assert result == "Counted to 6 so far."

def test_counter_adds_multiple_numbers_to_the_count():
    count = Counter()
    count.add(5)
    count.add(3)

    assert count.report() == "Counted to 8 so far."