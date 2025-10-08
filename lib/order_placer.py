class Order():
    def __init__(self, address):
        self.address = address
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def format_note(self):
        order_details = ", ".join(self.items)
        return f"Order for {self.address}: {order_details}"

"""
order = Order("123 Fake Street")
order.add_item("Chair")
order.add_item("Moisturiser")
order.format_note()
order.items
"""