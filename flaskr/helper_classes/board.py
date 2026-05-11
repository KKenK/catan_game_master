class Board():
    def __init__(self):

        self.tiles = self.generate_board_tiles()

    def generate_board_tiles(self):

        id = 0

        board = []

        for tile_count in [3,4,5,4,3]:

            row = []

            for number in range(tile_count):

                row.append(Hexagon(id))

                id += 1
            
            board.append(row)

        return board

    def print_board(self):

        for row in self.tiles:

            spaces = 7 - len(row)

            print(spaces * '-' + ','.join([str(hexagon.id) for hexagon in row]) + spaces * '-')
