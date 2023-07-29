from collections import deque

# Function to get possible moves from a given state
def get_moves(state):
    moves = []
    empty_tile_index = state.index(0)
    row, col = divmod(empty_tile_index, 3)

    # Possible moves: up, down, left, right
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in possible_moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_index = new_row * 3 + new_col
            new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
            moves.append(new_state)

    return moves

# Breadth-First Search algorithm
def bfs(start_state, goal_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path

        visited.add(tuple(state))

        for move in get_moves(state):
            if tuple(move) not in visited:
                queue.append((move, path + [move]))

    return None

# Helper function to print the puzzle state in a readable format
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])

if __name__ == "__main__":
    # Define the initial and goal states
    initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    goal_state = [1, 2, 3, 4, 5, 8, 6, 0, 7]

    # Solve the puzzle
    solution = bfs(initial_state, goal_state)

    if solution:
        print("Solution found!")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_puzzle(state)
            print()
    else:
        print("No solution found.")