from maze_generator import create_maze
import maze_solver_dfs
import maze_solver_bfs

def main():
    print("=== MAIN CONFIGURATION ENGINE ===")
    try:
        width = int(input("Enter maze width: "))
        height = int(input("Enter maze height: "))
    except ValueError:
        print("Invalid input numbers. Defaulting to 15x15.")
        width, height = 15, 15

    choice = input("Choose solver method (DFS or BFS): ").strip().upper()
    
    # 1. Generate customized grid layout
    maze = create_maze(width, height)
    
    input("\nMaze layout generated successfully! Press Enter to watch history trace...")
    
    # 2. Redirect execution context to specified solver file logic
    if choice == "DFS":
        maze_solver_dfs.solve_dfs(maze)
    elif choice == "BFS":
        maze_solver_bfs.solve_bfs(maze)
    else:
        print("Invalid Choice selected.")

if __name__ == "__main__":
    main()