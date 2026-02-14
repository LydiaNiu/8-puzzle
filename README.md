# 8-puzzle

## ✅ Project Conclusion (1 Paragraph)

This project implemented and compared three search algorithms—Uniform Cost Search, A* with the Misplaced Tile heuristic, and A* with the Manhattan Distance heuristic—to solve the 8-puzzle problem. Through empirical evaluation across varying solution depths, the results show that while all three algorithms guarantee optimal solutions, heuristic-based A* search significantly reduces the number of nodes expanded compared to Uniform Cost Search. Further analysis using the effective branching factor confirms that heuristics improve scalability by reducing the base of exponential growth in the search tree. Among the tested approaches, the Manhattan Distance heuristic consistently achieves the strongest pruning efficiency, demonstrating that more informative heuristics lead to substantially better performance while preserving optimality.

---

# ✅ Complete README File for GitHub

You can copy this directly into your `README.md`.

---

# 8-Puzzle Solver – Search Algorithm Comparison

This project implements and compares three classical search algorithms to solve the 8-puzzle problem:

* Uniform Cost Search (UCS)
* A* with Misplaced Tile heuristic
* A* with Manhattan Distance heuristic

The project analyzes algorithm performance in terms of:

* Solution depth
* Number of nodes expanded
* Effective branching factor

---

## 📌 Problem Description

The 8-puzzle is a sliding tile puzzle played on a 3×3 board containing 8 numbered tiles and one blank space. The objective is to transform a given initial configuration into a goal configuration by sliding tiles into the blank space.

Only half of all possible puzzle configurations are solvable. This implementation includes a solvability check before running any search algorithm.

---

## 🚀 Algorithms Implemented

### 1️⃣ Uniform Cost Search (UCS)

* Expands nodes based only on path cost ( g(n) )
* Guarantees optimality
* No heuristic guidance

### 2️⃣ A* with Misplaced Tile

* Uses the number of incorrectly positioned tiles as heuristic ( h(n) )
* Admissible heuristic
* More efficient than UCS

### 3️⃣ A* with Manhattan Distance

* Uses the sum of vertical and horizontal distances of each tile from its goal position
* More informative and admissible heuristic
* Most efficient among the three

---

## 📊 Performance Metrics

The project evaluates performance using:

* **Number of nodes expanded**
* **Solution depth**
* **Effective branching factor**

The effective branching factor is estimated using:

[
b \approx N^{1/d}
]

where:

* ( N ) = number of nodes expanded
* ( d ) = solution depth

This metric connects empirical results to theoretical time complexity ( O(b^d) ).

---

## 📈 Key Findings

* All three algorithms guarantee optimal solutions.
* A* significantly reduces node expansions compared to UCS.
* Manhattan Distance consistently outperforms Misplaced Tile.
* Even small reductions in effective branching factor produce exponential performance improvements at deeper levels.
