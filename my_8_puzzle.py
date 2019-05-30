
class eight_puzzle:
    def __init__ (self, inicial, pai):
        self.tabuleiro = inicial
        self.pai = pai
        self.f = 0
        self.g = 0
        self.h = 0

    # Método de distância Manhattan: Utiliza a distância do incremento com o
    #       valor atual do tabuleiro para o cálculo da distância
    def manhattan(self):
        inc = 0
        h = 0
        for i in range(3):
            for j in range(3):
                h += abs(inc - self.tabuleiro[i][j])
            inc += 1
        return h

    # Método Objetivo: Verifica se o valor atual do tabuleiro é igual ao valor
    #       do incremento para descobrir se o objetivo foi alcançado
    def objetivo(self):
        inc = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != inc:
                    return False
                inc += 1
        return True

    def __eq__(self, outro):
        return self.tabuleiro == outro.tabuleiro

# Método posição zero: Retorna o índice da peça vazia
def posicao_zero(atual):
    return [ ( i, row.index(0)) for i, row in enumerate(atual.tabuleiro) if 0 in row ][0]

# Método move: Move a peça vazia de posição e cria uma árvore de estados
def move(atual, x, y, i, j):
    n_estado = deepcopy(atual)
    n_estado[x][y] = n_estado[i][j]
    n_estado[i][j] = 0
    return eight_puzzle(n_estado, atual)

# Método de movimentação do Tabuleiro: Valida a movimentação no tabuleiro
#       e tenta todas as movimentações possíveis do estado atual
def movimentos(atual):
    pos0 = posicao_zero(atual)
    x, y = pos0[0], pos0[1]

    estados = []

    if x-1 >= 0:
        estados.append(move(atual, x, y, x-1, y))
    if x+1 < 3:
        estados.append(move(atual, x, y, x+1, y)) 
    if y-1 >= 0:
        estados.append(move(atual, x, y, x, y-1)) 
    if y+1 < 3:
        estados.append(move(atual, x, y, x, y+1))
    
    return estados

# Método Dijkstra: Aplica o método de busca Dijkstra
def dijkstra(inicial):
    pass

# Método Gulosa: Aplica o método de busca Gulosa
def gulosa(inicial):
    pass

# Método A estrela: Aplica o método de busca A estrela
def a_estrela(inicial):
    pass

# Método imprime tabuleiro
def imprime_tabuleiro(tabuleiro):
    for row in tabuleiro:
        print(row)
    print('\n')

if __name__ == "__main__":
    inicial = eight_puzzle([[5, 2, 8], [4, 1, 7], [0, 3, 6]], None)
    
    resultadoL = dijkstra(inicial)
    resultadoG = gulosa(inicial)
    resultadoA = a_estrela(inicial)

