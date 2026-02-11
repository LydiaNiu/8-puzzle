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
    def __init__(self, parent, state, g_cost, h_cost):
        self.parent = parent # Parent TreeNode
        self.state = state  # Puzzle configuration (2D list)
        self.g = g_cost # Depth cost (g(n))
        self.h = h_cost # Heuristic cost (h(n))

    # This function compute priority value f(n) = g(n) + h(n) for A* search algorithms.
    def f(self):
        return self.g + self.h

    # less than operator is used by heapq to maintain the priority queue order.
    def __lt__(self, other):
        return self.f() < other.f()


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

    # Create initial node / MAKE_NODE in the pseudocode
    start_node = TreeNode(None, initial_state, 0, 0) # The root of the tree, no parents, g and f both =0
    print("\nInitial State:", start_node.state)
    
    # Push node into heap-based priority queue / MODE_QUEUE in the pseudocode
    # The heapq = frontier control 
    heapq.heappush(pq, start_node)

    # Main loop 
    while pq:
        # Pop thenode with smallest priority value
        current_node = heapq.heappop(pq)
        
        # Goal test: check if the current node's state is the goal state, if so, return the node
        if is_goal(goal, current_node.state):
            print("Goal state reached!")
            return current_node
        else:
            # expansion
            
            # 1. find the children of the current node by calling the expand function
            children = expand(current_node)
            
            # 2. calculate the f(n) values for each child node
            # update their g and h values accordingly
            child.g = current_node.g + 1 # increase 1 in every expansion
            # question: 
            for child in children:
                if heuristic_function is not None:
                    child.h = heuristic_function(child.state)
                else:
                    child.h = 0 # for uniform cost search, h(n) = 0
                child.f = child.g + child.h # calculate f(n) for each child node
            
            # sort the children based on their f(n) values before pushing them into the priority queue
            children.sort(key=lambda x: x.f())  
            # append the expanded children of the current node into the priority queue
            for child in children:
                heapq.heappush(pq, child) # the heappush function will rearrange the list with priority
        pass


# 3 Algorithms

def uniform_cost_search(initial_state):
    print("Running Uniform Cost Search...")
    general_search(initial_state, heuristic_function=None)


def a_star_misplaced_tile(initial_state):
    print("Running A* with Misplaced Tile Heuristic...")
    general_search(initial_state, heuristic_function=misplaced_tile_heuristic)


def a_star_manhattan_distance(initial_state):
    print("Running A* with Manhattan Distance Heuristic...")
    general_search(initial_state, heuristic_function=manhattan_distance_heuristic)



#done
def is_goal(goal, current):
    # This function checks whether the given state matches the goal configuration.
    #use a for loop to compare each element of the current state with goal state.
    for i in range(9):
        if current[i] != goal[i]:
            return False
    return True


# def to_tuple(node):
#     # Convert a node into a tuple for hashing.
#     return tuple(node.f(node), node.state)


# Heuristic Functions
'''
following are the heuristic functions for the A* search algorithms. 

The first one counts the number of misplaced tiles. 
The second one calculates the sum of Manhattan distances of the tiles from their goal positions.

Both functions ignore the blank tile (0) when calculating their respective heuristics.
Both functions return the heuristic value, which is used in the A* search to estimate the cost to reach the goal state from the current state.
'''

#done
def misplaced_tile_heuristic(state):
    # Counts the number of misplaced tiles (excluding blank).
    misplace_tile = 0
    for i in range(len(state)): # only check the first 8 tiles, ignore the blank tile (0) from the goal state
        if state[i] != goal[i]:
            misplace_tile += 1
    return misplace_tile

#done
def find_man_dist(tile_value, current_pos, distance):
    # Helper function to calculate Manhattan distance for one single tile.
    # Calculate the row and column of the current position and goal position.
    goal_pos = tile_value - 1  # since tile values are 1-8, their goal positions are 0-7
    current_row, current_col = divmod(current_pos, 3)
    goal_row, goal_col = divmod(goal_pos, 3)
    
    # Calculate Manhattan distance for this tile
    # The formula is from the youtube video, "Manhattan | Algorithm | Simple Python Tutorial"
    return abs(current_row - goal_row) + abs(current_col - goal_col) 

#done
def manhattan_distance_heuristic(state):
    # Computes the sum of Manhattan distances of tiles from their goal positions.
    distance = 0
    for i in range(len(state)):
        if state[i] == 0: # ignore the blank tile (0)
            continue
        else:
            # get the position of the tile in the current state and goal state
            tile_value = state[i]
            distance += find_man_dist(tile_value, i, distance)
    return distance




# Utility Functions (Operators)

# TODO
def get_blank_position(state):
    return state.index('0') # find the index of the blank tile (0) in the current state

# TODO
def swap_tiles(state, pos1, pos2):
    """
    Swap two positions in the puzzle and return a new state.
    Uses deepcopy to preserve original state.
    """
    new_state = copy.deepcopy(state)
    pass
    return new_state

# Expansion
# TODO
def expand(node):
    """
    Generate all valid child nodes from the given node.
    Uses deepcopy to avoid modifying parent state.
    """
    children = []

    # Example usage of deepcopy (no real move logic)
    new_state = copy.deepcopy(node.state)

    # Placeholder for move generation
    pass

    return children

# TODO
def reconstruct_path(goal_node):
    """
    Reconstruct solution path from goal node to root.
    """
    pass

#done
def print_current_state(state):
    print("\nCurrent State:")
    for i in range(3):
        print(state[i*3:(i+1)*3])
    pass



# Global goal state for the 8-puzzle
goal = [1,2,3,4,5,6,7,8,0]

def main():
    puzzle_choice = input("Welcome to the 8-Puzzle Solver! \nPress 1 for provided puzzle, or 2 to enter your own: ")
    initial_state = []
    
    if puzzle_choice == '1':
        print("\nPlease select the difficulty level:")
        print("1. Easy\n2. Medium\n3. Hard")
        difficulty_choice = input("Enter choice (1/2/3): ")
        
        if difficulty_choice == '1':
            initial_state = [1,2,3,4,5,6,0,7,8]
        elif difficulty_choice == '2':
            initial_state = [1,2,3,0,4,5,7,6,8]
        elif difficulty_choice == '3':
            initial_state = [0,1,2,5,3,6,4,7,8]
            
    elif puzzle_choice == '2':
        print("\nEnter your puzzle, using 0 for the blank tile.")
        # user input 8 numbers in a single line, separated by comma
        initial_state = list(map(int, input("Enter the puzzle state (e.g., 1,2,3,4,5,6,7,8,0): ").split(',')))
            
    print_current_state(initial_state)
    
    alg_choice = input("\nSelect algorithm:\n1. Uniform Cost Search\n2. A* with Misplaced Tile Heuristic\n3. A* with Manhattan Distance Heuristic\nEnter choice (1/2/3): ")
    
    if alg_choice == '1':
        uniform_cost_search(initial_state)
    elif alg_choice == '2':
        a_star_misplaced_tile(initial_state)
    elif alg_choice == '3':        
        a_star_manhattan_distance(initial_state)
    
    # TODO: After the search is complete, reconstruct the path from the goal node 
    # to the root node and print the statistics (number of nodes expanded, depth of solution).
    pass


if __name__ == "__main__":
    main()

