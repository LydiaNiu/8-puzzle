import heapq # for priority queue (frontier)
import copy # for deepcopy of puzzle states

def get_blank_position(state):
    return state.index(0) # find the index of the blank tile (0) in the current state

def swap_tiles(state, blank_pos, target_pos):
# Swap two positions in the puzzle and return a new state. Uses deepcopy to preserve original state.
    new_state = copy.deepcopy(state)
    print("new state blank:", new_state[blank_pos], "target:", new_state[target_pos]) # print the values being swapped for debugging
    new_state[blank_pos], new_state[target_pos] = new_state[target_pos], new_state[blank_pos]
    return new_state

s1 = [1,2,3,4,5,6,0,7,8]
s2 = [1,2,3,0,4,5,7,6,8]
s3 = [0,1,2,5,3,6,4,7,8]

# testing the swap_tiles function
new_state = swap_tiles(s1, get_blank_position(s1), 2) # example usage of swap_tiles function
print(s1) # print the original state
print(new_state) # print the state after swapping
