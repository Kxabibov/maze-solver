import sys
from maze_generator import create_maze
import maze_solver_dfs
import maze_solver_bfs

class StreamSplitter:
    """A custom pipeline that splits print statements to both a file and the screen."""
    def __init__(self, log_file, terminal_display):
        self.log_file = log_file
        self.terminal_display = terminal_display

    def write(self, data):
        self.log_file.write(data)          
        self.terminal_display.write(data)  

    def flush(self):
        self.log_file.flush()
        self.terminal_display.flush()


def print_maze(maze):
    """Helper function to cleanly print the maze grid layout row by row."""
    for row in maze:
        print(" ".join(row))


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

    # 🚀 STEP 1: Set up our streams BEFORE printing the raw maze layout
    original_stdout = sys.stdout
    terminal_display = sys.stderr

    try:
        with open("maze_output.txt", "w") as log_file:
            # 🚀 STEP 2: Turn on the splitter right here!
            sys.stdout = StreamSplitter(log_file, terminal_display)

            # Anything printed from this point forward goes into BOTH the terminal and the file!
            print("\n=====================================")
            print(f"   RAW GENERATED MAZE ({width}x{height})")
            print("=====================================")
            print_maze(maze)
            print("=====================================")
            print(f"Start Point: 'S' | End Point: 'E' | Selected Solver: {choice}")

            input("\nMaze layout generated successfully! Press Enter to watch history trace...")
            
            # 2. Redirect execution context to specified solver file logic
            if choice == "DFS":
                maze_solver_dfs.solve_dfs(maze)
            elif choice == "BFS":
                maze_solver_bfs.solve_bfs(maze)
            else:
                print("Invalid Choice selected.")
                
    finally:
        # SAFETY NET: Always restore standard terminal controls
        sys.stdout = original_stdout

if __name__ == "__main__":
    main()