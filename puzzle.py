"""
8-Puzzle Solver using different search algorithms.

This program solves the eight puzzle using:
1) Uniform Cost Search
2) A* with the Misplaced Tile heuristic
3) A* with the Manhattan Distance heuristic
"""

import heapq
from typing import List, Tuple, Optional, Set


class PuzzleState:
    """Represents a state of the 8-puzzle."""
    
    def __init__(self, board: List[List[int]], parent=None, move: str = "", cost: int = 0):
        """
        Initialize a puzzle state.
        
        Args:
            board: 3x3 list representing the puzzle (0 represents empty space)
            parent: Parent state
            move: Move that led to this state
            cost: Cost to reach this state (depth)
        """
        self.board = [row[:] for row in board]  # Deep copy
        self.parent = parent
        self.move = move
        self.cost = cost
        self.blank_pos = self._find_blank()
        
    def _find_blank(self) -> Tuple[int, int]:
        """Find the position of the blank (0) tile."""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (0, 0)
    
    def is_goal(self) -> bool:
        """Check if this state is the goal state."""
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal
    
    def get_successors(self) -> List['PuzzleState']:
        """Generate all possible successor states."""
        successors = []
        row, col = self.blank_pos
        
        # Possible moves: Up, Down, Left, Right
        moves = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]
        
        for dr, dc, move_name in moves:
            new_row, new_col = row + dr, col + dc
            
            # Check if move is valid
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Create new board with swapped tiles
                new_board = [row[:] for row in self.board]
                new_board[row][col], new_board[new_row][new_col] = \
                    new_board[new_row][new_col], new_board[row][col]
                
                successors.append(
                    PuzzleState(new_board, self, move_name, self.cost + 1)
                )
        
        return successors
    
    def to_tuple(self) -> Tuple:
        """Convert board to tuple for hashing."""
        return tuple(tuple(row) for row in self.board)
    
    def __eq__(self, other):
        """Check equality based on board configuration."""
        if not isinstance(other, PuzzleState):
            return False
        return self.board == other.board
    
    def __hash__(self):
        """Hash based on board configuration."""
        return hash(self.to_tuple())
    
    def __str__(self):
        """String representation of the puzzle."""
        result = []
        for row in self.board:
            result.append(" ".join(str(x) if x != 0 else "*" for x in row))
        return "\n".join(result)


def misplaced_tiles_heuristic(state: PuzzleState) -> int:
    """
    Calculate the number of misplaced tiles (excluding blank).
    
    Args:
        state: Current puzzle state
        
    Returns:
        Number of misplaced tiles
    """
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    misplaced = 0
    
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0 and state.board[i][j] != goal[i][j]:
                misplaced += 1
    
    return misplaced


def manhattan_distance_heuristic(state: PuzzleState) -> int:
    """
    Calculate the Manhattan distance for all tiles.
    
    Args:
        state: Current puzzle state
        
    Returns:
        Sum of Manhattan distances for all tiles
    """
    distance = 0
    
    for i in range(3):
        for j in range(3):
            tile = state.board[i][j]
            if tile != 0:
                # Calculate goal position for this tile
                goal_row = (tile - 1) // 3
                goal_col = (tile - 1) % 3
                
                # Add Manhattan distance
                distance += abs(i - goal_row) + abs(j - goal_col)
    
    return distance


def uniform_cost_search(initial_state: PuzzleState) -> Tuple[Optional[PuzzleState], int, int]:
    """
    Solve the puzzle using Uniform Cost Search.
    
    Args:
        initial_state: Starting state of the puzzle
        
    Returns:
        Tuple of (solution_state, nodes_expanded, max_queue_size)
    """
    if initial_state.is_goal():
        return (initial_state, 0, 1)
    
    # Priority queue: (cost, counter, state)
    counter = 0
    frontier = [(0, counter, initial_state)]
    explored: Set[Tuple] = set()
    nodes_expanded = 0
    max_queue_size = 1
    
    while frontier:
        max_queue_size = max(max_queue_size, len(frontier))
        
        _, _, current_state = heapq.heappop(frontier)
        
        if current_state.to_tuple() in explored:
            continue
        
        explored.add(current_state.to_tuple())
        nodes_expanded += 1
        
        if current_state.is_goal():
            return (current_state, nodes_expanded, max_queue_size)
        
        for successor in current_state.get_successors():
            if successor.to_tuple() not in explored:
                counter += 1
                heapq.heappush(frontier, (successor.cost, counter, successor))
    
    return (None, nodes_expanded, max_queue_size)


def a_star_search(initial_state: PuzzleState, heuristic) -> Tuple[Optional[PuzzleState], int, int]:
    """
    Solve the puzzle using A* search with a given heuristic.
    
    Args:
        initial_state: Starting state of the puzzle
        heuristic: Heuristic function to use
        
    Returns:
        Tuple of (solution_state, nodes_expanded, max_queue_size)
    """
    if initial_state.is_goal():
        return (initial_state, 0, 1)
    
    # Priority queue: (f_cost, counter, state)
    counter = 0
    h_cost = heuristic(initial_state)
    frontier = [(h_cost, counter, initial_state)]
    explored: Set[Tuple] = set()
    nodes_expanded = 0
    max_queue_size = 1
    
    while frontier:
        max_queue_size = max(max_queue_size, len(frontier))
        
        _, _, current_state = heapq.heappop(frontier)
        
        if current_state.to_tuple() in explored:
            continue
        
        explored.add(current_state.to_tuple())
        nodes_expanded += 1
        
        if current_state.is_goal():
            return (current_state, nodes_expanded, max_queue_size)
        
        for successor in current_state.get_successors():
            if successor.to_tuple() not in explored:
                counter += 1
                g_cost = successor.cost
                h_cost = heuristic(successor)
                f_cost = g_cost + h_cost
                heapq.heappush(frontier, (f_cost, counter, successor))
    
    return (None, nodes_expanded, max_queue_size)


def get_solution_path(state: Optional[PuzzleState]) -> List[PuzzleState]:
    """
    Reconstruct the solution path from initial to goal state.
    
    Args:
        state: Goal state (with parent links)
        
    Returns:
        List of states from initial to goal
    """
    if state is None:
        return []
    
    path = []
    current = state
    while current is not None:
        path.append(current)
        current = current.parent
    
    return list(reversed(path))


def print_solution(algorithm_name: str, result: Tuple[Optional[PuzzleState], int, int]):
    """
    Print the solution details.
    
    Args:
        algorithm_name: Name of the algorithm used
        result: Tuple of (solution_state, nodes_expanded, max_queue_size)
    """
    solution_state, nodes_expanded, max_queue_size = result
    
    print(f"\n{'=' * 60}")
    print(f"{algorithm_name}")
    print(f"{'=' * 60}")
    
    if solution_state is None:
        print("No solution found!")
        return
    
    path = get_solution_path(solution_state)
    
    print(f"Solution found!")
    print(f"Solution depth: {solution_state.cost}")
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Max queue size: {max_queue_size}")
    print(f"\nSolution path ({len(path)} states):")
    
    for i, state in enumerate(path):
        if i == 0:
            print(f"\nInitial state:")
        else:
            print(f"\nMove {i}: {state.move}")
        print(state)


def main():
    """Main function to demonstrate the puzzle solver."""
    # Example puzzle configurations
    
    # Easy puzzle (few moves to solve)
    easy_puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]
    
    # Medium puzzle
    medium_puzzle = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    # Harder puzzle
    hard_puzzle = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]
    
    # Very hard puzzle
    very_hard_puzzle = [
        [1, 3, 6],
        [5, 0, 2],
        [4, 7, 8]
    ]
    
    # Select puzzle to solve
    print("Select a puzzle to solve:")
    print("1. Easy (1 move)")
    print("2. Medium (2 moves)")
    print("3. Hard (3 moves)")
    print("4. Very Hard (9 moves)")
    print("5. Custom puzzle")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        initial_board = easy_puzzle
    elif choice == "2":
        initial_board = medium_puzzle
    elif choice == "3":
        initial_board = hard_puzzle
    elif choice == "4":
        initial_board = very_hard_puzzle
    elif choice == "5":
        print("\nEnter the puzzle configuration (use 0 for blank):")
        print("Enter 3 rows of 3 numbers each, separated by spaces:")
        initial_board = []
        for i in range(3):
            row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
            initial_board.append(row)
    else:
        print("Invalid choice. Using easy puzzle.")
        initial_board = easy_puzzle
    
    initial_state = PuzzleState(initial_board)
    
    print("\nInitial puzzle state:")
    print(initial_state)
    
    # Solve with all three algorithms
    print("\n\nSolving with different algorithms...\n")
    
    # 1. Uniform Cost Search
    ucs_result = uniform_cost_search(initial_state)
    print_solution("Uniform Cost Search", ucs_result)
    
    # 2. A* with Misplaced Tiles heuristic
    astar_misplaced_result = a_star_search(initial_state, misplaced_tiles_heuristic)
    print_solution("A* with Misplaced Tile Heuristic", astar_misplaced_result)
    
    # 3. A* with Manhattan Distance heuristic
    astar_manhattan_result = a_star_search(initial_state, manhattan_distance_heuristic)
    print_solution("A* with Manhattan Distance Heuristic", astar_manhattan_result)
    
    # Comparison
    print(f"\n{'=' * 60}")
    print("COMPARISON SUMMARY")
    print(f"{'=' * 60}")
    print(f"{'Algorithm':<40} {'Nodes':<10} {'Queue':<10}")
    print(f"{'-' * 60}")
    print(f"{'Uniform Cost Search':<40} {ucs_result[1]:<10} {ucs_result[2]:<10}")
    print(f"{'A* (Misplaced Tiles)':<40} {astar_misplaced_result[1]:<10} {astar_misplaced_result[2]:<10}")
    print(f"{'A* (Manhattan Distance)':<40} {astar_manhattan_result[1]:<10} {astar_manhattan_result[2]:<10}")


if __name__ == "__main__":
    main()
