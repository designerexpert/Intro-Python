class Room:
    def __init__(self, name, description, n_to=None, e_to=None, w_to=None, s_to=None, inventory=None, is_lit=False):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.w_to = w_to
        self.s_to = s_to
        self.is_lit = is_lit
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory