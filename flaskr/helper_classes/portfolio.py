class Portfolio():

    def __init__(self, settlements, metropolises, settler_id):
        self.settler_id = settler_id
        self.settlements = settlements
        self.metropolises = metropolises
        self.value = self._calculate_portfolio_value()

    def _calculate_portfolio_value(self):

        settlement_value = len([settlement for settlement in self.settlements if not settlement.is_city])

        city_value = len([settlement for settlement in self.settlements if settlement.is_city]) * 2 

        metropolis_value = len(self.metropolises) * 2

        return settlement_value + city_value + metropolis_value

    def print(self):
        print(f"""settler id: {self.settler_id} 
        number of settlements: {len(self.settlements)}
        value: {self.value}
        """)