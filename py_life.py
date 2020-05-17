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
CELL_SIZE = 20
DISPLAY_X = 400
DISPLAY_Y = 400

class Life:
    'Life Universe Class'
    seed = []
    size = [0, 0]
    end_tick = 0
    current_tick = 0
    cells = []
    num_cells = 0
    board = None 
    
    def __init__(self, size, end_tick, seed, display):
        self.size = size
        self.end_tick = end_tick
        self.seed = seed
        self.current_tick = 0
        self.board = display 
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
            self.cells[y][x + row].set_state(self.seed[0][row])
            for col in range(cols):
                cell = self.cells[y + col][x + row]
                cell.set_state(self.seed[row][col])

                if cell.state == ALIVE:
                    self.board.draw_cell(x + row, y + col, ALIVE)
                    self.board.update_display()

    def run_life(self):
        print(GREEN + "Running Life" + ENDC)

        for tick in range(self.end_tick):
            print(GREEN + "GEN: " + str(tick) + ENDC)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(RED + str(event) + ENDC)
                    quit()
     
            for row, row_cells in enumerate(self.cells):
                for col, cell in enumerate(row_cells):
                    cell.probe_neighbours(self, row, col)
                    cell.get_next_gen()

            for row, row_cells in enumerate(self.cells):
                for col, cell in enumerate(row_cells):
                    cell.update()
                    self.board.draw_cell(row,col, cell.get_state())

            self.board.update_display()
            time.sleep(1)

    def print_console(self): # for easier debug
        for print_row in self.cells:
            for cell in print_row:
                print("[" +str(cell.get_state()) + "],", end = '')
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

    
class Cell:
    'Cell Class'
    state = DEAD
    next_state = DEAD 
    neigh_states = [] 

    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    
    def probe_neighbours(self, life, row, col):
        
        # Loop over each possible transform to get each neightbouring cell
        self.neigh_states.clear()
        for row_trans in [1, 0, -1]:
            for col_trans in [1, 0, -1]:
                neigh_pos = [row + row_trans, col + col_trans]
                
                # Dont count the current cell as a neighbour
                if (row_trans == 0) and (col_trans == 0):
                    continue
                # Check if neighbouring cell is out of bounds
                if ((neigh_pos[0] < 0) | (neigh_pos[0] >= (life.size[0]))):
                    continue
                if ((neigh_pos[1] < 0) | (neigh_pos[1] >= (life.size[1]))):
                    continue

                neigh_state = life.cells[neigh_pos[0]][neigh_pos[1]].get_state() 
                self.neigh_states.append(neigh_state)
                
    def get_next_gen(self):
        #debug
        live_cell = 0
        if self.state == ALIVE:
            live_cell+=1

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


class Display:
    'Board display Class'
    board = None
    x_size = 0
    y_size = 0
    cell_size = 0
    x_num_cells = 0
    y_num_cells = 0

    def __init__(self, x_size, y_size, cell_size):
        self.x_size = x_size
        self.y_size = y_size
        self.cell_size = cell_size 
        self.x_num_cells = self.x_size // self.cell_size
        self.y_num_cells = self.y_size // self.cell_size
        self.board = self.init_display()
        self.draw_grid()

    def init_display(self):
            pygame.init()
            screen = pygame.display.set_mode((self.x_size , self.y_size)) 
            clock = pygame.time.Clock()
            pygame.display.set_caption('PYLIFE')
            clock.tick(60)
            return screen
    def update_display(self):
        pygame.display.flip()

    def draw_grid(self):
        for x in range(self.x_num_cells):
            for y in range(self.y_num_cells):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE) 
                pygame.draw.rect(self.board, WHITE, rect, 1)
                self.update_display()

    def draw_cell(self, x, y, state):
        if state == ALIVE:
            colour = WHITE
            sub = 0
        else:
            colour = BLACK
            # Subtract one from cell size to preserve the grid
            sub = 1

        rect = pygame.Rect(x * 20, y * 20, CELL_SIZE - sub, CELL_SIZE - sub) 
        pygame.draw.rect(self.board, colour, rect, 0)

def main():
    # Blinker 
    seed_1 = [[ALIVE, ALIVE, ALIVE], [DEAD, DEAD, DEAD]]
    # Toad
    seed_2 = [[DEAD, ALIVE, ALIVE, ALIVE], [ALIVE, ALIVE, ALIVE, DEAD]]
    # Beacon
    seed_3 = [[ALIVE, ALIVE, DEAD, DEAD], [ALIVE, ALIVE, DEAD, DEAD], [DEAD, DEAD, ALIVE, ALIVE], [DEAD, DEAD, ALIVE, ALIVE]]
    # R-pentomino
    seed_4 = [[DEAD, ALIVE, ALIVE], [ALIVE, ALIVE, DEAD], [DEAD, ALIVE, DEAD]] 
    # Glider
    seed_5 = [[DEAD, ALIVE, DEAD], [DEAD, DEAD, ALIVE], [ALIVE, ALIVE, ALIVE]] 

    display = Display(DISPLAY_X, DISPLAY_Y, CELL_SIZE)
    life = Life([20, 20], 100, seed_5, display)

if __name__ == "__main__":
    main()