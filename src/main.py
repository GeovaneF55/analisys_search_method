from algorithms import bfs, greedy, astar
import time

# Print Solution
def print_solution(alg, height, visited, time):
    print('\n{}'.format(alg))
    print(' - Caminho Solução: {} vértices'.format(height))
    print(' - Vértices percorridos: {} vértices'.format(visited))
    print(' - Tempo de execução: {0:0.4f}'.format(time))

# Print puzzle of the given board
def print_puzzle(label, board):
    print(label)
    for row in board:
        print(row)
    print('\n')

# Resolve the test to the solution with BFS, Greedy and Astar methods
def test(test, goal, label='Test'):

    print('\n##### ' + label + ' #####')
    print_puzzle('Objetivo:', goal)
    print_puzzle('Inicial:', test)

    start = time.time()
    height, visited = greedy(test, goal)
    end = time.time()
    print_solution('ALGORITMO GULOSO', height, visited, end-start)

    start = time.time()
    height, visited = astar(test, goal)
    end = time.time()
    print_solution('ALGORITMO A*', height, visited, end-start)
    
    start = time.time()
    height, visited = bfs(test, goal)
    end = time.time()
    print_solution('ALGORITMO BFS', height, visited, end-start)

# Main method
if __name__ == '__main__':
    goal = [[' ', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

    test([[' ', '1', '2'], ['3', '4', '5'], ['6', '7', '8']], goal, 'TESTE - Solução')
    test([['1', '2', ' '], ['3', '4', '5'], ['6', '7', '8']], goal, 'TESTE - Bem Perto da Solução')
    test([['1', '4', '2'], ['3', '5', '8'], ['6', ' ', '7']], goal, 'TESTE - Perto da Solução')
    test([['5', '2', '8'], ['4', '1', '7'], [' ', '3', '6']], goal, 'TESTE - Embaralhado 1')
    test([['2', '3', '6'], [' ', '1', '8'], ['4', '5', '7']], goal, 'TESTE - Embaralhado 2')