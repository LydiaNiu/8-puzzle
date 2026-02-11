
goal = [1,2,3,4,5,6,7,8,0]
initial_state = [1,2,3,4,5,6,0,7,8]
print(initial_state)



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def find_man_dist(tile_value, current_pos, distance):
    # Helper function to calculate Manhattan distance for a single tile.
    # Calculate the row and column of the current position and goal position.
    goal_pos = tile_value - 1  # since tile values are 1-8, their goal positions are 0-7
    current_row, current_col = divmod(current_pos, 3)
    goal_row, goal_col = divmod(goal_pos, 3)
    
    # Calculate Manhattan distance for this tile
    return abs(current_row - goal_row) + abs(current_col - goal_col)



def manhattan_distance_heuristic(state):
    # Computes the sum of Manhattan distances of tiles from their goal positions.
    distance = 0
    for i in range(len(state)):
        if state[i] == 0: # ignore the blank tile (0)
            continue
        else:
            # get the position of the tile in the current state and goal state
            tile_value = state[i]
            print(tile_value)
            distance += find_man_dist(tile_value, i, distance)
            print(distance)
    return distance
    
def misplaced_tile_heuristic(state):
    # Counts the number of misplaced tiles (excluding blank).
    misplace_tile = 0
    for i in range(len(state)): # only check the first 8 tiles, ignore the blank tile (0) from the goal state
        if state[i] != goal[i]:
            misplace_tile += 1
    return misplace_tile




# h_n = manhattan_distance_heuristic(initial_state)
h_n = misplaced_tile_heuristic(initial_state)

print("final:", h_n)
