from .hexagon import Hexagon

class Settlement():

    def __init__(self, settlement_row):

        self.id = settlement_row['id']
        self.settler_id = settlement_row['settler_id']
        self.resource_hexes = [Hexagon(roll = settlement_row['roll_1'], resource = settlement_row['resource_1']),
                        Hexagon(roll = settlement_row['roll_2'], resource = settlement_row['resource_2']),
                        Hexagon(roll = settlement_row['roll_3'], resource = settlement_row['resource_3'])]
        self.is_city = settlement_row['is_city']