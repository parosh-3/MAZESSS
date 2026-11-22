from caveman_maze_solver import caveman_solver
from dinosaur_maze_solver import dinosaur_solver

def main():
    maze_names = ["maze_001.txt", 
                  "maze_002.txt", 
                  "maze_003.txt", 
                  "maze_004.txt", # Caveman's Cryptonite don't delete
                  "maze_005.txt",
                  "maze_006.txt" # Dinosaur's personal hell, (No path to E)
                  ]
    print("CAVEMAN BABY")
    modern = caveman_solver(load_maze(maze_names[3]))
    modern.run()

    print("DINOSAUR BABY")
    prehistoric = dinosaur_solver(load_maze(maze_names[3]))
    prehistoric.run()
    
    #for i in range(len(maze_names)):
        #print(f"Maze Number: {i + 1}")
        
        #maze = load_maze(maze_names[i])

        #print("CAVEMAN BABY")
        #modern = caveman_solver(maze)
        #modern.run()

        #print("DINOSAUR BABY")
        #prehistoric = dinosaur_solver(maze)
        #prehistoric.run()

        #print()

def load_maze(maze_name):
    maze = []
    with open("its_aMAZEing/" + maze_name) as file:
        for line in file:
            maze.append(line.rstrip("\n"))

    return maze
   

if __name__ == "__main__":
    main()