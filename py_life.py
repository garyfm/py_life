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

    def __init__(self, size, end_tick, seed):
        print(GREEN + "Created Life Universe" + ENDC)
        self.size = size
        self.end_tick = end_tick
        self.seed = seed
        self.current_tick = 0

    def get_size(self):
        return self.size
        
    def get_end_tick(self):
        return self.ticks

    def inc_ticks(self):
        self.current_tick += 1

    def get_tick(self):
        return self.current_tick        

class Cell:
    'Cell Class'
    current_state = None
    next_state = None 
    neighbours_states = []

    def __init__(self, current_state, next_state, neighbours_states):
       print(RED + "Created Cell" + ENDC)
       self.current_state = current_state 
       self.next_state = next_state
       self.neighbours_states = neighbours_states  

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
    life = Life([5,5], 100, 0)
    

if __name__ == "__main__":
    main()