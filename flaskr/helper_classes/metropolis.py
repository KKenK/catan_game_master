class Metropolis():
    def __init__(self, row_object):
        self.id = row_object['city_improvement']
        self.level = row_object['level']
        self.settler_id = row_object['settler_id']
        self.settlement_id = row_object['settlement_id']