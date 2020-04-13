#!/usr/bin/python3

# Consts
ALIVE = True
DEAD = False
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

    def create_cells(self):
        for row in range(self.size[0]):
            self.cells.append([Cell()])
            for col in range((self.size[1] - 1)):
                self.cells[row].append(Cell())
        self.update_num_cells()

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
    current_state = None
    next_state = None 
    neighbours_states = []

    def __init__(self):
       self.current_state = None 
       self.next_state = None
       self.neighbours_states = None  

    def get_current_state(self):
        return self.current_state
    def get_next_state(self):
        return self.next_state
    def get_neighbours_states(self):
        return self.neighbours_states
    
    def set_current_state(self, state):
        self.current_state = state
    def set_next_state(self, state):
        self.next_state = state
    def set_neighbours_states(self, states):
        self.neighbours_states = states  # TODO: fix for list


def main():
    life = Life([10,10], 100, 0)
    print(life.get_num_cells())

if __name__ == "__main__":
    main()