class Army():
    def __init__(self, knights):
        self.settler_id = knights[0]['settler_id']
        self.knights = knights
        self.army_strength = sum([knight['level'] for knight in knights if not knights['is_active']])



