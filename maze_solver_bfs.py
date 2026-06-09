import os
import time
from maze_generator import create_maze

def clear_and_print(maze):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in maze:
        print(" ".join(row))
    print()
    time.sleep(0.08)

def solve_bfs(maze):
    working_maze = [row[:] for row in maze]
    
    start, end = None, None
    for r in range(len(working_maze)):
        for c in range(len(working_maze[0])):
            if working_maze[r][c] == 'S': start = (r, c)
            elif working_maze[r][c] == 'E': end = (r, c)

    if not start or not end: 
        return False

    queue = [start]
    visited = {start}

    while queue:
        curr = queue.pop(0)  # FIFO behavior
        
        if curr == end:
            clear_and_print(working_maze)
            return True

        if curr != start:
            working_maze[curr[0]][curr[1]] = 'o'  # Leave track permanently visible
            clear_and_print(working_maze)

        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(working_maze) and 0 <= nc < len(working_maze[0]):
                if working_maze[nr][nc] in ['.', 'E'] and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    return False

if name == "main":
    try:
        width = int(input("Enter maze width for BFS: "))
        height = int(input("Enter maze height for BFS: "))
    except ValueError:
        width, height = 15, 15

    test_maze = create_maze(width, height)
    solve_bfs(test_maze)