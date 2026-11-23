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

**Concluded**
OG Caveman's memory pruning idea itself is the bug. The shortest path would be entirely possible by changing the movement behavior. I developed a corrected verision that keeps memory at cross-roads where there are two possible moves that can reduce manhattan distance by 1. It does correctly produce the intended result throughout my tests, however, the pruning is almost never used so for most mazes the new Caveman is basically just a glorified Dino. The other solution which is much more efficient was taken from my time solving `LeetCode 3341 — Find Minimum Time to Reach Last Room I`. There I kept a map that kept track of the earliest arrival to each room and then any room that I got to at a later or equal time was pruned. This algorithm was much more efficient than the new Caveman and was aptly named ChronoCaveman.

OG Caveman remains one of my most efficient recursive DFS approaches for determining reachability, but it cannot guarantee the shortest path.