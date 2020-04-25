#!/usr/bin/python3
import time
import pygame

# Consts
ALIVE = True
DEAD = False
NUM_NEIGH_CELLS = 8
# Colors
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'
#Display
FPS = 60 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CELL_SIZE = 10
DISPLAY_X = 200
DISPLAY_Y = 200

class Life:
    'Life Universe Class'
    seed = []
    size = [0, 0]
    end_tick = 0
    current_tick = 0
    cells = []
    num_cells = 0
    board = None 
    
    def __init__(self, size, end_tick, seed):
        self.size = size
        self.end_tick = end_tick
        self.seed = seed
        self.current_tick = 0
        self.board = self.init_display(DISPLAY_X, DISPLAY_Y)
        self.create_cells()    
        self.seed_life()
        self.run_life()

    def create_cells(self):
        print(GREEN + "Created Life Universe" + ENDC)
        for row in range(self.size[0]):
            self.cells.append([Cell()])
            for col in range((self.size[1] - 1)):
                self.cells[row].append(Cell())
        self.update_num_cells()

    def seed_life(self):
        print(GREEN + "Seeding Life" + ENDC)
        # Seed fixed to centre for now
        x, y = self.get_life_centre()
        rows = len(self.seed)
        cols = len(self.seed[0])

        for row in range(rows):
            self.cells[x + row][y].set_state(self.seed[0][row])
            for col in range(cols):
                self.cells[x + row][y + col].set_state(self.seed[row][col])
                pygame.draw.rect(self.board, WHITE, (x + row, y + col, CELL_SIZE,  CELL_SIZE))
                pygame.display.flip()

    def run_life(self):
        print(GREEN + "Running Life" + ENDC)

        for tick in range(self.end_tick):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(RED + str(event) + ENDC)
                    quit()
     
            for row, row_cells in enumerate(self.cells):
                for col, cell in enumerate(row_cells):
                    cell.probe_neighbours(self, row, col)
                    cell.get_next_gen()
                    cell.update()
                    print("Cell [" + str(row) + "," + str(col) + "]: " + str(cell.state))

                    if cell.state == None:
                        print(RED + "ERROR STATE NONE" + ENDC) 

                    if cell.state == ALIVE:
                        pygame.draw.rect(self.board, WHITE, (row, col, CELL_SIZE,  CELL_SIZE))
                    else:
                        pygame.draw.rect(self.board, BLACK, (row, col, CELL_SIZE,  CELL_SIZE))

                    pygame.display.flip()
                    time.sleep(1)
            print(GREEN + "GEN: " + str(tick) + ENDC)
            time.sleep(5)

    def init_display(self, x_size, y_size):
        pygame.init()
        screen = pygame.display.set_mode((x_size , y_size)) 
        clock = pygame.time.Clock()
        pygame.display.set_caption('PYLIFE')
        clock.tick(60)
        return screen

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

    
class Cell:
    'Cell Class'
    state = DEAD
    next_state = DEAD 
    neigh_states = [DEAD]

    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    
    def probe_neighbours(self, life, row, col):
        # Loop over each possible transform to get each neightbouring cell
        for row_trans in [1, 0, -1]:
            for col_trans in [1, 0, -1]:
                # Check if neighbouring cell is out of bounds
                neigh_pos = [row + row_trans, col + col_trans]
                if ((neigh_pos[0] < 0) | (neigh_pos[0] > (life.size[0] - 1))):
                    break
                if ((neigh_pos[1] < 0) | (neigh_pos[1] > (life.size[1] - 1))):
                    break
                self.neigh_states.append(life.cells[neigh_pos[0]][neigh_pos[1]].get_state())

        # TODO: For now all squares outside of board are dead
        for i, item in enumerate(self.neigh_states):
            if (item == None):
                self.neigh_states[i] = DEAD
    
    def get_next_gen(self):
        alive_neigh = sum(self.neigh_states)
        if (self.state == ALIVE):
            # Survive
            if ((alive_neigh == 2) | (alive_neigh == 3)):
                self.next_state = ALIVE
                return
            else:
                # Under/Over Populated
                self.next_state = DEAD
                return
        else:
            # Reproduce
            if (alive_neigh == 3):
                self.next_state = ALIVE
                return

    def update(self):
        self.state = self.next_state

def main():

    init_seed = [[ALIVE, ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, DEAD, DEAD]]
    
    life = Life([10, 10], 100, init_seed)

if __name__ == "__main__":
    main()