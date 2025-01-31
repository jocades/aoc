from typing import List, Tuple, Dict
from collections import deque


class ShortestPathDemo:
    @staticmethod
    def bfs_path_visualization(
        grid: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
    ):
        """
        Demonstrate BFS path finding with visualization of exploration levels

        Args:
            grid (List[List[int]]): 2D grid where 0 is path, 1 is wall
            start (Tuple[int, int]): Starting coordinates
            end (Tuple[int, int]): Ending coordinates
        """
        rows, cols = len(grid), len(grid[0])

        # Tracking distances and previous nodes for path reconstruction
        distances = [[float("inf")] * cols for _ in range(rows)]
        previous = [[None] * cols for _ in range(rows)]

        # Possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Queue for BFS, storing (x, y, distance)
        queue = deque([(start[0], start[1], 0)])
        distances[start[0]][start[1]] = 0

        # BFS Exploration
        while queue:
            x, y, current_distance = queue.popleft()

            # Reached the end?
            if (x, y) == end:
                break

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check if move is valid
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and grid[nx][ny] == 0
                    and distances[nx][ny] == float("inf")
                ):
                    # Update distance and previous node
                    distances[nx][ny] = current_distance + 1
                    previous[nx][ny] = (x, y)

                    # Add to queue
                    queue.append((nx, ny, current_distance + 1))

        # Reconstruct path
        path = []
        current = end
        while current:
            path.append(current)
            current = previous[current[0]][current[1]]
        path.reverse()

        # Visualization
        print("Grid with Exploration Levels:")
        for r in range(rows):
            row_display = []
            for c in range(cols):
                if (r, c) == start:
                    row_display.append("S")  # Start
                elif (r, c) == end:
                    row_display.append("E")  # End
                elif distances[r][c] != float("inf"):
                    row_display.append(str(distances[r][c]))  # Distance from start
                elif grid[r][c] == 1:
                    row_display.append("#")  # Wall
                else:
                    row_display.append(".")  # Unreached
            print(" ".join(row_display))

        print("\nShortest Path:", path)
        print("Path Length:", len(path) - 1)


def main():
    # Demonstration grid
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]

    start = (0, 0)
    end = (4, 4)

    demo = ShortestPathDemo()
    demo.bfs_path_visualization(grid, start, end)


if __name__ == "__main__":
    main()
