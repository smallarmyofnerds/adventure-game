class Portal:
    def __init__(self, dest, *args, **kwargs):
        self.dest = dest
        self.pass_message = kwargs.get("pass_message", None)
        self.blocked_message = kwargs.get("blocked_message", None)
    
    def can_pass(self, inventory):
        return True

class LockedPortal(Portal):
    def __init__(self, dest, key_name, *args, **kwargs):
        super(LockedPortal, self).__init__(dest, *args, **kwargs)
        self.key_name = key_name

    def can_pass(self, inventory):
        return inventory.find(self.key_name) is not None

class WinPortal(Portal):
    def __init__(self, dest, key_1_name, key_2_name, *args, **kwargs):
        super(WinPortal, self).__init__(dest, *args, **kwargs)
        self.key_1_name = key_1_name
        self.key_2_name = key_2_name
    
    def can_pass(self, inventory):
        return (inventory.find(self.key_1_name) is not None) and (inventory.find(self.key_2_name) is not None)
