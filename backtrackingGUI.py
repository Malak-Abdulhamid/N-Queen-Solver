from tkinter import *

def solve_n_queens(n):
    board = [-1] * n

    def isvalid(i, j):
        for row in range(i):
            if board[row] == j or abs(row - i) == abs(board[row] - j):
                return False
        return True

    def dfs(i):
        if i == n:
            return True
        for j in range(n):
            if isvalid(i, j):
                board[i] = j
                if dfs(i + 1):
                    return True
                board[i] = -1
        return False

    if dfs(0):
        return board
    return None

def draw_board(solution):
    for widget in frame.winfo_children():
        widget.destroy()

    if not solution:
        Label(frame, text="No solution!",font=("Arial", 14) ).pack()
        return

    n = len(solution)
    images.clear()
    square_size = 50

    for i in range(n):
        for j in range(n):
            color = "#463022" if (i + j) % 2 == 0 else "#fff7ae"
            if solution[i] == j:
                img = PhotoImage(file="queen-bee (2).png")
                images.append(img)
                label = Label(frame, image=img, bg=color)
            else:
                label = Label(frame, text="", bg=color)
            label.grid(row=i, column=j, sticky="nsew")

    for i in range(n):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)

def on_solve():
    n = int(entry.get())
    solution = solve_n_queens(n)
    draw_board(solution)


window = Tk()
window.title("N-Queens Solver 👑")
window.geometry("600x600")

label = Label(window, text=" N-Queens Solver ",
                font=("Arial", 20, 'bold'),
                bg="#f9ffd5",
                fg="#5a4b35",
                relief = RAISED,
                bd=5,
                padx = 5,
                pady = 5,
                 )

label.pack()
icon = PhotoImage(file="queen-bee (2).png")
window.iconphoto(True, icon)

window.configure(bg="#f9ffd5")

images = []

top_frame = Frame(window, bg="#f9ffd5", relief="ridge", bd=5, pady = 10)
top_frame.pack(pady=10)

Label(top_frame, text="Enter N:", 
      font=("Arial",16,'bold',),
      relief = RIDGE,
      bd=2,
      bg="#f9ffd5",
      fg="#5a4b35",
      ).pack(side=LEFT, padx=5)
entry = Entry(top_frame, font=("Arial", 14), width=10, justify="center", bg="#f9ffd5",
                fg="#5a4b35")
entry.pack(side=LEFT, padx=5)
Button(top_frame, text="Solve", font=("Arial", 14, 'bold'), bg="#f9ffd5", fg="#5a4b35", command=on_solve).pack(side=LEFT, padx=5)

# Frame للبورد
frame = Frame(window, relief=GROOVE, bd=5)
frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

window.mainloop()