from algorithms import bfs

if __name__ == '__main__':
    solution = [[' ', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    test     = [['1', '4', '2'], ['3', '5', '8'], ['6', ' ', '7']]

    nmoves = bfs(test, solution)
    print(nmoves)
