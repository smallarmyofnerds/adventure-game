class Portal:
    def __init__(self, dest, *args, **kwargs):
        self.dest = dest
        self.pass_message = kwargs.get("pass_message", None)
        self.blocked_message = kwargs.get("blocked_message", None)
    
    def can_pass(self, inventory):
        return True
    
    def get_dest(self, inventory):
        return self.dest

class LockedPortal(Portal):
    def __init__(self, dest, key_name, *args, **kwargs):
        super(LockedPortal, self).__init__(dest, *args, **kwargs)
        self.key_name = key_name

    def can_pass(self, inventory):
        return inventory.find(self.key_name) is not None

class WinPortal(LockedPortal):
    def __init__(self, dying_dest, key_name, thing_1_name, thing_2_name, winning_dest, *args, **kwargs):
        super(WinPortal, self).__init__(dying_dest, key_name, *args, **kwargs)
        self.thing_1_name = thing_1_name
        self.thing_2_name = thing_2_name
        self.winning_dest = winning_dest
    
    def get_dest(self, inventory):
        item_1 = inventory.find(self.thing_1_name)
        item_2 = inventory.find(self.thing_2_name)
        if item_1 is not None and item_2 is not None:
            return self.winning_dest
        else:
            return self.dest

class ClearingWinPortal(Portal):
    def __init__(self, dying_dest, thing_1_name, thing_2_name, winning_dest, *args, **kwargs):
        super(ClearingWinPortal, self).__init__(dying_dest, *args, **kwargs)
        self.thing_1_name = thing_1_name
        self.thing_2_name = thing_2_name
        self.winning_dest = winning_dest
    
    def get_dest(self, inventory):
        item_1 = inventory.find(self.thing_1_name)
        item_2 = inventory.find(self.thing_2_name)
        if item_1 is not None and item_2 is not None:
            return self.winning_dest
        else:
            return self.dest