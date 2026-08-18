class Portfolio():

    def __init__(self, settlements, settler_id):
        self.settler_id = settler_id
        self.settlements = settlements
        self.value = self._calculate_portfolio_value()

    def _calculate_portfolio_value(self):

        settlement_value = len([settlement for settlement in self.settlements if not settlement['is_city']])

        city_value = len([settlement for settlement in self.settlements if settlement['is_city']]) * 2 

        return settlement_value + city_value