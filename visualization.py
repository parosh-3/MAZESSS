import pygame
from mazes import load_maze
from chief_visual import chief_visual
from oracle_visual import oracle_visual

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Caveman Cinema")

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
                      "maze_021.txt", # 25x29 Open unsolveable maze
                      "maze_022.txt", #50x50 down then right solvable maze
                      "maze_023.txt"
                      ]
    i = 15
    maze = load_maze(maze_names[i])

    chief = oracle_visual(maze)

    explorer = chief.run()

    running = True

    clock = pygame.time.Clock()

    visited = set()
    finished = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        try:
            position = next(explorer)
            visited.add(position)
        except StopIteration:
            i = (i + 1) % len(maze_names)
            pygame.display.set_caption(f"Caveman Cinema — {maze_names[i]}")
            maze = load_maze(maze_names[i])
            chief = oracle_visual(maze)
            explorer = chief.run()
            visited.clear()
            position = next(explorer)

            pass
        
        screen.fill((25, 25, 25))
        draw_maze(maze, screen)
        draw_visited_rooms(visited, screen, maze)
        draw_position(maze, screen, position)
        pygame.display.flip()
        clock.tick(20)

    pygame.quit()


def draw_visited_rooms(visited, screen, maze):
    x = len(maze)
    y = len(maze[0])
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width / y
    cell_height = screen_height / x
    for position in visited:
        pixel_x = position[1] * cell_width
        pixel_y = position[0] * cell_height
        pygame.draw.rect(screen, (19, 41, 75), (pixel_x, pixel_y, cell_width, cell_height))


def draw_position(maze, screen, caveman):
    x = len(maze)
    y = len(maze[0])
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width / y
    cell_height = screen_height / x
    pixel_x = caveman[1] * cell_width
    pixel_y = caveman[0] * cell_height

    pygame.draw.rect(screen, (255, 127, 0), (pixel_x, pixel_y, cell_width, cell_height))

def draw_maze(maze, screen):
    x = len(maze)
    y = len(maze[0])
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width / y
    cell_height = screen_height / x
    for row in range(x):
        for col in range(y):
            if maze[row][col] != "#":
                pixel_x = col * cell_width
                pixel_y = row * cell_height
                if maze[row][col] == "S":
                    pygame.draw.rect(screen, (0, 255, 0), (pixel_x, pixel_y, cell_width, cell_height))
                elif maze[row][col] == "E":
                    pygame.draw.rect(screen, (255, 0, 0), (pixel_x, pixel_y, cell_width, cell_height))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (pixel_x, pixel_y, cell_width, cell_height))

if __name__ == "__main__":
    main()