from FireAnt import FireAnt
from UnionFind import UnionFind
import random

class fire_ant_visual:
    def __init__(self, maze):
        self.maze = maze
        self.global_map = {}


    def find_start_end(self):
        coordinates = []
        for i in range(len(self.maze)):
            try:
                coordinates.append(self.maze[i].index("S"))
                coordinates.append(i)
            except ValueError:
                pass
            try:
                coordinates.append(self.maze[i].index("E"))
                coordinates.append(i)
            except ValueError:
                pass
        if len(coordinates) == 4:
            start1, start2, end1, end2 = coordinates
            self.start = (start2, start1)
            self.end = (end2, end1)

        else:
            self.coordinates = []

    def get_manhattan_distance(self, position) -> int:
        return abs(self.end[0] - position[0]) + abs(self.end[1] - position[1])
    
    def get_legal_moves(self, position, direction_traveled = ""):
        legal_moves = {}
        if len(position) != 2:
            return

        try:
            if self.maze[position[0] + 1][position[1]] != "#" and direction_traveled != "U":
                legal_moves["D"] = self.get_manhattan_distance([position[0] + 1, position[1]])
        except IndexError:
            pass

        try:
            if self.maze[position[0] - 1][position[1]] != "#" and position[0] - 1 >= 0 and direction_traveled != "D":
                legal_moves["U"] = self.get_manhattan_distance([position[0] - 1, position[1]])
        except IndexError:
            pass

        try:
            if self.maze[position[0]][position[1] + 1] != "#" and direction_traveled != "L":
                legal_moves["R"] = self.get_manhattan_distance([position[0], position[1] + 1])
        except IndexError:
            pass

        try:
            if self.maze[position[0]][position[1] - 1] != "#" and position[1] - 1 >= 0 and direction_traveled != "R":
                legal_moves["L"] = self.get_manhattan_distance([position[0], position[1] - 1])
        except IndexError:
            pass

        # Prioritize moves based on smallest manhattan distance
        return sorted(legal_moves, key=legal_moves.get)

    def move(self, position, direction):
        if direction == "R":
            return (position[0], position[1] + 1)
        elif direction == "L":
            return (position[0], position[1] - 1)
        elif direction == "U":
            return (position[0] - 1, position[1])
        elif direction == "D":
            return (position[0] + 1, position[1])

    def get_valid_start(self, otherstarts: list) -> tuple:
        while True:
            row = random.randint(0, len(self.maze) - 1)
            col = random.randint(0, len(self.maze[0]) - 1)
            if self.maze[row][col] != "#" and (row, col) not in otherstarts:
                return (row, col)


    def run(self, num_ants: int, seed: int | None = None):
        self.find_start_end()

        if num_ants <= 0:
            raise ValueError("Enter a positive number of ants")
    
        
        if len(self.get_legal_moves(self.start)) == 0 or len(self.get_legal_moves(self.end)) == 0:
            print("No Solution")
            return None

        if seed is None:
            seed = random.randrange(2**32)

        random.seed(seed)
        print(f"Random Seed: {seed}")

        self.ants = []
        starting_positions = []
        
        for i in range(num_ants):
            valid_start = self.get_valid_start(starting_positions)
            self.global_map[valid_start] = i
            self.ants.append(FireAnt(valid_start))
            starting_positions.append(valid_start)

        yield from self.home_made_solve_maze()

        return None

    def all_not_empty(self):
        for ant in self.ants:
            if not ant.is_empty():
                return True

        return False

    def home_made_solve_maze(self):
        un = UnionFind(len(self.ants))
        colony_at_start = -1
        colony_at_end = -2
    
        while self.all_not_empty():
    
            for i, ant in enumerate(self.ants):
                position = ant.get_and_remove()
                    
    
                if position is None:
                    continue

                yield position, i
    
                moves = self.get_legal_moves(position)
    
                if position == self.start:
                    colony_at_start = un.find(i)
                elif position == self.end:
                    colony_at_end = un.find(i)
    
    
                if colony_at_start >= 0 and colony_at_end >= 0 and un.find(colony_at_start) == un.find(colony_at_end):
                    return 1
    
                for move in moves:
                    new_position = self.move(position, move)
                    if new_position in self.global_map:
                        un.merge(i, self.global_map[new_position])
                        continue
                    self.global_map[new_position] = i
                    ant.add_to_queue(new_position)
    
    
    
        return 0