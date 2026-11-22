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

**Commit of this version**
https://github.com/parosh-3/MAZESSS/tree/cf3ba1c09fb5ebac95ecba3675ef9903b7d8f65d

### Caveman Fix Attempt Three
Success! The fix combines the idea of familial memory and priority ordering. When there is a tie between manhattan distances it gets flagged as a cross-roads and then Caveman remembers everything up until that cross-roads but gets rid of memory of the subsequent children. So at cross-road, D and R share the same memory but when branch D finishes searching it deletes its memory and R branch uses only the memory achieved up until the cross-road. The same tie-breaker as the previous attempt at a fix. Metrics
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 294 | 323 |
| Path length | 32 | 32 |
Outcome he found the shortest path however on maze_004.txt he failed to achieve that score in a shorter amount of recurrsive calls than Dino.

**Why did Caveman perform worse?**
I have no clue, Dino only prunes based on best path and if he walks in circles. So the memory should save Caveman steps/calls. A plausible explanation is that Dino searches based on D -> U -> R -> L order while Caveman searches based on distance.

**Commit of this version**
https://github.com/parosh-3/MAZESSS/tree/6876d5ee1f7063a696f1331479fecf7b8dd15a68

### Caveman vs Dino (With priority move decisions)
Using the same priority move decision making system they achieved the same amount of calls
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 323 | 323 |
| Path length | 32 | 32 |
There was a bug where Dino measured only calls where he didn't reject moves due to the length of path pruning. So I'll restore the older D -> U -> R -> L move order and see if he does better or worse on maze_004.txt. With that being said take the numbers above this one with a grain of salt for Dino specifically.
After running:
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 323 | 323 |
| Path length | 32 | 32 |
I tried Caveman vs Dino on mazes 1-5 and only on maze 2 was there a difference giving results
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 124 | 62 |
| Path length | 25 | 25 |
That heavily implies that his memory pruning is heavily dependent on maze structure. On maze 6 Caveman showed no improved speed over Dino I did interupt the search. I ran Caveman for about a minute and he wasn't able to know that the maze had no solution. I'll check now with a memory prune counter to see how many times it gets activated in all of the mazes.

**Final Results**
Caveman across all tests has shown that in maze 2 his improvement was 50% less calls. However, running them against eachother on maze 2 again and making Dino use manhattan priority based movement gave these results
| Metric | Dino | Caveman |
|---|---:|---:|
| Recursive calls | 62 | 62 |
| Path length | 25 | 25 |
I had added another metric for Caveman and he used the memory pruning 0 times across mazes 1-5. This doesn't prove that his memory system doesn't work but it gives evidence for that. It does give evidence that the manhattan move ordering can reduce work while not making more work. 

## November 22, 2026 - Chrono Caveman Arrives
Chrono Caveman improves upon Caveman's idea of memory by storing arrival time per cell. If he arrives later or at the same time prune. This is provably correct so I'll leave that as a proof for the reader. He still uses Manhattan distance ordering. The next major improvement would be to order his exploration more efficiently.

**Benchmark of the Day**
Maze 16 a 50x50 maze with 865 indpendent loops.
- Chrono Caveman:
    Number of function calls: 106105
    Path Length: 92
    Improved Time: 53084
    First Discoveries: 1748
- Dino:
    Number of function calls: Lower bound of 4.18 * 10^22
    Path Length: Likely found to be 92
