class Settlement():

    def __init__(self, settlement_row):

        self.id = settlement_row['id']
        self.settler_id = settlement_row['settler_id']
        self.resource_1 = settlement_row['resource_1']
        self.roll_1 = settlement_row['roll_1']
        self.resource_2 = settlement_row['resource_2']
        self.roll_2 = settlement_row['roll_2']
        self.resource_3 = settlement_row['resource_3']
        self.roll_3 = settlement_row['roll_3']
        self.is_city = settlement_row['is_city']