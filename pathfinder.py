from typing import *
from collections import deque

dx = [ -1, 0, 1,  0, -1,  1, 1, -1]
dy = [  0, 1, 0, -1, -1, -1, 1,  1]

class Node:
    def __init__(self, coord: Tuple, parent = None) -> None:
        self.coord = coord
        self.parent = parent

class PathFinder:
    def __init__(self, dirNum) -> None:
        self.dirNum = dirNum
        pass

    def isValid(self, grid: List[List[int]], visited: set, coord: Tuple[int, int]) -> bool:

        if coord in visited:
            return False

        if coord[0] >= 0 and coord[0] <= len(grid[0])-1 and coord[1] >= 0 and coord[1] <= len(grid[0])-1:
            return grid[coord[0]][coord[1]] == 0 or grid[coord[0]][coord[1]] == 2
        else:
            return False
    
    def find_path(self, grid: List[List[int]], start_coord: Tuple):
        startNode = Node(coord=start_coord)
        queue:Deque[Node] = deque()
        visited = set()
        visited.add(start_coord)
        queue.append(startNode)

        # visit neighbours 
        count = 0
        while (len(queue) > 0 ):
            count += 1
            current_node = queue.popleft()
            visited.add(current_node.coord)

            if grid[current_node.coord[0]][current_node.coord[1]] == 2:
                break

            for i in range(self.dirNum):
                new_coord = (current_node.coord[0]+dx[i], current_node.coord[1]+dy[i])
                if self.isValid(grid=grid, visited=visited, coord=new_coord):
                    queue.append(Node(coord=new_coord, parent=current_node))

        return current_node
