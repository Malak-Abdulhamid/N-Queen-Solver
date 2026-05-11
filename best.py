import heapq
def heuristic(queens):
    conflicts = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            r1, c1 = queens[i]
            r2, c2 = queens[j]
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                conflicts += 1
    return conflicts
def best_first_search(n):
    counter = 0
    initial_board = []
    heap = [(heuristic(initial_board), counter, initial_board)]
    nodes_expanded = 0
    while heap:
        h, _, board = heapq.heappop(heap)
        nodes_expanded += 1
        if len(board) == n and h == 0:
            print(f"Solution found after expanding {nodes_expanded} nodes.")
            return board
        if len(board) < n:
            row = len(board)
            for col in range(n):
                new_board = board + [(row, col)]
                counter += 1
                h_value = heuristic(new_board)
                heapq.heappush(heap, (h_value, counter, new_board))
    print(f"No solution found after expanding {nodes_expanded} nodes.")
    return None
solution = int(input("Enter the number of queens: "))
print(best_first_search(solution))

