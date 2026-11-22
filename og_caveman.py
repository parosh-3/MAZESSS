import time

class og_caveman:
    #Caveman clone
    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.position = []
        self.failed_positions = []
        self.path_best = []
        self.failure = 0
        self.success = 1
        self.inconclusive = 2
        self.recursive_calls = 0
        self.memory_prunes = 0


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
        solution = self.home_made_solve_maze(self.start, (self.start,), ())
        end = time.perf_counter()

        if solution == self.failure:
            print("No solution")

        #print(self.path_best)
        print(f"Number of function calls: {self.recursive_calls}")
        print(f"Memory Prunes: {self.memory_prunes}")
        print(f"Path Length: {len(self.path_best)}")
        print(f"Time Elapsed: {end - start:.6f} seconds")

        return None


    def home_made_solve_maze(self, current_position, path_position_current, path_direction_current):
        # Initialize overall_verdict so in case we have all failures we dont get any issues
        overall_verdict = self.failure

        #Benchmarking
        self.recursive_calls += 1

        # If we have reached a best path then if our path is greater than that path just terminate
        if len(path_direction_current) >= len(self.path_best) and len(self.path_best) != 0:
            return self.inconclusive
        
        # If we are in a failed position then we can't succeed so don't bother searching
        if current_position in self.failed_positions:
            self.memory_prunes += 1
            return self.failure

        # If we have reached "E" then stop and set that as our best path
        if current_position == self.end:
            self.path_best = path_direction_current
            return self.success
        
        # I need this recurrsion to know which directions it can go
        for direction in self.get_legal_moves(current_position):
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
            # If we reach the end tell parent we reached the end
            verdict = self.home_made_solve_maze(next_position, new_path_position, new_path_direction)
            if verdict == self.success:
                overall_verdict = self.success
            elif verdict == self.inconclusive and overall_verdict != self.success:
                overall_verdict = self.inconclusive
        # If we exhaustively searched every branch from the current position then mark that position as failed
        if overall_verdict == self.failure:
            self.failed_positions.append(current_position)

        return overall_verdict