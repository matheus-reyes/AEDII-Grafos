# Importa a classe Grafo do documento Grafo.py
from Grafo import Grafo

# Import o pacote csv
import csv

# Importa o módulo time que contém métodos para calcular tempo
import time

print ("Começou!")

#inicia a contagem de tempo de execução
ini = time.time()

# Abre o arquivo e o lê com 'read' depois armazena em entrada_csv Ids_Pessoas
entrada_csv = open('EP4/dados/ids_pessoas.csv', 'r')
# Abre o arquivo e o lê com 'read' depois armazena em entrada_txt Encontros
entrada_txt = open('EP4/dados/gigante1.txt', 'r')

# Pula as primeiras linhas da entrada referentes ao: número de vértices e arestas | nome da coluna 
next(entrada_txt)   
next(entrada_txt)
next(entrada_csv)

# Lê a variável entrada com o método reader e a armazena na variável dados
dados_tabela = csv.reader(entrada_csv)

# Cria as listas para os vértices e arestas
nodes = []
all_edges = []

# For que percorre a variável dados que contém todos os dados da tabela CSV
for dados in dados_tabela:
    nodes.append(dados[0])

# For que percorre a variável linha que contém as arestas e atribui a all_edges
for linha in entrada_txt:
    stripped_line = linha.strip()
    line_list = stripped_line.split()
    all_edges.append(line_list)

# Converte para lista de tuplas
all_edges = [tuple(l) for l in all_edges]

# Inicializa o construtor da classe Grafo e armazena na variável grafo
grafo = Grafo(nodes)

# Cria as arestas
for u,v in all_edges:
    grafo.add_edge(u,v)

# listas de adjacências
adj_list = grafo.print_adj_list()

# Dicionário que armazenará o grafo inteiro, com seus vértices sendo a chave
# e cada lista sendo a lista de adjacência
adjacentes = {}

# percorre o array com a lista de adjacência e preenche o dicionário
for elemento in adj_list:
    adjacentes[elemento[0]] = elemento[1:]

contador1 = 1
contador2 = 1

# Lista que armazena a quantidade de passos de cada conexão
numeroPassos = []

for vertices in nodes:
    for vertices2 in nodes:
        numeroPassos.append(grafo.bfs_shortest_path(adjacentes, str(contador1), str(contador2)))
        contador2 +=1
    contador2 = 1
    contador1 += 1

# Escreve no arquivo de saída as quantidades vértices por componentes linha por linha
with open('EP4/dados/tabela_saida.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter =',')
    a.writerows(map(lambda x: [x], numeroPassos))


# Calcula o tempo de execução ao final do processamento
fim = time.time()

# Fim do Processamento
print ("Acabou!")

# Exibe na tela o tempo de processamento do código
print("Tempo de execuçao (S): ", fim-ini)