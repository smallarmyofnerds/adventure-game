class Portal:
    def __init__(self, dest):
        self.dest = dest
    
    def can_pass(self, inventory):
        return True

class LockedPortal(Portal):
    def __init__(self, dest, key_name):
        super(LockedPortal, self).__init__(dest)
        self.key_name = key_name

    def can_pass(self, inventory):
        return inventory.find(self.key_name) is not None