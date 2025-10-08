class HousingEstate():
    def __init__(self):
        self.houses = []
    
    def get_house_numbers(self):
        house_numbers = []
        for house in self.houses:
            house_numbers.append(house.number)
        return house_numbers
        



















"""
item1 = Item("Chair")
item2 = Item("Moisturiser")
order = Order("123 Fake Street")
order.items.append(item1)
order.items.append(item2)
order.items
for item in order.items:
    print(item.product_type) 

house1 = House(137, "white")
house2 = House(24, "red")
housing_estate = HousingEstate()
housing_estate.houses.append(house1)
housing_estate.houses.append(house2)
housing_estate.houses
"""