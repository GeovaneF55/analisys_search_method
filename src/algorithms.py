from queue import Queue

from puzzle import children

# Start and final are list of lists. The first one represents the initial
# state; the last one, the final state.
# Returns the number of moves made until reach final state.
def bfs(start, final):
    queue, visited = Queue(), []
    queue.put(start)

    state = 0
    path = [-1]

    while not queue.empty():
        current = queue.get()
         
        if current == final:
            break

        if current in visited:
            continue

        visited.append(current)
        for child in children(current):                
            if child not in visited:
                path.append(state)
                queue.put(child)

        state += 1

    nmoves = 0
    while path[state] != -1:
        nmoves += 1
        state   = path[state]

    return nmoves
