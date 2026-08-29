#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    
    # Define the 8 neighbor offsets (all directions except the center)
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Check each neighbor
    for dr, dc in neighbors:
        neighbor_row = row + dr
        neighbor_col = col + dc
        
        # Check if neighbor is within grid bounds
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            # Count if neighbor is alive (value == 1)
            if grid[neighbor_row][neighbor_col] == 1:
                alive_count += 1
    
    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Count the number of alive neighbors
            neighbor_count = count_neighbors(grid, r, c)
            current_state = grid[r][c]
            
            # Apply Conway's Game of Life rules
            if current_state == 1:  # Cell is currently alive
                # Rule 1 & 2: Survive if has 2 or 3 neighbors, die otherwise
                if neighbor_count == 2 or neighbor_count == 3:
                    next_grid[r][c] = 1  # Stays alive
                else:
                    next_grid[r][c] = 0  # Dies (underpopulation or overpopulation)
            else:  # Cell is currently dead
                # Rule 4: Reproduction - becomes alive if has exactly 3 neighbors
                if neighbor_count == 3:
                    next_grid[r][c] = 1  # Becomes alive
                # else: stays dead (already initialized to 0)

    return next_grid