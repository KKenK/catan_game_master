class Army():
    def __init__(self, settler_id, knights):
        self.settler_id = settler_id
        self.knights = knights
        self.strength = sum([knight.level for knight in knights if knight.is_active])

    def print_army_dict(self):
        print(self.__dict__)

