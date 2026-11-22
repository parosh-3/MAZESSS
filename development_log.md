# Development Log

## November 21, 2026 — Dino and Caveman

### Dino — Original Maze Solver

Dino is the original recursive maze-solving algorithm. It explores possible paths through a maze, avoiding positions already visited within the current path to prevent cycles.

When Dino reaches the destination, it records the path if it improves upon the best solution found so far. It also prunes branches that cannot improve the current best path.

**Strengths:** Designed to find the shortest valid path through exhaustive exploration and pruning.

**Weaknesses:** Computationally inefficient because it may repeatedly explore the same positions through different paths.

### Caveman — Evolution of Dino

Caveman was developed as an optimization of Dino, with the goal of reducing unnecessary recursive exploration.

Its main addition is **failed-position caching**. When Caveman determines that exploration from a position has failed, it records that position. Future searches encountering a cached failed position are immediately pruned.

Caveman also distinguishes between three search outcomes:

- **Success:** A path reaches the destination.
- **Failure:** Exploration is considered unsuccessful.
- **Inconclusive:** Exploration is terminated because the current path cannot improve the best known solution.

The intended improvement is to reduce repeated work while preserving Dino's shortest-path correctness.

### Known Bug — Caveman's Kryptonite

Caveman currently has a correctness issue: its pruning and caching behavior can cause it to miss shorter valid paths.

A preserved regression maze, nicknamed **Caveman's Kryptonite**, produces the following results:

| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 294 | 251 |
| Path length | 32 | 40 |

Caveman performs fewer recursive calls but returns a longer path than Dino.

**Status:** Bug reproduced; root cause not yet established.

### Additional Regression Test — `maze_006.txt` (Evil Maze)

`maze_006.txt` is an intentionally unsolvable maze used to test whether an algorithm can efficiently establish that no path exists.

**Observed behavior:**
- **Dino:** Exceeded 500 million recursive calls without completing the search or determining that the maze was unsolvable.
- **Caveman:** Identified the maze as unsolvable relatively quickly.

This establishes a second major objective for MazeLab: algorithms must not only find shortest paths when they exist, but also correctly and efficiently determine when no solution exists.

The project will therefore evaluate **correctness, shortest-path optimality, and unsolvability detection**, alongside computational performance.

**Status:** Original behavior observed; exact benchmark measurements and independent verification pending.

### Next Steps

- Investigate Caveman's correctness without modifying the original implementation.
- Determine whether the issue originates from the caching strategy, pruning behavior, implementation, or their interaction.
- Preserve Caveman's Kryptonite as a regression test.
- Develop a corrected version and compare its correctness and performance against Dino.

### Attempted Caveman Fix

Familial memory (R parent branch has memory, then clear for D branch, and so on) **Important only at the very top level**. On maze_004.txt didn't save or improve anything same diagontics as without that improvement.
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 294 | 251 |
| Path length | 32 | 40 |
Both cache resets found 0 entries.

**Why did it fail?**
It failed because the problem was inside the R family. 
- Certainty of cause
    Both resets executed.
    Both resets found zero cached failures.
    The path length and recursive call count remained unchanged.
    The problematic [1,8] failure was observed during exploration within the R family.


### Caveman Fix Attempt Two
Ordered exploration based on smallest manhattan distance. **Important didn't use familial memory**. On maze_004.txt results are as follows
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 294 | 251 |
| Path length | 32 | 40 |
No observable improvement.

**Why did it fail?**
It failed because when he gets to a cross-roads he prioritizes going down even though D and R share the same manhattan distance. Since he choose down he explored that branch and then marked a good location as a failure
- Certainty of cause
    sorted sorts based on insertion order, when manhattan distances are ties, into the dictionary which inserts in D -> U -> R -> L order
    The algorithm because of recurrsion explores D branch first then updates failure
    R branch then recieves that memory