import tkinter as tk
from tkinter import ttk
import time
import random
import heapq
class NQueensGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("N-Queens AI Solver")
        self.root.geometry("520x620")
        self.root.resizable(False, False)
        self.solution = None
        self.time_taken = 0
        self.algorithm_name = ""
        self.steps = 0
        self.font_main = ("Times New Romain", 10)
        self.font_title = ("Times New Romain", 14, "bold")
        self.create_widgets()
    # ================= UI =================
    def create_widgets(self):
        title = tk.Label(self.root, text="N-Queens Solver", font=self.font_title)
        title.pack(pady=8)
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text="N:", font=self.font_main).grid(row=0, column=0)
        self.n_var = tk.IntVar(value=8)
        tk.Entry(frame, textvariable=self.n_var, width=5).grid(row=0, column=1, padx=5)
        tk.Label(frame, text="Algorithm:", font=self.font_main).grid(row=0, column=2)
        self.algo_var = tk.StringVar(value="Backtracking (DFS)")
        self.algo_combo = ttk.Combobox(
            frame,
            textvariable=self.algo_var,
            width=22,
            state="readonly",
            values=[
                "Backtracking (DFS)",
                "Hill Climbing",
                "Best First Search",
                "Genetic Algorithm"
            ]
        )
        self.algo_combo.grid(row=0, column=3, padx=5)
        tk.Button(
            self.root,
            text="Solve",
            bg="#826251",
            fg="white",
            font=self.font_main,
            command=self.solve
        ).pack(pady=8)
        self.info = tk.Label(self.root, text="", font=self.font_main)
        self.info.pack()
        # Chess board
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)
        self.status = tk.Label(self.root, text="Ready", fg="gray", font=("Segoe UI", 9))
        self.status.pack()
    # ================= BOARD =================
    def draw_board(self, board):
        self.canvas.delete("all")
        n = len(board)
        size = 400 // n
        light = "#FFE8D1"
        dark = "#826251"
        for i in range(n):
            for j in range(n):
                x1, y1 = j * size, i * size
                x2, y2 = x1 + size, y1 + size
                color = light if (i + j) % 2 == 0 else dark
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                if board[i] == j:
                    self.canvas.create_text(
                        x1 + size // 2,
                        y1 + size // 2,
                        text="♚",
                        font=("Times New Romain", size // 2),
                        fill="black"
                    )
    # ================= BACKTRACKING =================
    def backtracking(self, n):
        board = [-1] * n
        self.steps = 0
        def safe(r, c):
            for i in range(r):
                if board[i] == c or abs(board[i] - c) == abs(i - r):
                    return False
            return True
        def dfs(r):
            self.steps += 1
            if r == n:
                return True
            for c in range(n):
                if safe(r, c):
                    board[r] = c
                    if dfs(r + 1):
                        return True
                    board[r] = -1
            return False
        start = time.perf_counter()
        dfs(0)
        self.time_taken = time.perf_counter() - start
        return board
    # ================= HILL CLIMBING =================
    def hill_climbing(self, n):
        self.steps = 0
        def conflicts(b):
            c = 0
            for i in range(n):
                for j in range(i + 1, n):
                    if b[i] == b[j] or abs(b[i] - b[j]) == abs(i - j):
                        c += 1
            return c
        start = time.perf_counter()
        board = [random.randint(0, n - 1) for _ in range(n)]
        for _ in range(4000):
            self.steps += 1
            h = conflicts(board)
            if h == 0:
                break
            best = board[:]
            best_h = h
            for col in range(n):
                old = board[col]
                for row in range(n):
                    board[col] = row
                    new_h = conflicts(board)
                    if new_h < best_h:
                        best_h = new_h
                        best = board[:]
                board[col] = old
            if best_h >= h:
                board = [random.randint(0, n - 1) for _ in range(n)]
            else:
                board = best
        self.time_taken = time.perf_counter() - start
        return board
    # ================= BEST FIRST =================
    def best_first(self, n):
        self.steps = 0
        def h(b):
            c = 0
            for i in range(len(b)):
                for j in range(i + 1, len(b)):
                    if b[i] == b[j] or abs(b[i] - b[j]) == abs(i - j):
                        c += 1
            return c
        start = time.perf_counter()
        heap = [(0, [])]
        visited = set()
        while heap:
            self.steps += 1
            _, board = heapq.heappop(heap)
            if len(board) == n:
                if h(board) == 0:
                    self.time_taken = time.perf_counter() - start
                    return board
                continue
            for col in range(n):
                new = board + [col]
                t = tuple(new)
                if t in visited:
                    continue
                visited.add(t)
                heapq.heappush(heap, (h(new), new))
        self.time_taken = time.perf_counter() - start
        return None
    # ================= GENETIC =================
    def genetic(self, n):
        self.steps = 0
        POP = 60
        GEN = 300
        MUT = 0.15
        def fitness(b):
            c = 0
            for i in range(n):
                for j in range(i + 1, n):
                    if b[i] == b[j] or abs(b[i] - b[j]) == abs(i - j):
                        c += 1
            return -c
        def cross(a, b):
            p = random.randint(1, n - 2)
            return a[:p] + b[p:]
        start = time.perf_counter()
        pop = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(POP)]
        for _ in range(GEN):
            self.steps += 1
            pop = sorted(pop, key=fitness, reverse=True)[:20]
            new = pop[:]
            while len(new) < POP:
                a, b = random.sample(pop, 2)
                child = cross(a, b)
                if random.random() < MUT:
                    i = random.randint(0, n - 1)
                    child[i] = random.randint(0, n - 1)
                new.append(child)
            pop = new
            best = max(pop, key=fitness)
            if fitness(best) == 0:
                self.time_taken = time.perf_counter() - start
                return best
        self.time_taken = time.perf_counter() - start
        return max(pop, key=fitness)
    # ================= SOLVE =================
    def solve(self):
        n = self.n_var.get()
        algo = self.algo_var.get()
        if n == 2 or n == 3:
            self.solution = None
            self.canvas.delete("all")
            self.info.config(
                text=f"No solution exists for N = {n}",
                fg="red"
            )
            self.status.config(text="Done")
            return
        self.status.config(text="Solving...")
        if algo == "Backtracking (DFS)":
            self.solution = self.backtracking(n)
            self.algorithm_name = "Backtracking"
        elif algo == "Hill Climbing":
            self.solution = self.hill_climbing(n)
            self.algorithm_name = "Hill Climbing"
        elif algo == "Best First Search":
            self.solution = self.best_first(n)
            self.algorithm_name = "Best First Search"
        else:
            self.solution = self.genetic(n)
            self.algorithm_name = "Genetic"
        if self.solution:
            self.draw_board(self.solution)
            self.info.config(
                text=f"{self.algorithm_name} | Time: {self.time_taken:.6f}s | Steps: {self.steps}",
                fg="green"
            )
        else:
            self.info.config(text="No solution found", fg="red")
        self.status.config(text="Done")
    def run(self):
        self.root.mainloop()
# ================= RUN =================
if __name__ == "__main__":
    NQueensGUI().run()