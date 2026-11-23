import heapq


class oracle_visual:

    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.position = []
        self.failed_positions = []
        self.path_best = []
        self.loop_iterations = 0
        self.improved_time = 0
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
            self.start = (start2, start1)
            self.end = (end2, end1)

        else:
            self.coordinates = []

        self.dy = self.end[1] - self.start[1]
        self.dx = self.end[0] - self.start[0]

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

    def balance(self, position):
        px = position[0] - self.start[0]
        py = position[1] - self.start[1]

        return abs(self.dx * py - self.dy * px)

    def run(self):
        self.find_start_end()
        
        if len(self.position) < 2:
            self.position = self.start
        
        if len(self.get_legal_moves(self.start)) == 0 or len(self.get_legal_moves(self.end)) == 0:
            print("No Solution")
            return None
        
        return self.home_made_solve_maze(self.start)


    def home_made_solve_maze(self, start):
        pq = []
        steps = 0
        position = start
        arrival_time = {}
        distance_to_exit = self.get_manhattan_distance(start)
        priority = distance_to_exit + steps
        heapq.heappush(pq, (priority, distance_to_exit, self.balance(position), steps, position))
        while len(pq) != 0:
            self.loop_iterations += 1

            discard, discard2, discard3, steps, position = heapq.heappop(pq)

            if steps >= arrival_time.get(position, float('inf')):
                continue
            else:
                if position in arrival_time:
                    self.improved_time += 1
                else:
                    self.first_discoveries += 1
                arrival_time[position] = steps

            yield position
            if position == self.end:
                return steps

            moves = self.get_legal_moves(position)

            for move in moves:
                new_position = self.move(position, move)
                if new_position not in arrival_time:
                    distance_to_exit = self.get_manhattan_distance(new_position)
                    priority = distance_to_exit + steps + 1
                    heapq.heappush(pq, (priority, distance_to_exit, self.balance(new_position), steps + 1, new_position))

            

        return 0