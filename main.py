"""
8-Puzzle Solver – Skeleton Structure
Algorithms:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with Manhattan Distance Heuristic

"""

import heapq          # for priority queue (frontier)
import copy           # for deepcopy of puzzle states


class TreeNode:
    """
    Represents a node in the search tree.
    Stores puzzle state, cost values, and parent pointer.
    """

    def __init__(self, parent, state, g_cost, h_cost):
        self.parent = parent      # Parent TreeNode
        self.state = state        # Puzzle configuration (2D list)
        self.g = g_cost           # Path cost so far
        self.h = h_cost           # Heuristic cost

    def f(self):
        """Total estimated cost f(n) = g(n) + h(n)"""
        return self.g + self.h

    def __lt__(self, other):
        """
        Required for heapq.
        Nodes are compared by f(n).
        """
        return self.f() < other.f()


def general_search(initial_state, heuristic_function):
    """
    General search framework used by all algorithms.
    heuristic_function determines the algorithm behavior.
    """

    # Priority queue (frontier)
    frontier = []

    # Create initial node
    start_node = TreeNode(None, initial_state, 0, 0)

    # Push node into heap-based priority queue
    heapq.heappush(frontier, start_node)

    # Main loop placeholder
    while frontier:
        # Pop node with smallest priority value
        current_node = heapq.heappop(frontier)

        # Goal test, expansion, and bookkeeping go here
        pass


# 3 Algorithms

def uniform_cost_search(initial_state):
    """
    Uniform Cost Search.
    Equivalent to A* with heuristic = 0.
    """
    general_search(initial_state, heuristic_function=None)


def a_star_misplaced_tile(initial_state):
    """
    A* Search using Misplaced Tile heuristic.
    """
    general_search(initial_state, heuristic_function=misplaced_tile_heuristic)


def a_star_manhattan_distance(initial_state):
    """
    A* Search using Manhattan Distance heuristic.
    """
    general_search(initial_state, heuristic_function=manhattan_distance_heuristic)


# Expansion and State Logic

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


def is_goal(state):
    """
    Check whether the given state matches the goal configuration.
    """
    pass


def board_to_tuple(state):
    """
    Convert a 2D puzzle state into a tuple for hashing.
    Used for visited-state tracking.
    """
    pass


# Heuristic Functions

def misplaced_tile_heuristic(state):
    """
    Counts the number of misplaced tiles (excluding blank).
    """
    
    pass


def manhattan_distance_heuristic(state):
    """
    Computes the sum of Manhattan distances of tiles
    from their goal positions.
    """
    
    pass



# Utility Functions


def get_blank_position(state):
    """
    Locate the position of the blank tile (0).
    """
    pass


def swap_tiles(state, pos1, pos2):
    """
    Swap two positions in the puzzle and return a new state.
    Uses deepcopy to preserve original state.
    """
    new_state = copy.deepcopy(state)
    pass
    return new_state


def reconstruct_path(goal_node):
    """
    Reconstruct solution path from goal node to root.
    """
    pass


def print_current_state(state):
    print("\nCurrent State:")
    for i in range(3):
        print(state[i*3:(i+1)*3])
    pass



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
        print("Enter your puzzle, using 0 for the blank tile.")
        for i in range(3):
            row = input(f"Row {i + 1}: ")
            initial_state.append(list(map(int, row.split())))
            
    print_current_state(initial_state)
    
    alg_choice = input("\nSelect algorithm:\n1. Uniform Cost Search\n2. A* with Misplaced Tile Heuristic\n3. A* with Manhattan Distance Heuristic\nEnter choice (1/2/3): ")
    
    if alg_choice == '1':
        algorithm = uniform_cost_search
    elif alg_choice == '2':
        algorithm = a_star_misplaced_tile
    elif alg_choice == '3':        
        algorithm = a_star_manhattan_distance
    
    pass


if __name__ == "__main__":
    main()

