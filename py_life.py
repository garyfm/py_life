#!/usr/bin/python3

# Consts
ALIVE = True
DEAD = False
NUM_NEIGH_CELLS = 8
# Colors
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

class Life:
    'Life Universe Class'
    seed = []
    size = [0, 0]
    end_tick = 0
    current_tick = 0
    cells = []
    num_cells = 0
    
    def __init__(self, size, end_tick, seed):
        print(GREEN + "Created Life Universe" + ENDC)
        self.size = size
        self.end_tick = end_tick
        self.seed = seed
        self.current_tick = 0
        self.create_cells()    
        self.seed_life()
        self.print_life()
        self.run_life()

    def create_cells(self):
        for row in range(self.size[0]):
            self.cells.append([Cell()])
            for col in range((self.size[1] - 1)):
                self.cells[row].append(Cell())
        self.update_num_cells()

    def seed_life(self):
        # Seed fixed to centre for now
        x, y = self.get_life_centre()
        rows = len(self.seed)
        cols = len(self.seed[0])

        for row in range(rows):
            self.cells[x + row][y].set_state(self.seed[0][row])
#            self.print_life()
            for col in range(cols):
                self.cells[x + row][y + col].set_state(self.seed[row][col])
#                self.print_life()

    def run_life(self):
        cell = self.cells[5][5]
        cell.probe_neighbours(self, 5, 5)
        print(cell.get_neighbours_states())

    def print_life(self):
        for row in self.cells:
            for cell in row:
                print("[" + str(cell.get_current_state()) + "],", end = '')
            print("\r\n")

    def get_life_centre(self):
        centre_x = int(len(self.cells) / 2) 
        centre_y = int(len(self.cells[0]) / 2)
        return centre_x, centre_y

    def get_num_cells(self):
        return self.num_cells 
    def update_num_cells(self):
        nrow = len(self.cells)
        ncols = len(self.cells[0])
        self.num_cells = nrow * ncols

    def get_size(self):
        return self.size
    def get_end_tick(self):
        return self.ticks
    def get_tick(self):
        return self.current_tick        
    def inc_ticks(self):
        self.current_tick += 1

class Cell:
    'Cell Class'
    state = DEAD
    next_state = None 
    neigh_states = []

    def __init__(self):
       self.neighbours_states = None  

    def get_current_state(self):
        return self.state
    def get_next_state(self):
        return self.next_state
    def get_neighbours_states(self):
        return self.neigh_states
    
    def set_state(self, state):
        self.state = state
    def set_next_state(self, state):
        self.next_state = state
    def set_neighbours_states(self, states):
        self.neighbours_states = states 

    def probe_neighbours(self, life, row, col):
        self.neigh_states.append(life.cells[row - 1][col - 1].get_current_state())
        self.neigh_states.append(life.cells[row - 1][col].get_current_state())
        self.neigh_states.append(life.cells[row - 1][col + 1].get_current_state())
        self.neigh_states.append(life.cells[row][col + 1].get_current_state())
        self.neigh_states.append(life.cells[row + 1][col + 1].get_current_state())
        self.neigh_states.append(life.cells[row + 1][col].get_current_state())
        self.neigh_states.append(life.cells[row + 1][col - 1].get_current_state())
        self.neigh_states.append(life.cells[row][col - 1].get_current_state())

def main():

    init_seed = [[ALIVE, ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, DEAD, DEAD]]

    life = Life([10,10], 100, init_seed)
    print(life.get_num_cells())

if __name__ == "__main__":
    main()