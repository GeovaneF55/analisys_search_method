from algorithms import bfs

if __name__ == '__main__':
    solution = [[' ', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    test     = [['5', '2', '8'], ['4', '1', '7'], [' ', '3', '6']]

    nmoves = bfs(test, solution)
    print(nmoves)
