class Room:
    def __init__(self, name, desc, exits, *args, **kwargs):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.is_game_over = kwargs.get('is_game_over', False)
        self.is_win_game = kwargs.get("is_win_game", False)
        self.objects = kwargs.get('objects', [])
    
    def get_exit(self, direction):
        return self.exits.get(direction)
    
    def get_exit_directions(self):
        return list(self.exits.keys())
    
    def get_items(self):
        return self.objects
    
    def get_item(self, item_name):
        for item in self.objects:
            if item == item_name:
                return item
        
        return None
    
    def remove_item(self, item_name):
        self.objects.remove(item_name)
                