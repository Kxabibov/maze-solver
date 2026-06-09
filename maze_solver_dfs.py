import os
import time
from maze_generator import create_maze

def clear_and_print(maze):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in maze:
        print(" ".join(row))
    print()
    time.sleep(0.1)  # Slightly slower so you can see the deep exploration clearly

def solve_dfs(maze):
    working_maze = [row[:] for row in maze]
    
    # 1. Find Start and End
    start, end = None, None
    for r in range(len(working_maze)):
        for c in range(len(working_maze[0])):
            if working_maze[r][c] == 'S': start = (r, c)
            elif working_maze[r][c] == 'E': end = (r, c)

    if not start or not end: 
        return False

    # Stack only needs to keep track of coordinates for pure exploration history
    stack = [start]
    visited = {start}

    while stack:
        curr = stack.pop()  # Pop the latest cell (LIFO)
        r, c = curr
        
        # If we hit the end, show the final frame and exit
        if curr == end:
            clear_and_print(working_maze)
            return True

        # Leave a permanent trace on the map for every cell processed
        if curr != start:
            working_maze[r][c] = 'o'
            clear_and_print(working_maze)

        # Look in all 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            # Boundary and collision checks
            if 0 <= nr < len(working_maze) and 0 <= nc < len(working_maze[0]):
                if working_maze[nr][nc] in ['.', 'E'] and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append((nr, nc))
                    
    return False

if __name__ == "__main__":
    try:
        width = int(input("Enter maze width for DFS: "))
        height = int(input("Enter maze height for DFS: "))
    except ValueError:
        width, height = 15, 15

    test_maze = create_maze(width, height)
    solve_dfs(test_maze)