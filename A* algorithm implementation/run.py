from Map import Map_Obj
from Strucutres import Astar

"""
To run the code:

1. Declare an instance of Astar by providing the path to the map, start and ending points.
Example: task1 = Astar('Samfundet_map_1.csv', [27,18], [40, 32])

2. To see the map, run the show_map method by providing the path
Example: task1_map.show_map(task1.path)
"""

# Task 1

task1 = Astar('Samfundet_map_1.csv', [27,18], [40, 32])
task1_map = Map_Obj(1)
task1_map.show_map(task1.path)

# Task 2

task2 = Astar('Samfundet_map_1.csv', [8, 5], [40, 32])
task2_map = Map_Obj(2)
task2_map.show_map(task2.path)

# Task 3

task3 = Astar('Samfundet_map_2.csv', [28, 32], [6, 32])
task3_map = Map_Obj(3)
task3_map.show_map(task3.path)

# Task 4

task4 = Astar('Samfundet_map_Edgar_full.csv', [28, 32], [6, 32])
task4_map = Map_Obj(4)
task4_map.show_map(task4.path)
