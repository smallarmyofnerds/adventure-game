class Inventory:
    def __init__(self):
        self.inventory = []
    
    def __repr__(self):
        return str(self.inventory)

    def pocket(self, pickup):
        self.inventory.append(pickup)
    
    def find(self, pickup_name):
        for item in self.inventory:
            if item == pickup_name:
                return item
        return None   
    
    def get_items(self):
        return self.inventory
    
    