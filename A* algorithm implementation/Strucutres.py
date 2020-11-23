class Node:
    """
    Node class that represents each cell on the grid.
    """
    def __init__(self, g = None, h = None, cost = 1):
        self.f = None
        self.g = g
        self.h = h
        self.cost = cost

class Astar:
    """
    Astar object that implement the A* algorithm.
    Initialized by providing:
        - file path of the map given as csv
        - start node as array [row, column] (starting from 0)
        - end node as array [row, column] (starting from 0)
    """
    def __init__(self, map_path, start = None, end = None):
        self.start = start
        self.end = end
        self.grid = self.build_the_grid(map_path)
        self.path = self.build_the_path()
    def build_the_grid(self, map_path):
        """
        Method that get's the data from the csv, and returns
        the grid of Nodes, representing the mapping.
        """
        import csv
        grid = []
        with open(map_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            r = 0
            for row in csv_reader:
                c = 0
                temp_row = []
                for i in range(len(row)):
                    if int(row[i]) > 0: temp_row += [Node(h=(((r - self.end[0])**2) + ((c - self.end[1])**2)) ** .5, cost=int(row[i]))]
                    else: temp_row += [None]
                    c += 1
                grid += [temp_row]
                r += 1
        return grid

    def build_the_path(self):
        """
        Applying A* search algorithm. Returns an array of coordinates([row, column]) on the path.
        """
        path, rows, columns = [self.start], len(self.grid) - 1, len(self.grid[0]) - 1
        while path[-1] != self.end:
            possible_ways = []
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (0 <= (path[-1][0] + direction[0]) <= rows) or (0 <= (path[-1][1] + direction[1]) <= columns):
                    temp_coord = [path[-1][0] + direction[0], path[-1][1] + direction[1]]
                    if self.grid[temp_coord[0]][temp_coord[1]] and temp_coord not in path:
                        possible_ways += [temp_coord]
            if not possible_ways:
                self.grid[path[-1][0]][path[-1][1]] = None
                path.pop()
                if not path: return print("No possible ways!!!")
                continue
            for way in possible_ways: self.grid[way[0]][way[1]].f = self.grid[way[0]][way[1]].cost + self.grid[way[0]][way[1]].h
            path_coord = possible_ways[0]
            for way in possible_ways[1:]:
                if self.grid[way[0]][way[1]].f < self.grid[path_coord[0]][path_coord[1]].f: path_coord = way
            path += [path_coord]
        return path       
