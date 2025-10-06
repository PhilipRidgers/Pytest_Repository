from lib.gratitudes import *

"""
An empty gratitudes list should return "Be grateful for: "
"""

def test_start_with_empty_list():
    grateful = Gratitudes()
    result = grateful.format()
    assert result == "Be grateful for: "

"""
Adding a gratitude to a list should return
e.g "Be grateful for: music"
"""

def test_add_one_to_list():
    grateful = Gratitudes()
    grateful.add("music")
    result = grateful.format()
    assert result == "Be grateful for: music"

"""
Adding multiple items to the list should return them
with commas in between. E.g. "Be grateful for: music, art, "sleep"
"""

def test_add_multi_to_list():
    grateful = Gratitudes()
    grateful.add("music")
    grateful.add("art")
    grateful.add("sleep")
    result = grateful.format()
    assert result == "Be grateful for: music, art, sleep"