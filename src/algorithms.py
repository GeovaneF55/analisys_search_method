from puzzle import children, get_pos

def qt_visited(visited):
    return len(visited)

# Manhattan Distance Method: Uses a distance from the increment with the
#   current value of the tray for calculating the distance
def manhattan(state, final):
    h = 0
    for i, row in enumerate(state):
        for j, elem in enumerate(row):
            x, y = get_pos(final, elem)
            if state[i][j] != final[i][j] and state[i][j] != ' ':
                h += abs(x - i) + abs(y - j)
    return h

# Breadth First Search (BFS) search method algorithm
# Start and final are list of lists. The first one represents the initial
# state; the last one, the final state.
# Returns the number of moves made until reach final state.
def bfs(start, final):
    queue, visited = [], []

    state = 0
    foundsolution = False

    elem = {
        'state': start,
        'path': -1,
        'g': 0
    }

    queue.append(elem)

    while queue and not foundsolution:
        current = queue.pop(0)
         
        if current['state'] == final:
            foundsolution = True
            break

        if current['state'] in visited:
            continue

        visited.append(current['state'])
        for child in children(current['state']):                
            if child not in visited:
                g = current['g'] + 1
                elem = {
                    'state': child,
                    'path': state,
                    'g': g
                }
                queue.append(elem)

        state += 1

    return (
        current['g'] if foundsolution else -1,
        qt_visited(visited)
    )

# Greedy search method algorithm
# Start and final are list of lists. The first one represents the initial
# state; the last one, the final state.
# Returns the number of moves made until reach final state.
def greedy(start, final):
    queue, visited = [], []

    state = 0
    foundsolution = False

    elem = {
        'state': start,
        'path': -1,
        'g': 0,
        'h': manhattan(start, final)
    }

    queue.append(elem)

    current = []

    while queue and not foundsolution:
        current = queue.pop(0)
         
        if current['state'] == final:
            foundsolution = True
            break

        if current['state'] in visited:
            continue

        visited.append(current['state'])
        for child in children(current['state']):                
            if child not in visited:
                g = current['g'] + 1
                h = manhattan(child, final)
                elem = {
                    'state': child,
                    'path': state,
                    'g': g,
                    'h': h
                }
                queue.append(elem)

        queue = sorted(queue, key=lambda k: k['h'])
        state += 1

    return (
        current['g'] if foundsolution else -1,
        qt_visited(visited)
    )

# A Star search method algorithm
# Start and final are list of lists. The first one represents the initial
# state; the last one, the final state.
# Returns the number of moves made until reach final state.
def astar(start, final):
    queue, visited = [], []

    state = 0
    foundsolution = False

    elem = {
        'state': start,
        'path': -1,
        'g': 0,
        'h+g': manhattan(start, final) + 0
    }

    queue.append(elem)

    current = []

    while queue and not foundsolution:
        current = queue.pop(0)
         
        if current['state'] == final:
            foundsolution = True
            break

        if current['state'] in visited:
            continue

        visited.append(current['state'])
        for child in children(current['state']):                
            if child not in visited:
                g = current['g'] + 1
                h = manhattan(child, final)
                elem = {
                    'state': child,
                    'path': state,
                    'g': g,
                    'h': h,
                    'h+g': h + g
                }
                queue.append(elem)

        queue = sorted(queue, key=lambda k: k['h+g'])
        state += 1

    return (
        current['g'] if foundsolution else -1,
        qt_visited(visited)
    )