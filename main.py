"""
8-Puzzle Solver – Skeleton Structure
Algorithms:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with Manhattan Distance Heuristic

"""

import heapq # for priority queue (frontier)
import copy # for deepcopy of puzzle states

# The class TreeNode = tree strucutre for the search algorithms.
# Each object represents a node/state in the search tree.
# The nature of the node can store puzzle state, cost values, and parent pointer.
class TreeNode:

    # This function create new search node and store the g&h cost values
    def __init__(self, parent, state, g_cost, h_cost, f_cost):
        self.parent = parent # Parent TreeNode
        self.state = state  # Puzzle configuration (2D list)
        self.g = g_cost # Depth cost (g(n))
        self.h = h_cost # Heuristic cost (h(n))
        self.f = f_cost # Total cost (f(n) = g(n) + h(n))

    # less than operator is used by heapq to maintain the priority queue order.
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h )


def general_search(initial_state, heuristic_function):
    """
    This function serves as a general search framework used by all algorithms.
    
    the heuristic_function determines the algorithm's behavior.
    the parameter is a function, which is called when re-calculate the h(n) for the children nodes
    Note: Uniform cost search has no heuristic function, the paramenter passses in 'None', h(n) = 0
    """
    
    # The following codes are from the pseudocode of general search provided in project description
    
    # Priority queue (frontier)
    pq = []
    visited = set() # to keep track of visited states, avoid cycles and redundant expansions

    # Create initial node / MAKE_NODE in the pseudocode
    start_node = TreeNode(None, initial_state, 0, 0,0) # The root of the tree, no parents, g and f both =0
    
    # Push node into heap-based priority queue / MODE_QUEUE in the pseudocode
    # The heapq = frontier control 
    heapq.heappush(pq, start_node)

    # Main loop 
    while pq:
        # Pop thenode with smallest priority value
        current_node = heapq.heappop(pq)
        visited.add(tuple(current_node.state)) # add the current node's state to the visited set
        # might need to make it as str
        
        # Goal test: check if the current node's state is the goal state, if so, return the node
        if is_goal(goal, current_node.state):
            print("\nGoal state reached!\n\n")
            print("Solution found at depth:", current_node.g)
            print("Number of nodes expanded:", len(visited)) # nodes expanded: len(visited)
            print("Max queue size:", len(pq) + len(visited)) # max queue : len(heap) + len(visited)
            return current_node
        else:
            # expansion
            
            # 1. find the children of the current node by calling the expand function
            children = []
            copy_node = copy.deepcopy(current_node)
            blank_pos = get_blank_position(copy_node.state) # get the position of the blank tile = 0 in the current state
            
            # 2. check the 4 conditions of the 4 operators (up, down, left, right)
            # -> swap tile if the condition meets
            # -> check if the state after swap is already visited before 
            # -> if visited, skip
            # -> if not visited, create a new child node with the new state after operation, and add it to the children list
            if blank_pos + 3 < 9: # move down
                temp_state = swap_tiles(copy_node.state, blank_pos, blank_pos + 3)        
                if tuple(temp_state) not in visited:
                    child1 = TreeNode(parent = copy_node, state = swap_tiles(copy_node.state, blank_pos, blank_pos + 3), g_cost = copy_node.g + 1, 
                                      h_cost = heuristic_function(temp_state) if heuristic_function is not None else 0, 
                                      f_cost = copy_node.g + 1 + heuristic_function(temp_state) if heuristic_function is not None else 0) # g(n) increases by 1 for each expansion, h(n) will be calculated later
                    children.append(child1)
            
            if blank_pos - 3 >= 0: # move up
                temp_state = swap_tiles(copy_node.state, blank_pos, blank_pos - 3)
                if tuple(temp_state) not in visited:
                    child2 = TreeNode(parent = copy_node, state = swap_tiles(copy_node.state, blank_pos, blank_pos - 3), g_cost = copy_node.g + 1, 
                                      h_cost = heuristic_function(temp_state) if heuristic_function is not None else 0,
                                      f_cost = copy_node.g + 1 + heuristic_function(temp_state) if heuristic_function is not None else 0)
                    children.append(child2)
            
            if blank_pos % 3 != 0: # move left
                temp_state = swap_tiles(copy_node.state, blank_pos, blank_pos - 1)
                if tuple(temp_state) not in visited:
                    child3 = TreeNode(parent = copy_node, state = swap_tiles(copy_node.state, blank_pos, blank_pos - 1), g_cost = copy_node.g + 1, 
                                      h_cost = heuristic_function(temp_state) if heuristic_function is not None else 0,
                                      f_cost = copy_node.g + 1 + heuristic_function(temp_state) if heuristic_function is not None else 0)
                    children.append(child3)
            
            if blank_pos % 3 != 2: # move right
                temp_state = swap_tiles(copy_node.state, blank_pos, blank_pos + 1)
                if tuple(temp_state) not in visited:
                    child4 = TreeNode(parent = copy_node, state = swap_tiles(copy_node.state, blank_pos, blank_pos + 1), g_cost = copy_node.g + 1, 
                                      h_cost = heuristic_function(temp_state) if heuristic_function is not None else 0,
                                      f_cost = copy_node.g + 1 + heuristic_function(temp_state) if heuristic_function is not None else 0)
                    children.append(child4)

            # 3. append the expanded children of the current node into the priority queue
            for child in children:
                heapq.heappush(pq, child) # the heappush function will rearrange the list with priority
            
            best_child = pq[0] # the child with the smallest f(n) value is at the front of the priority queue
            print("\nThe best state to expand with a g(n) = ", best_child.g, " and h(n) = ", best_child.h, " is... \n")
            print_current_state(best_child.state)

def is_goal(goal, current):
    # This function checks whether the given state matches the goal configuration.
    #use a for loop to compare each element of the current state with goal state.
    for i in range(9):
        if current[i] != goal[i]:
            return False
    return True


# Heuristic Functions
'''
Following are the 2 different heuristic functions for the A* search algorithms. 

1. Misplaced tiles simply counts the number of tiles that are not in their goal positions. 
2. Manhattan distance calculates the sum of Manhattan distances of the tiles from their goal positions.

Both functions ignore the blank tile (0) when calculating their respective heuristics.
Both functions return the heuristic value, which is used in the A* search to estimate the cost 
to reach the goal state from the current state.
Functions are being taken in as the paramter of the general_search function
Functions are used when creating the child nodes in the exapansion step to calculate the h(n)
'''


def misplaced_tile_heuristic(state):
    # Counts the number of misplaced tiles (excluding blank).
    misplace_tile = 0
    # a for loop to compare each tile in the current state with the corresponding tile in the goal state
    for i in range(len(state)): 
        if state[i] != goal[i]:
            misplace_tile += 1
    return misplace_tile

def find_man_dist(tile_value, current_pos):
    # helper function to calculate Manhattan distance for one single tile.
    # calculate the row and column of the current position and goal position.
    goal_pos = tile_value - 1  # since tile values are 1-8, their goal positions are 0-7
    current_row, current_col = divmod(current_pos, 3)
    goal_row, goal_col = divmod(goal_pos, 3)
    
    # Calculate Manhattan distance for this tile
    # The formula is from the youtube video, "Manhattan | Algorithm | Simple Python Tutorial"
    return abs(current_row - goal_row) + abs(current_col - goal_col) 

def manhattan_distance_heuristic(state):
    # Computes the sum of Manhattan distances of tiles from their goal positions.
    distance = 0
    for i in range(len(state)):
        if state[i] == 0: # ignore the blank tile (0)
            continue
        else:
            # call the calcualting function: find_man_dist for each tile and sum up the total distance
            tile_value = state[i]
            distance += find_man_dist(tile_value, i)
    return distance




# Utility Functions (Operators)
def get_blank_position(state):
    return state.index(0) # find the index of the blank tile (0) in the current state

def swap_tiles(state, blank_pos, target_pos):
    # Swap two positions in the puzzle and return a new state. Uses deepcopy to preserve original state.
    new_state = copy.deepcopy(state)
    new_state[blank_pos], new_state[target_pos] = new_state[target_pos], new_state[blank_pos]
    return new_state

def print_current_state(state):
    for i in range(3):
        print(state[i*3:(i+1)*3])
    pass

# Solvability Check
'''
When testing user inputed puzzle, the program first check if the puzzle is solvable
If not, the program will print a message and exit.
Doing so, the function checks if the number of inversions is even or odd. 

For 3x3 puzzle, if the number of inversions is even, the puzzle is solvable; if odd, it is not solvable.
Inversion: the front tile is higher than back tile

ex: 
[1, 2, 3, 4, 5, 6, 8, 7] inversion = 1 (8 is higher than 7) -> non solvable
[2, 1, 3, 4, 5, 6, 8 ,7] inversion = 2 (2 is higher than 1, 8 is higher than 7) -> solvable
'''
def is_solvable(state):
    inversions = 0
    # Create a list without the blank tile to simplify logic
    # or simply skip '0' inside the loop
    for i in range(len(state)):
        if state[i] == 0: continue  # Skip the blank tile
        for j in range(i + 1, len(state)):
            if state[j] == 0: continue  # Skip the blank tile
            if state[i] > state[j]:
                inversions += 1

    # For 3x3 puzzle, solvable if inversions is even
    return inversions % 2 == 0


# Global goal state for the 8-puzzle
goal = [1,2,3,4,5,6,7,8,0]

def main():
    puzzle_choice = input("Welcome to the 8-Puzzle Solver! \n\nPress 1 for provided puzzle, or 2 to enter your own: ")
    initial_state = []
    
    if puzzle_choice == '1':
        print("\nPlease select the difficulty level ( 1 - 8 ):")
        difficulty_choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
        
        if difficulty_choice == '1':
            initial_state = [1,2,3,4,5,6,7,8,0]
        elif difficulty_choice == '2':
            initial_state = [1,2,3,4,5,6,0,7,8]
        elif difficulty_choice == '3':
            initial_state = [1,2,3,5,0,6,4,7,8]
        elif difficulty_choice == '4':
            initial_state = [1,3,6,5,0,2,4,7,8]
        elif difficulty_choice == '5':
            initial_state = [1,3,6,5,0,7,4,8,2]
        elif difficulty_choice == '6':
            initial_state = [1,6,7,5,0,3,4,8,2]
        elif difficulty_choice == '7':
            initial_state = [7,1,2,4,8,5,6,3,0]
        elif difficulty_choice == '8':
            initial_state = [0,7,2,4,6,1,3,5,8]
        print("\nCurrent State:")
        print_current_state(initial_state)
        
    elif puzzle_choice == '2':
        # user input 8 numbers in a single line, separated by comma
        initial_state = list(map(int, input("\nEnter your puzzle, using 0 for the blank tile and comma as split.\n\nExample: 1,5,6,2,3,4,7,8,0\n\n").split(',')))
        if not is_solvable(initial_state):
            print("\nThis input puzzle is not solvable, it cannot meet the goal state.")
            return

            
    print("\nGoal State:")
    for i in range(3):
        print(goal[i*3:(i+1)*3])
    
    alg_choice = input("\nSelect algorithm:\n\n1. Uniform Cost Search\n2. A* with Misplaced Tile Heuristic\n3. A* with Manhattan Distance Heuristic\n\nEnter choice (1/2/3): ")
    
    # 3 Algorithms
    if alg_choice == '1':
        general_search(initial_state, None)
    elif alg_choice == '2':
        general_search(initial_state, misplaced_tile_heuristic)
    elif alg_choice == '3':
        general_search(initial_state, manhattan_distance_heuristic)
    pass


if __name__ == "__main__":
    main()

