from algorithms import bfs, greedy, astar

# Print puzzle of the given board
def print_puzzle(label, board):
    print(label)
    for row in board:
        print(row)
    print('\n')

if __name__ == '__main__':
    solution = [[' ', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    test     = [['1', '4', '2'], ['3', '5', '8'], ['6', ' ', '7']]
    # test    = [['5', '2', '8'], ['4', '1', '7'], [' ', '3', '6']]

    print_puzzle('Solução:', solution)
    print_puzzle('Teste:', test)

    print('ALGORITMO BFS - Qtde passos: ', bfs(test, solution))

    print('ALGORITMO GULOSO - Qtde passos: ', greedy(test, solution))

    print('ALGORITMO A ESTRELA (está igual ao guloso) - Qtde passos: ', astar(test, solution))

