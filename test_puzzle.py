"""
Unit tests for the 8-puzzle solver.
"""

import unittest
from puzzle import (
    PuzzleState,
    misplaced_tiles_heuristic,
    manhattan_distance_heuristic,
    uniform_cost_search,
    a_star_search,
    get_solution_path
)


class TestPuzzleState(unittest.TestCase):
    """Test cases for PuzzleState class."""
    
    def test_initial_state(self):
        """Test puzzle state initialization."""
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        state = PuzzleState(board)
        self.assertEqual(state.board, board)
        self.assertEqual(state.blank_pos, (2, 2))
        self.assertEqual(state.cost, 0)
    
    def test_is_goal(self):
        """Test goal state detection."""
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        non_goal_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        
        goal_state = PuzzleState(goal_board)
        non_goal_state = PuzzleState(non_goal_board)
        
        self.assertTrue(goal_state.is_goal())
        self.assertFalse(non_goal_state.is_goal())
    
    def test_get_successors(self):
        """Test successor generation."""
        # Middle position should have 4 successors
        board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        state = PuzzleState(board)
        successors = state.get_successors()
        self.assertEqual(len(successors), 4)
        
        # Corner position should have 2 successors
        corner_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        corner_state = PuzzleState(corner_board)
        corner_successors = corner_state.get_successors()
        self.assertEqual(len(corner_successors), 2)
    
    def test_equality(self):
        """Test state equality."""
        board1 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        board2 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        board3 = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        
        state1 = PuzzleState(board1)
        state2 = PuzzleState(board2)
        state3 = PuzzleState(board3)
        
        self.assertEqual(state1, state2)
        self.assertNotEqual(state1, state3)


class TestHeuristics(unittest.TestCase):
    """Test cases for heuristic functions."""
    
    def test_misplaced_tiles_goal(self):
        """Test misplaced tiles heuristic on goal state."""
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        state = PuzzleState(goal_board)
        self.assertEqual(misplaced_tiles_heuristic(state), 0)
    
    def test_misplaced_tiles_non_goal(self):
        """Test misplaced tiles heuristic on non-goal state."""
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        state = PuzzleState(board)
        # Only tile 8 is misplaced
        self.assertEqual(misplaced_tiles_heuristic(state), 1)
    
    def test_manhattan_distance_goal(self):
        """Test Manhattan distance heuristic on goal state."""
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        state = PuzzleState(goal_board)
        self.assertEqual(manhattan_distance_heuristic(state), 0)
    
    def test_manhattan_distance_non_goal(self):
        """Test Manhattan distance heuristic on non-goal state."""
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        state = PuzzleState(board)
        # Tile 8: should be at (2,1), is at (2,2) -> distance = 1
        self.assertEqual(manhattan_distance_heuristic(state), 1)
    
    def test_manhattan_distance_complex(self):
        """Test Manhattan distance on a more complex state."""
        board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        state = PuzzleState(board)
        # Tile 5: should be at (1,1), is at (2,1) -> distance = 1
        # Tile 8: should be at (2,1), is at (2,2) -> distance = 1
        # Total = 2
        self.assertEqual(manhattan_distance_heuristic(state), 2)


class TestSearchAlgorithms(unittest.TestCase):
    """Test cases for search algorithms."""
    
    def test_ucs_already_solved(self):
        """Test UCS on already solved puzzle."""
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        state = PuzzleState(goal_board)
        solution, nodes, queue_size = uniform_cost_search(state)
        
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_goal())
        self.assertEqual(solution.cost, 0)
    
    def test_ucs_one_move(self):
        """Test UCS on puzzle requiring one move."""
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        state = PuzzleState(board)
        solution, nodes, queue_size = uniform_cost_search(state)
        
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_goal())
        self.assertEqual(solution.cost, 1)
    
    def test_astar_misplaced_already_solved(self):
        """Test A* (misplaced) on already solved puzzle."""
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        state = PuzzleState(goal_board)
        solution, nodes, queue_size = a_star_search(state, misplaced_tiles_heuristic)
        
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_goal())
        self.assertEqual(solution.cost, 0)
    
    def test_astar_misplaced_one_move(self):
        """Test A* (misplaced) on puzzle requiring one move."""
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        state = PuzzleState(board)
        solution, nodes, queue_size = a_star_search(state, misplaced_tiles_heuristic)
        
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_goal())
        self.assertEqual(solution.cost, 1)
    
    def test_astar_manhattan_already_solved(self):
        """Test A* (Manhattan) on already solved puzzle."""
        goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        state = PuzzleState(goal_board)
        solution, nodes, queue_size = a_star_search(state, manhattan_distance_heuristic)
        
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_goal())
        self.assertEqual(solution.cost, 0)
    
    def test_astar_manhattan_one_move(self):
        """Test A* (Manhattan) on puzzle requiring one move."""
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        state = PuzzleState(board)
        solution, nodes, queue_size = a_star_search(state, manhattan_distance_heuristic)
        
        self.assertIsNotNone(solution)
        self.assertTrue(solution.is_goal())
        self.assertEqual(solution.cost, 1)
    
    def test_all_algorithms_same_solution_length(self):
        """Test that all algorithms find optimal solution."""
        board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        state = PuzzleState(board)
        
        ucs_solution, _, _ = uniform_cost_search(state)
        astar_misplaced_solution, _, _ = a_star_search(state, misplaced_tiles_heuristic)
        astar_manhattan_solution, _, _ = a_star_search(state, manhattan_distance_heuristic)
        
        # All should find optimal solution
        self.assertEqual(ucs_solution.cost, astar_misplaced_solution.cost)
        self.assertEqual(ucs_solution.cost, astar_manhattan_solution.cost)


class TestSolutionPath(unittest.TestCase):
    """Test cases for solution path reconstruction."""
    
    def test_get_solution_path(self):
        """Test solution path reconstruction."""
        board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        state = PuzzleState(board)
        solution, _, _ = uniform_cost_search(state)
        
        path = get_solution_path(solution)
        
        # Check path properties
        self.assertGreater(len(path), 0)
        self.assertEqual(path[0].board, board)  # First state is initial
        self.assertTrue(path[-1].is_goal())  # Last state is goal
        self.assertEqual(len(path), solution.cost + 1)
    
    def test_get_solution_path_none(self):
        """Test solution path with None input."""
        path = get_solution_path(None)
        self.assertEqual(path, [])


if __name__ == "__main__":
    unittest.main()
