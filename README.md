# MAZESSS

A personal project focused on learning, implementing, and experimenting with maze-solving algorithms.

The goal is to traverse mazes, find the shortest path when one exists, and determine when a maze is unsolvable.

The project includes multiple maze-solving approaches, performance benchmarks, adversarial test mazes, and a Pygame visualization that lets you watch the algorithms explore in real time.

## Requirements

- Python 3
- Pygame (for visualization)

Install Pygame with:

```bash
python3 -m pip install pygame
```

## Maze Format

Mazes are represented using four characters:

| Character | Meaning |
|---|---|
| `#` | Wall |
| `.` | Open space |
| `S` | Starting position |
| `E` | Exit |

Movement is restricted to four directions: up, down, left, and right. Each move has a cost of one.

## Meet the Cavemen

| Algorithm | Description |
|---|---|
| **Chief Caveman** | Dijkstra's shortest-path algorithm using a priority queue. |
| **Oracle Caveman** | A* search using Manhattan distance, with experiments in priority-queue tie-breaking. |
| **Diagonal Oracle Caveman** | A* using Manhattan distance, with tie-breaking that favors positions closer to the straight line connecting S and E. |
| **ChronoCaveman** | Recursive depth-first search that remembers the earliest arrival time at each coordinate to avoid unnecessary exploration. |
| **Dino** | Brute-force recursive depth-first exploration. It can find shortest paths, but becomes extremely inefficient on mazes with many possible routes. (It sucks.) |
| **OG Caveman** | An aggressive depth-first algorithm that caches failed positions. It can find valid routes but is not guaranteed to find the shortest one. |
| **Caveman** | An experimental version using familial memory and failure pruning. In many tested mazes, its memory optimization provided little benefit, making it effectively a fancier Dino. |

The names are purely for fun.

## Experiments and Benchmarks

The algorithms include performance measurements such as execution time, iterations or recursive calls, and algorithm-specific metrics.

I've experimented with different exploration strategies, especially how Dijkstra's algorithm and A* prioritize candidates.

Some mazes are intentionally designed to expose weaknesses in particular algorithms.

For example:

- **Maze 004:** Demonstrates OG Caveman's shortest-path correctness issue.
- **Maze 016:** Demonstrates the dramatic performance improvements possible with A* and different tie-breaking strategies.
- **Maze 023:** An adversarial maze designed to make Manhattan-distance A* explore almost every reachable room.

## Visualization — Caveman Cinema

The project includes a Pygame visualizer that displays maze exploration as it happens.

Instead of seeing only the final result, you can watch the algorithms select rooms, explore the maze, and leave behind a visual record of their search.

## Running the Project

Run the maze benchmarks:

```bash
python3 mazes.py
```

Launch the visualization:

```bash
python3 visualization.py
```

## Development Log

See [development_log.md](development_log.md) for the history of the project, including failed experiments, algorithm changes, performance comparisons, and the evolution of the Cavemen.