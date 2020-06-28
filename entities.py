class Cell:

    def __init__(self, initial_status):
        self.is_alive = initial_status
        self.neighbors = list()
        self.next_status = None

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

    def should_live(self):
        neighbors_alive = sum([neighbor.is_alive for neighbor in self.neighbors])
        if neighbors_alive == 3 or (neighbors_alive == 2 and self.is_alive):
            self.next_status = True
        else:
            self.next_status = False

    def next_generation(self):
        self.is_alive = self.next_status


 
class Board:

    def __init__(self, matrix):

        self.width = len(matrix)
        self.height = len(matrix[0])


        self.matrix = list()
        self.cells = list()
        
        for y_value in range(0, self.height):
            self.matrix.append(list())
            for x_value in range(0, self.width): 
                new_cell = Cell(bool(matrix[x_value][y_value]))
                self.matrix[y_value].append(new_cell)
                self.cells.append(new_cell)

        self.set_neighbors()

    def set_neighbors(self):
        for x_value in range(0,self.width):
            for y_value in range(0,self.height):
                neighbors_positions = ((x_value-1,y_value-1),(x_value, y_value-1),(x_value+1,y_value-1),
                                        (x_value-1, y_value),(x_value+1, y_value),
                                        (x_value-1, y_value+1), (x_value, y_value+1), (x_value+1,y_value+1))
                neighbors_list = list()
                for neighbors_position in neighbors_positions:
                    try:
                        if (neighbors_position[0] >= 0 and neighbors_position[1] >= 0) and (neighbors_position[0] < self.width and neighbors_position[1] < self.height):
                            print(neighbors_position[0],neighbors_position[1])
                            neighbors_list.append(self.matrix[neighbors_position[0]][neighbors_position[1]])
                    except Exception:
                        exit()
                self.matrix[x_value][y_value].set_neighbors(neighbors_list)


    def next_generation(self):
        for cell in self.cells:
            cell.should_live()
        for cell in self.cells:
            cell.next_generation()

class BoardPrinter:
    def print_board(self, board):
        for height in range(0, board.height):
            print([int(board.matrix[width][height].is_alive) for width in range(0, board.width)])