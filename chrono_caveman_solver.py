import time

class chrono_caveman_solver:
    
    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.position = []
        self.time_tracker = {}
        self.path_best = []
        self.recursive_calls = 0
        self.failed_debugging = []
        self.visited_old_failed = 0
        self.improved_arrivals = 0
        self.first_discoveries = 0


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
            self.start = [start2, start1]
            self.end = [end2, end1]

        else:
            self.coordinates = []

    def get_manhattan_distance(self, position) -> int:
        return abs(self.end[0] - position[0]) + abs(self.end[1] - position[1])
    
    def get_legal_moves(self, position, direction_traveled = ""):
        legal_moves = {}
        smallest_distance = float('inf')
        has_tie = False
        if len(position) != 2:
            return

        try:
            if self.maze[position[0] + 1][position[1]] != "#" and direction_traveled != "U":
                legal_moves["D"] = self.get_manhattan_distance([position[0] + 1, position[1]])
                smallest_distance = legal_moves["D"]
        except IndexError:
            pass

        try:
            if self.maze[position[0] - 1][position[1]] != "#" and position[0] - 1 >= 0 and direction_traveled != "D":
                legal_moves["U"] = self.get_manhattan_distance([position[0] - 1, position[1]])
                if (smallest_distance == legal_moves["U"]):
                    has_tie = True
                elif (smallest_distance > legal_moves["U"]):
                    smallest_distance = legal_moves["U"]
        except IndexError:
            pass

        try:
            if self.maze[position[0]][position[1] + 1] != "#" and direction_traveled != "L":
                legal_moves["R"] = self.get_manhattan_distance([position[0], position[1] + 1])
                if (smallest_distance == legal_moves["R"]):
                    has_tie = True
                elif (smallest_distance > legal_moves["R"]):
                    smallest_distance = legal_moves["R"]
                    has_tie = False
        except IndexError:
            pass

        try:
            if self.maze[position[0]][position[1] - 1] != "#" and position[1] - 1 >= 0 and direction_traveled != "R":
                legal_moves["L"] = self.get_manhattan_distance([position[0], position[1] - 1])
                if (smallest_distance == legal_moves["L"]):
                    has_tie = True
                elif (smallest_distance > legal_moves["L"]):
                    smallest_distance = legal_moves["L"]
                    has_tie = False
        except IndexError:
            pass

        # Prioritize moves based on smallest manhattan distance
        return sorted(legal_moves, key=legal_moves.get), has_tie

    def move(self, position, direction):
        if direction == "R":
            return[position[0], position[1] + 1]
        elif direction == "L":
            return [position[0], position[1] - 1]
        elif direction == "U":
            return [position[0] - 1, position[1]]
        elif direction == "D":
            return [position[0] + 1, position[1]]


    def run(self):
        self.find_start_end()
        
        if len(self.position) < 2:
            self.position = self.start
        
        if len(self.get_legal_moves(self.start)) == 0 or len(self.get_legal_moves(self.end)) == 0:
            print("No Solution")
            return None

        start = time.perf_counter()
        self.home_made_solve_maze(self.start, (self.start,), ())
        end = time.perf_counter()

        if (len(self.path_best) == 0):
            print("No Solution")
        #print(self.path_best)
        print(f"Number of function calls: {self.recursive_calls}")
        print(f"Path Length: {len(self.path_best)}")
        print(f"Improved Time: {self.improved_arrivals}")
        print(f"First Discoveries: {self.first_discoveries}")
        print(f"Time Elapsed: {end - start:.6f} seconds")

        return None


    def home_made_solve_maze(self, current_position, path_position_current, path_direction_current):

        #Benchmarking
        self.recursive_calls += 1
        #Checks if we reached this position in a better time
        if len(path_direction_current) >= self.time_tracker.get(tuple(current_position), float('inf')):
            return
        else:
            if tuple(current_position) in self.time_tracker:
                self.improved_arrivals += 1
            else:
                self.first_discoveries += 1
            self.time_tracker[tuple(current_position)] = len(path_direction_current)

        # If we have reached a best path then if our path is greater than that path just terminate
        if len(path_direction_current) >= len(self.path_best) and len(self.path_best) != 0:
            return

        # If we have reached "E" then stop and set that as our best path
        if current_position == self.end:
            self.path_best = path_direction_current
            return

        moves, has_tie = self.get_legal_moves(current_position)
        
        # I need this recurrsion to know which directions it can go
        for direction in moves: 
            # Get the next position  
            next_position = self.move(current_position, direction)
            # Using tuples because lists get modified for all instances of the function
            new_path_direction = path_direction_current + (direction,)
            # Samething as above
            new_path_position = path_position_current + (next_position,)
            # Prevents going in loops while only stopping to search a single branch not the entire node/loop
            if next_position in path_position_current:
                continue
            # Move on to the next part of the branch!
            self.home_made_solve_maze(next_position, new_path_position, new_path_direction)
            
        
