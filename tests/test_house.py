from lib.house import *

"""
The user can set the house number and door colour.
Ensure their choices are stored correctly, and there are
two floors as user story instructs.
"""

def test_house_parameters():
    house = House(137, "white")
    assert house.number == 137 and house.colour == "white" \
    and house.floors == 2


"""
When we have a house, the key details can be got back.
"""

def test_correct_details_returned():
    house = House(137, "white")
    assert house.get_details() == "House number 137 has 2 floors and a white door."

"""
When we have a house, and when we change its door colour
this gets reflected in its attribute.
"""

def test_repaint_door():
    house = House(24, "red")
    house.repaint_door("blue")
    assert house.colour == "blue"
