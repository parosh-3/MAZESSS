from caveman_maze_solver import caveman_solver
from oracle_caveman_solver import oracle_caveman_solver
from chief_caveman_solver import chief_caveman_solver
from chrono_caveman_solver import chrono_caveman_solver
from og_caveman import og_caveman
import sys
sys.setrecursionlimit(5000)

def main():
    maze_names = ["maze_001.txt", 
                  "maze_002.txt", 
                  "maze_003.txt", 
                  "maze_004.txt", # Caveman's Cryptonite don't delete
                  "maze_005.txt",
                  "maze_006.txt", # Dinosaur's personal hell, (No path to E)
                  "maze_007.txt",
                  "maze_008.txt",
                  "maze_009.txt",
                  "maze_010.txt",
                  "maze_011.txt",
                  "maze_012.txt", # high wall density 25x29
                  "maze_013.txt", # medium wall density 25x29
                  "maze_014.txt", # low wall density 25x29
                  "maze_015.txt", # 50x50 monster
                  "maze_016.txt", # 50x50 low density monster don't run dino on it. Lower bound = 4.18 * 10^22 calls would finish in ~ 3.4 billion years at ~390k calls a second
                  "maze_017.txt", # Open battle field 0 walls 8x8 64 traversable squares.
                  "maze_018.txt", # 25x29 dead-end heavy solveable maze
                  "maze_019.txt", # 25x29 dead-end heavy unsolveable maze
                  "maze_020.txt", # 25x29 Open solveable maze
                  "maze_021.txt" # 25x29 Open unsolveable maze
                  ]
    
    for i in range(20, 21):
        print(f"Maze Number: {i + 1}")
            
        maze = load_maze(maze_names[i])

        print("ORACLE CAVEMAN BABY")
        oracle = oracle_caveman_solver(maze)
        oracle.run()

        print("CHIEF CAVEMAN BABY")
        chief = chief_caveman_solver(maze)
        chief.run()

        print()

def load_maze(maze_name):
    maze = []
    with open("its_aMAZEing/" + maze_name) as file:
        for line in file:
            maze.append(line.rstrip("\n"))

    return maze
   

if __name__ == "__main__":
    main()