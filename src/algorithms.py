from queue import Queue

from puzzle import children

# Start and final are list of lists. The first one represents the initial
# state; the last one, the final state.
# Returns the number of moves made until reach final state.
def bfs(start, final):
    queue, visited = Queue(), []
    queue.put(start)
    nmoves = 0

    while not queue.empty():
        current = queue.get()
       
        print(nmoves)

        if current == final:
            queue = Queue()

        if current in visited:
            continue

        nmoves += 1
        visited.append(current)

        for child in children(current):
            if child not in visited:
                queue.put(child)

    return nmoves
