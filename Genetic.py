import random
import heapq
# ================== CONFIG ==================
MAX_N = 30
POP_SIZE = 80
MUTATION_RATE = 0.2
GENERATIONS = 1200
N = 8
# ================== FITNESS ==================
def fitness(board):
    conflicts = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    for i in range(N):
        c = board[i]

        if c in cols:
            conflicts += 1
        else:
            cols.add(c)

        d1 = i - c
        d2 = i + c

        if d1 in diag1:
            conflicts += 1
        else:
            diag1.add(d1)

        if d2 in diag2:
            conflicts += 1
        else:
            diag2.add(d2)

    return -conflicts
# ================== POPULATION ==================
def create_population():
    return [[random.randint(0, N - 1) for _ in range(N)] for _ in range(POP_SIZE)]
# ================== SELECTION ==================
def selection(pop):
    return heapq.nlargest(30, pop, key=fitness)
# ================== CROSSOVER ==================
def crossover(p1, p2):
    point = random.randint(1, N - 2)
    return p1[:point] + p2[point:]
# ================== MUTATION ==================
def mutate(board):
    board = board[:]
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, N - 1)
        board[idx] = random.randint(0, N - 1)
    return board
# ================== GA ==================
def genetic_algorithm():
    pop = create_population()
    for _ in range(GENERATIONS):
        pop = selection(pop)
        new_pop = pop[:]
        while len(new_pop) < POP_SIZE:
            p1, p2 = random.sample(pop, 2)
            child = mutate(crossover(p1, p2))
            new_pop.append(child)
        pop = new_pop
        best = max(pop, key=fitness)
        if fitness(best) == 0:
            return best
    return max(pop, key=fitness)
# ================== PRINT BOARD ==================
def print_board(board):
    for i in range(N):
        row = ["." for _ in range(N)]
        row[board[i]] = "Q"
        print(" ".join(row))
# ================== MAIN ==================
def main():
    global N
    N = int(input("Enter N (e.g. 8): "))
    if N > MAX_N:
        N = MAX_N
    solution = genetic_algorithm()
    print("\nSolution:\n")
    print_board(solution)
if __name__ == "__main__":
    main()

    