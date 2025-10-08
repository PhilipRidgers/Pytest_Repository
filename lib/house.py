class House():
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour
        self.floors = 2
    
    def get_details(self):
        details = f"House number {self.number} has {self.floors} " \
        + f"floors and a {self.colour} door."
        return details
    
    def repaint_door(self, door_colour):
        self.colour = door_colour