from lib.order_placer import *

def test_adding_two_items():
    order = Order("123 Fake Street")
    order.add_item("Chair")
    order.add_item("Moisturiser")
    assert order.items == ["Chair", "Moisturiser"]