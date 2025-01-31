from typing import List, Tuple, Optional


class GridSearch:
    def __init__(self, grid: List[List[int]]):
        """
        Initialize the grid search.
        0 represents open path
        1 represents wall/obstacle

        Args:
            grid (List[List[int]]): 2D grid representing the map
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid_move(self, x: int, y: int) -> bool:
        """
        Check if the move is within grid bounds and not a wall

        Args:
            x (int): x-coordinate
            y (int): y-coordinate

        Returns:
            bool: True if move is valid, False otherwise
        """
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    def depth_first_search(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> Optional[List[Tuple[int, int]]]:
        """
        Depth-First Search (DFS) for pathfinding

        Characteristics:
        - Explores as far as possible along each branch before backtracking
        - Does not guarantee the shortest path
        - Uses less memory compared to BFS
        - Can get stuck in infinite loops if not carefully implemented

        Args:
            start (Tuple[int, int]): Starting coordinates
            end (Tuple[int, int]): Ending coordinates

        Returns:
            Optional[List[Tuple[int, int]]]: Path from start to end, or None if no path exists
        """
        # Possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Create a copy of the grid to mark visited cells
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        # Track the path
        path = []

        def dfs(x: int, y: int) -> bool:
            """
            Recursive DFS implementation

            Args:
                x (int): Current x-coordinate
                y (int): Current y-coordinate

            Returns:
                bool: True if path to end is found, False otherwise
            """
            # Check if current position is out of bounds or already visited
            if not self.is_valid_move(x, y) or visited[x][y]:
                return False

            # Mark as visited
            visited[x][y] = True
            path.append((x, y))

            # Check if reached the end
            if (x, y) == end:
                return True

            # Explore in all four directions
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                # Recursive DFS
                if dfs(next_x, next_y):
                    return True

            # Backtrack if no path found
            path.pop()
            return False

        # Start DFS from the start point
        dfs(start[0], start[1])

        return path if path and path[-1] == end else None

    def breadth_first_search(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> Optional[List[Tuple[int, int]]]:
        """
        Breadth-First Search (BFS) for pathfinding

        Characteristics:
        - Explores all neighboring cells before moving to next level
        - Guarantees the shortest path in an unweighted graph
        - Uses more memory as it keeps track of all possible paths
        - Ideal for finding shortest path in grid-based navigation

        Args:
            start (Tuple[int, int]): Starting coordinates
            end (Tuple[int, int]): Ending coordinates

        Returns:
            Optional[List[Tuple[int, int]]]: Shortest path from start to end, or None if no path exists
        """
        # Possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Create a copy of the grid to mark visited cells
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        # Queue to store cells to visit
        queue = [(start[0], start[1], [start])]
        visited[start[0]][start[1]] = True

        while queue:
            x, y, path = queue.pop(0)

            # Check if reached the end
            if (x, y) == end:
                return path

            # Explore in all four directions
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy

                # Check if move is valid and not visited
                if self.is_valid_move(next_x, next_y) and not visited[next_x][next_y]:
                    # Mark as visited
                    visited[next_x][next_y] = True

                    # Create new path by extending current path
                    new_path = path + [(next_x, next_y)]
                    queue.append((next_x, next_y, new_path))

        # No path found
        return None


# Example usage and demonstration
def main():
    # Example grid: 0 = open path, 1 = wall
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]

    # Create grid search instance
    grid_search = GridSearch(grid)

    # Define start and end points
    start = (0, 0)
    end = (4, 4)

    print("Depth-First Search (DFS) Path:")
    dfs_path = grid_search.depth_first_search(start, end)
    print(dfs_path)

    print("\nBreadth-First Search (BFS) Path:")
    bfs_path = grid_search.breadth_first_search(start, end)
    print(bfs_path)


if __name__ == "__main__":
    main()
