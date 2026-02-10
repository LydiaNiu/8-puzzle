# 8-Puzzle Solver

This program solves the eight puzzle using three different search algorithms:
1. **Uniform Cost Search** - Explores states in order of path cost
2. **A* with the Misplaced Tile heuristic** - Uses number of misplaced tiles as heuristic
3. **A* with the Manhattan Distance heuristic** - Uses sum of Manhattan distances as heuristic

## The 8-Puzzle Problem

The 8-puzzle consists of a 3x3 grid with 8 numbered tiles and one blank space. The goal is to rearrange the tiles from a given initial configuration to the goal configuration:

```
Goal State:
1 2 3
4 5 6
7 8 *
```

Where `*` represents the blank space.

## Features

- **Three search algorithms** with performance comparison
- **Interactive puzzle selection** with pre-configured examples
- **Custom puzzle input** option
- **Detailed solution path** showing each move
- **Performance metrics** including nodes expanded and maximum queue size

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Usage

### Running the Program

```bash
python puzzle.py
```

The program will prompt you to select a puzzle:
1. Easy (1 move to solve)
2. Medium (2 moves to solve)
3. Hard (3 moves to solve)
4. Very Hard (8 moves to solve)
5. Custom puzzle

### Example Output

```
Initial puzzle state:
1 3 6
5 * 2
4 7 8

Solving with different algorithms...

============================================================
Uniform Cost Search
============================================================
Solution found!
Solution depth: 8
Nodes expanded: 311
Max queue size: 199

...

============================================================
COMPARISON SUMMARY
============================================================
Algorithm                                Nodes      Queue     
------------------------------------------------------------
Uniform Cost Search                      311        199       
A* (Misplaced Tiles)                     19         16        
A* (Manhattan Distance)                  13         12
```

### Custom Puzzle Input

When selecting option 5, enter your puzzle configuration:
```
Enter the puzzle configuration (use 0 for blank):
Enter 3 rows of 3 numbers each, separated by spaces:
Row 1: 1 2 3
Row 2: 4 0 6
Row 3: 7 5 8
```

## Running Tests

The project includes comprehensive unit tests:

```bash
python -m unittest test_puzzle.py -v
```

## Algorithm Comparison

The program demonstrates the efficiency differences between search algorithms:

- **Uniform Cost Search**: Explores all states at the same depth before moving deeper. Guarantees optimal solution but may expand many nodes.

- **A* with Misplaced Tiles**: Uses the number of misplaced tiles as a heuristic. More efficient than UCS but less informed than Manhattan distance.

- **A* with Manhattan Distance**: Uses the sum of Manhattan distances of all tiles to their goal positions. Most efficient for the 8-puzzle problem while still guaranteeing optimal solutions.

## Implementation Details

### PuzzleState Class
- Represents a puzzle configuration
- Tracks parent state for solution reconstruction
- Generates successor states (valid moves)
- Implements equality and hashing for efficient state comparison

### Heuristics

**Misplaced Tiles**: Counts how many tiles are not in their goal position (excluding blank).

**Manhattan Distance**: For each tile, calculates the distance it needs to travel to reach its goal position (sum of horizontal and vertical distances).

### Search Algorithms

All three algorithms use a priority queue (heap) for efficient state selection:
- **UCS**: Priority = path cost (g)
- **A* with Misplaced**: Priority = g + h (misplaced tiles)
- **A* with Manhattan**: Priority = g + h (Manhattan distance)

## File Structure

```
.
├── puzzle.py          # Main program with solver implementation
├── test_puzzle.py     # Unit tests
└── README.md         # This file
```

## License

This is an educational project for demonstrating search algorithms.