import random
class NQueensSolver:
    def __init__(self, n):
        self.n = n
    def calculate_conflicts(self, board):
        conflicts = 0
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    def solve(self):
        board = [random.randint(0, self.n - 1) for _ in range(self.n)]
        history = []
        steps = 0
        while steps < 5000:
            h = self.calculate_conflicts(board)
            history.append(h)
            if h == 0: 
                return board, history, steps
            best_board = list(board)
            current_h = h
            for col in range(self.n):
                original_row = board[col]
                for row in range(self.n):
                    if row == original_row: 
                        continue
                    board[col] = row
                    new_h = self.calculate_conflicts(board)
                    if new_h < current_h:
                        current_h = new_h
                        best_board = list(board)
                board[col] = original_row
            if current_h >= h:
                board = [random.randint(0, self.n - 1) for _ in range(self.n)]
            else:
                board = best_board
            steps += 1
        return None, history, steps
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
if __name__ == "__main__":
    try:
        n_input = input("Enter the number of queens (e.g., 8): ")
        n = int(n_input)
        print(f"\nSearching for a solution for {n}-Queens...")
        solver = NQueensSolver(n)
        solution, history, total_steps = solver.solve()
        if solution:
            print(f"--- Solution Found in {total_steps} iterations ---")
            print_board(solution)
            print("\nFinal State (Column indices):", solution)
            print("Conflict History (last 10 steps):", history[-10:])
        else:
            print("Could not find a solution within the iteration limit.")
    except ValueError:
        print("Please enter a valid integer.")