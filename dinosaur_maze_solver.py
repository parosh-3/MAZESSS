class dinosaur_solver:
    
    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.position = []
        self.failed_positions = []
        self.path_best = []
        self.calls = 0

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

    def get_legal_moves(self, position, direction_traveled = ""):
        legal_moves = []
        if len(position) != 2:
            return

        try:
            if self.maze[position[0] + 1][position[1]] != "#" and direction_traveled != "U":
                legal_moves.append("D")
        except IndexError:
            pass

        try:
            if self.maze[position[0] - 1][position[1]] != "#" and position[0] - 1 >= 0 and direction_traveled != "D":
                legal_moves.append("U")
        except IndexError:
            pass

        try:
            if self.maze[position[0]][position[1] + 1] != "#" and direction_traveled != "L":
                legal_moves.append("R")
        except IndexError:
            pass

        try:
            if self.maze[position[0]][position[1] - 1] != "#" and position[1] - 1 >= 0 and direction_traveled != "R":
                legal_moves.append("L")
        except IndexError:
            pass

        return legal_moves
    
    def add_to_failed_positions(self, path):
        for coordinate in path:
            if coordinate in self.failed_positions:
                self.failed_positions.append(coordinate)

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
        
        self.solve_maze(self.start, (self.start,), ())

        #print(self.path_best)
        print(f"Number of calls: {self.calls}")
        print(f"Path Length: {len(self.path_best)}")

        return None


    def solve_maze(self, current_position, path_position_current, path_direction_current):
        # If we have reached a best path then if our path is greater than that path just terminate
        if len(path_direction_current) >= len(self.path_best) and len(self.path_best) != 0:
            return
        
        self.calls += 1

        # If we have reached "E" then stop and set that as our best path
        if current_position == self.end:
            self.path_best = path_direction_current
            return
        
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
            if self.calls % 10000000 == 0:
                print(f"Dino calls: {self.calls:,}")
            
            self.solve_maze(next_position, new_path_position, new_path_direction)