import random

WALL = "#"
PATH = "."
START = "S"
END = "E"

def create_maze(w=21, h=15):
    if w % 2 == 0: w += 1
    if h % 2 == 0: h += 1

    maze = [[WALL] * w for _ in range(h)]
    visited = set()

    def carve(x, y):
        visited.add((x, y))
        maze[y][x] = PATH

        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < w and 0 < ny < h and (nx, ny) not in visited:
                maze[y + dy // 2][x + dx // 2] = PATH
                carve(nx, ny)

    carve(1, 1)
    maze[1][0] = START
    maze[h - 2][w - 1] = END
    return maze

if __name__ == "__main__":
    try:
        width = int(input("Enter maze width: "))
        height = int(input("Enter maze height: "))
    except ValueError:
        width, height = 15, 15
        
    generated_maze = create_maze(w=width, h=height)
    for row in generated_maze:
        print(" ".join(row))