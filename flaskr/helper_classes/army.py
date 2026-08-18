class Army():
    def __init__(self, knights, settler_id):
        self.settler_id = settler_id
        self.knights = knights
        self.army_strength = sum([knight.level for knight in knights if knight.is_active])



