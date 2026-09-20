import mazesolver

def main():
    maze = [
        "##########",
        "#S...#...#",
        "#.##.#.#.#",
        "#....#.#.#",
        "####...#.#",
        "#....###.#",
        "#.##.....#",
        "#......#E#",
        "##########"
    ]
    solver = mazesolver.maze_solver(maze)
    solver.run()


   

if __name__ == "__main__":
    main()