# MazeLab — TODO

## FireAnt 🐜 — Experimental Colony-Based Maze Solver

**Status:** Concept / Not yet implemented

### Core Idea

FireAnt is a proposed maze-solving algorithm that uses multiple explorers to investigate different regions of a maze.

Unlike Dino and Caveman, which explore paths recursively from the starting position, FireAnt would distribute explorers throughout the maze and attempt to connect their discovered paths.

The ultimate objective is to establish a connected route between the start (`S`) and end (`E`) positions.

### Proposed Behavior

- Deploy multiple explorers at different locations throughout the maze, potentially using random starting positions.
- Allow each explorer to expand through accessible passages and discover nearby regions.
- Track the paths or regions discovered by individual explorers.
- Identify when separate explored regions intersect or connect.
- Combine connected paths to establish a route from `S` to `E`.
- Experiment with starting from a single explorer before implementing the full multi-explorer approach.

### Unresolved Design Questions

- How should explorer starting positions be selected?
- Should explorers expand randomly or follow a specific exploration rule?
- How should discovered regions and their connections be represented?
- How should FireAnt combine paths from different explorers?
- How can FireAnt determine whether the resulting path is shortest?
- How should FireAnt determine that a maze has no solution?
- How many explorers should be used, and how should that number depend on maze size?

### Future Testing

Compare FireAnt against Dino, Caveman, and other maze-solving algorithms using:

- Correctness and shortest-path length
- Ability to identify unsolvable mazes
- Number of explored positions
- Computational performance
- Behavior on different maze structures

---

## Caveman 🦴 — Correctness Investigation

**Status:** Known bug / Investigation pending

- [ ] Preserve the original Caveman implementation.
- [ ] Reproduce the 40-step versus 32-step discrepancy on Caveman's Kryptonite.
- [ ] Investigate why failed-position caching can produce incorrect results.
- [ ] Determine whether the issue is mathematical, implementation-related, or both.
- [ ] Develop and test a corrected version.
- [ ] Verify that the correction preserves Caveman's ability to efficiently reject `maze_006.txt`, the unsolvable maze.
- [ ] Compare the corrected algorithm against Dino.

**Important:** Investigate the correctness issue independently before consulting existing solutions or receiving algorithmic hints.