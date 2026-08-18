class Settler():
    def __init__(self, settler_row):
            
        self.username = settler_row['username']
        self.victory_point_card = settler_row['victory_point_card'] 
        self.longest_road  = settler_row['longest_road']
        self.has_longest_road  = settler_row['has_longest_road']
        self.defender_of_catan = settler_row['defender_of_catan']
        
    def calculate_victory_points(self, settler_portfolio_worth):

        longest_road_victory_points = 2 if self.has_longest_road else 0
  
        return self.victory_point_card + self.defender_of_catan + longest_road_victory_points + settler_portfolio_worth