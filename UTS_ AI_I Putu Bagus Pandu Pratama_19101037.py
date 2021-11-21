
import queue

class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False

def heuristic_value(curr_node,dest):
    return (abs(curr_node.x-dest.x)+abs(curr_node.y-dest.y))

#GBFS algo for the maze
def gbfs(Grid, dest: Grid_Position, start: Grid_Position):

    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]
    m, n = (len(Grid), len(Grid))
    visited_blocks = [[False for i in range(m)]
                for j in range(n)]
    visited_blocks[start.x][start.y] = True
    q = queue.PriorityQueue()
    sol = Node(start, 0)
    q.put((0, sol))
    cells = 4
    cost = 0
    while q:
        current = q.get()  
        current_block = current[1]
        current_pos = current_block.pos

    
        if current_pos.x == dest.x and current_pos.y == dest.y:
            print("Algoritma yang digunakan = GBFS")
            print("No. gerakan yang digunakan = ", cost)
            return current_block.cost

        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1

        x_pos = current_pos.x
        y_pos = current_pos.y

        for i in range(cells):
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
                post = Grid_Position(x_pos, y_pos)
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
                post = Grid_Position(x_pos, y_pos)
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
                post = Grid_Position(x_pos, y_pos)
            if x_pos < 20 and y_pos < 20 and x_pos >= 0 and y_pos >= 0:
                if Grid[x_pos][y_pos] == 1:
                    if not visited_blocks[x_pos][y_pos]:
                        h = heuristic_value(post, dest)       
                        next_cell = Node(Grid_Position(x_pos, y_pos), current_block.cost + 1)
                        visited_blocks[x_pos][y_pos] = True
                        q.put((h, next_cell))

    return -1


def A_Star(maze, end, start):

    open1 = queue.PriorityQueue()
    closed = [[False for i in range(len(maze))]
                      for j in range(len(maze))]
    closed[start.x][start.y] = True

    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]


    Start = Node(start, 0)
    goal = Node(end, 0)

 
    open1.put((0, Start))
    cost = 0
    cells = 4


    while open1:

  

        current = open1.get()      
        current_node = current[1]  
        current_pos = current_node.pos


        if current_node not in closed:
            closed[current_pos.x][current_pos.y] = True
            cost = cost + 1

   
        if current_pos.x == end.x and current_pos.y == end.y:
            print("Algoritma yang digunakan = A* Algorithm")
            print("No. gerakan yang digunakan = ", cost)
            return current_node.cost

        x_pos = current_pos.x
        y_pos = current_pos.y

        for i in range(cells):
            if x_pos == len(maze) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
                post = Grid_Position(x_pos, y_pos)
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
                post = Grid_Position(x_pos, y_pos)
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
                post = Grid_Position(x_pos, y_pos)
            if x_pos < 20 and y_pos < 20 and x_pos >= 0 and y_pos >= 0:
                if maze[x_pos][y_pos] == 1:
                    if not closed[x_pos][y_pos]:
                        neighbor = Node(Grid_Position(x_pos, y_pos), current_node.cost + 1)
                        h = heuristic_value(neighbor.pos, end)      
                        f = h + neighbor.cost          
                        closed[x_pos][y_pos] = True     
                        open1.put((f, neighbor))

    return -1

def main():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
             [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
             [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
             [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    destination = Grid_Position(12, 19)
    starting_position = Grid_Position(14, 0)
    res = 0
    res1 = 0
    res = gbfs(maze, destination, starting_position)
    if res != -1:
        print("Jalur yang digunakan = ", res)
    else:
        print("Path does not exit")

    print()
    res1 = A_Star(maze, destination, starting_position)
    if res1 != -1:
       print("Jalur yang digunakan= ", res1)
    else:
       print("Path does not exit")


if __name__ == '__main__':
    main()

