"""
================================================================================
                    GUIA COMPLETO E AVANÇADO SOBRE LISTAS EM PYTHON
================================================================================

DEFINIÇÃO:
-----------
Uma lista em Python é uma estrutura de dados MUTÁVEL que permite armazenar
múltiplos valores em uma única variável. As listas são ordenadas, podem conter
elementos duplicados e permitem diferentes tipos de dados.

CARACTERÍSTICAS:
- Mutáveis (podem ser modificadas após criação)
- Ordenadas (mantêm a ordem de inserção)
- Indexadas (acesso por índice começando em 0)
- Permitem duplicatas
- Podem conter diferentes tipos de dados
- Representadas por colchetes []

================================================================================
"""

# ============================================================================
#                           1. CRIANDO LISTAS
# ============================================================================

# Lista vazia
lista_vazia = []
lista_vazia2 = list()

# Lista com valores
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
mista = [1, "texto", 3.14, True, None]

# Lista com repetição
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# Lista a partir de range
numeros_range = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista aninhada (matriz)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# ============================================================================
#                       2. ACESSANDO ELEMENTOS
# ============================================================================

cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]

# Acesso por índice (começa em 0)
primeira = cores[0]        # "vermelho"
segunda = cores[1]         # "azul"

# Índices negativos (começam do final)
ultima = cores[-1]         # "roxo"
penultima = cores[-2]      # "amarelo"

# Fatiamento (slicing)
primeiras_tres = cores[0:3]     # ["vermelho", "azul", "verde"]
do_meio = cores[1:4]            # ["azul", "verde", "amarelo"]
ultimas_duas = cores[-2:]       # ["amarelo", "roxo"]
pular_elementos = cores[::2]    # ["vermelho", "verde", "roxo"]
reverso = cores[::-1]           # Inverte a lista


# ============================================================================
#                    3. MÉTODOS BÁSICOS DE MODIFICAÇÃO
# ============================================================================

print("\n=== MÉTODOS BÁSICOS ===\n")

# append() - Adiciona elemento no final
lista1 = [1, 2, 3]
lista1.append(4)
print(f"append(4): {lista1}")  # [1, 2, 3, 4]

# insert() - Adiciona elemento em posição específica
lista1.insert(0, 0)  # Insere 0 na posição 0
print(f"insert(0, 0): {lista1}")  # [0, 1, 2, 3, 4]

# extend() - Adiciona múltiplos elementos
lista1.extend([5, 6, 7])
print(f"extend([5, 6, 7]): {lista1}")  # [0, 1, 2, 3, 4, 5, 6, 7]

# remove() - Remove primeira ocorrência do valor
lista2 = [1, 2, 3, 2, 4]
lista2.remove(2)  # Remove primeiro 2
print(f"remove(2): {lista2}")  # [1, 3, 2, 4]

# pop() - Remove e retorna elemento por índice
lista3 = [10, 20, 30, 40]
removido = lista3.pop()  # Remove último
print(f"pop(): removido={removido}, lista={lista3}")  # removido=40, lista=[10, 20, 30]

removido2 = lista3.pop(0)  # Remove índice 0
print(f"pop(0): removido={removido2}, lista={lista3}")  # removido=10, lista=[20, 30]

# clear() - Remove todos os elementos
lista4 = [1, 2, 3]
lista4.clear()
print(f"clear(): {lista4}")  # []

# del - Deleta elementos ou a lista inteira
lista5 = [1, 2, 3, 4, 5]
del lista5[0]  # Remove índice 0
print(f"del lista5[0]: {lista5}")  # [2, 3, 4, 5]

del lista5[1:3]  # Remove slice
print(f"del lista5[1:3]: {lista5}")  # [2, 5]


# ============================================================================
#                    4. MÉTODOS DE CONSULTA E ORGANIZAÇÃO
# ============================================================================

print("\n=== MÉTODOS DE CONSULTA ===\n")

numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# count() - Conta ocorrências
qtd = numeros.count(1)
print(f"count(1): {qtd}")  # 2

# index() - Retorna índice da primeira ocorrência
indice = numeros.index(4)
print(f"index(4): {indice}")  # 2

# index com início e fim
indice2 = numeros.index(1, 2)  # Busca a partir do índice 2
print(f"index(1, 2): {indice2}")  # 3

# sort() - Ordena a lista in-place (modifica a original)
numeros_copia = numeros.copy()
numeros_copia.sort()
print(f"sort(): {numeros_copia}")  # [1, 1, 2, 3, 4, 5, 6, 9]

numeros_copia.sort(reverse=True)  # Ordem decrescente
print(f"sort(reverse=True): {numeros_copia}")  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - Retorna nova lista ordenada (não modifica original)
numeros_ordenados = sorted(numeros)
print(f"sorted(): {numeros_ordenados}")  # [1, 1, 2, 3, 4, 5, 6, 9]
print(f"Original: {numeros}")  # [3, 1, 4, 1, 5, 9, 2, 6]

# reverse() - Inverte a lista in-place
numeros_rev = [1, 2, 3, 4, 5]
numeros_rev.reverse()
print(f"reverse(): {numeros_rev}")  # [5, 4, 3, 2, 1]

# copy() - Cria cópia superficial
original = [1, 2, 3]
copia = original.copy()
copia.append(4)
print(f"Original: {original}, Cópia: {copia}")  # Original: [1, 2, 3], Cópia: [1, 2, 3, 4]


# ============================================================================
#                    5. OPERAÇÕES MATEMÁTICAS E ESTATÍSTICAS
# ============================================================================

print("\n=== OPERAÇÕES MATEMÁTICAS ===\n")

valores = [10, 20, 30, 40, 50]

# Soma de todos os elementos
total = sum(valores)
print(f"sum(): {total}")  # 150

# Valor máximo e mínimo
maximo = max(valores)
minimo = min(valores)
print(f"max(): {maximo}, min(): {minimo}")  # max(): 50, min(): 10

# Comprimento da lista
tamanho = len(valores)
print(f"len(): {tamanho}")  # 5

# Média
media = sum(valores) / len(valores)
print(f"Média: {media}")  # 30.0

# Produto de todos os elementos
from functools import reduce
import operator
produto = reduce(operator.mul, valores)
print(f"Produto: {produto}")  # 12000000

# Soma cumulativa
def soma_cumulativa(lista):
    resultado = []
    total = 0
    for num in lista:
        total += num
        resultado.append(total)
    return resultado

print(f"Soma cumulativa: {soma_cumulativa(valores)}")  # [10, 30, 60, 100, 150]


# ============================================================================
#                    6. LIST COMPREHENSION (COMPREENSÃO DE LISTAS)
# ============================================================================

print("\n=== LIST COMPREHENSION ===\n")

# Sintaxe básica: [expressão for item in iterável]
quadrados = [x**2 for x in range(1, 6)]
print(f"Quadrados: {quadrados}")  # [1, 4, 9, 16, 25]

# Com condicional: [expressão for item in iterável if condição]
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Pares: {pares}")  # [2, 4, 6, 8, 10]

# If-else: [expressão_if if condição else expressão_else for item in iterável]
classificacao = ["par" if x % 2 == 0 else "ímpar" for x in range(1, 6)]
print(f"Classificação: {classificacao}")  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']

# Múltiplos loops
combinacoes = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(f"Combinações: {combinacoes}")  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# Achatar lista aninhada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
achatada = [num for linha in matriz for num in linha]
print(f"Achatada: {achatada}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Aplicar função
palavras = ["python", "lista", "programação"]
maiusculas = [p.upper() for p in palavras]
print(f"Maiúsculas: {maiusculas}")  # ['PYTHON', 'LISTA', 'PROGRAMAÇÃO']


# ============================================================================
#                    7. MÉTODOS AVANÇADOS COM MAP, FILTER, ZIP
# ============================================================================

print("\n=== MÉTODOS AVANÇADOS ===\n")

# map() - Aplica função a cada elemento
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(f"map (dobro): {dobrados}")  # [2, 4, 6, 8, 10]

# Múltiplas listas com map
a = [1, 2, 3]
b = [4, 5, 6]
soma_elementos = list(map(lambda x, y: x + y, a, b))
print(f"map (soma): {soma_elementos}")  # [5, 7, 9]

# filter() - Filtra elementos baseado em condição
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maiores_que_5 = list(filter(lambda x: x > 5, numeros))
print(f"filter (>5): {maiores_que_5}")  # [6, 7, 8, 9, 10]

# zip() - Combina múltiplas listas
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 35]
cidades = ["SP", "RJ", "MG"]
combinado = list(zip(nomes, idades, cidades))
print(f"zip: {combinado}")  # [('Ana', 25, 'SP'), ('Bruno', 30, 'RJ'), ('Carlos', 35, 'MG')]

# Descompactar zip
lista1, lista2 = zip(*[(1, 'a'), (2, 'b'), (3, 'c')])
print(f"Descompactar: {list(lista1)}, {list(lista2)}")  # [1, 2, 3], ['a', 'b', 'c']

# enumerate() - Adiciona índice aos elementos
frutas = ["maçã", "banana", "laranja"]
with_index = list(enumerate(frutas))
print(f"enumerate: {with_index}")  # [(0, 'maçã'), (1, 'banana'), (2, 'laranja')]

# enumerate com índice inicial diferente
with_index2 = list(enumerate(frutas, start=1))
print(f"enumerate(start=1): {with_index2}")  # [(1, 'maçã'), (2, 'banana'), (3, 'laranja')]


# ============================================================================
#                    8. OPERAÇÕES COM ALL, ANY, SUM
# ============================================================================

print("\n=== ALL, ANY, SUM ===\n")

# all() - Retorna True se todos os elementos são True
todos_positivos = all([5, 10, 15, 20])
print(f"all([5, 10, 15, 20]): {todos_positivos}")  # True

todos_positivos2 = all([5, 10, 0, 20])
print(f"all([5, 10, 0, 20]): {todos_positivos2}")  # False (0 é False)

# any() - Retorna True se algum elemento é True
algum_positivo = any([0, 0, 5, 0])
print(f"any([0, 0, 5, 0]): {algum_positivo}")  # True

# Verificar se todos são pares
numeros = [2, 4, 6, 8]
todos_pares = all(x % 2 == 0 for x in numeros)
print(f"Todos pares?: {todos_pares}")  # True

# Verificar se algum é negativo
numeros2 = [5, 10, -3, 20]
tem_negativo = any(x < 0 for x in numeros2)
print(f"Tem negativo?: {tem_negativo}")  # True


# ============================================================================
#                    9. BUSCA E VERIFICAÇÃO
# ============================================================================

print("\n=== BUSCA E VERIFICAÇÃO ===\n")

lista = [10, 20, 30, 40, 50]

# Verificar se elemento existe
existe = 30 in lista
print(f"30 in lista: {existe}")  # True

nao_existe = 100 not in lista
print(f"100 not in lista: {nao_existe}")  # True

# Encontrar índice de máximo e mínimo
numeros = [3, 7, 2, 9, 1, 5]
indice_max = numeros.index(max(numeros))
indice_min = numeros.index(min(numeros))
print(f"Índice do máximo: {indice_max}, Índice do mínimo: {indice_min}")  # 3, 4

# Encontrar todos os índices de um valor
lista_dup = [1, 2, 3, 2, 4, 2, 5]
valor = 2
indices = [i for i, x in enumerate(lista_dup) if x == valor]
print(f"Índices de {valor}: {indices}")  # [1, 3, 5]


# ============================================================================
#                    10. ORDENAÇÃO AVANÇADA
# ============================================================================

print("\n=== ORDENAÇÃO AVANÇADA ===\n")

# Ordenar por comprimento
palavras = ["python", "é", "incrível", "e", "poderoso"]
por_tamanho = sorted(palavras, key=len)
print(f"Ordenar por tamanho: {por_tamanho}")  # ['é', 'e', 'python', 'incrível', 'poderoso']

# Ordenar lista de tuplas
alunos = [("Ana", 8.5), ("Bruno", 9.0), ("Carlos", 7.5)]
por_nota = sorted(alunos, key=lambda x: x[1], reverse=True)
print(f"Ordenar por nota: {por_nota}")  # [('Bruno', 9.0), ('Ana', 8.5), ('Carlos', 7.5)]

# Ordenar dicionários em lista
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 20}
]
por_idade = sorted(pessoas, key=lambda x: x["idade"])
print(f"Ordenar por idade: {por_idade}")

# Ordenação customizada
def criterio_custom(x):
    return (x % 2 == 0, x)  # Ímpares primeiro, depois valor

numeros = [1, 2, 3, 4, 5, 6]
ordenado_custom = sorted(numeros, key=criterio_custom)
print(f"Ordenação customizada: {ordenado_custom}")  # [1, 3, 5, 2, 4, 6]


# ============================================================================
#                    11. MANIPULAÇÃO DE LISTAS ANINHADAS
# ============================================================================

print("\n=== LISTAS ANINHADAS ===\n")

# Criar matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Acessar elementos
elemento = matriz[1][2]  # Linha 1, Coluna 2
print(f"Elemento [1][2]: {elemento}")  # 6

# Transpor matriz
transposta = [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]
print(f"Transposta: {transposta}")  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Soma de cada linha
somas_linhas = [sum(linha) for linha in matriz]
print(f"Soma das linhas: {somas_linhas}")  # [6, 15, 24]

# Achatar lista aninhada profunda
def achatar(lista):
    resultado = []
    for item in lista:
        if isinstance(item, list):
            resultado.extend(achatar(item))
        else:
            resultado.append(item)
    return resultado

aninhada = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
achatada = achatar(aninhada)
print(f"Achatada: {achatada}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ============================================================================
#                    12. REMOÇÃO DE DUPLICATAS
# ============================================================================

print("\n=== REMOÇÃO DE DUPLICATAS ===\n")

lista_dup = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# Usando set (não mantém ordem)
sem_dup_set = list(set(lista_dup))
print(f"Sem duplicatas (set): {sem_dup_set}")  # Ordem não garantida

# Mantendo ordem
sem_dup_ordem = []
for item in lista_dup:
    if item not in sem_dup_ordem:
        sem_dup_ordem.append(item)
print(f"Sem duplicatas (ordem): {sem_dup_ordem}")  # [1, 2, 3, 4, 5]

# Usando dict.fromkeys (Python 3.7+)
sem_dup_dict = list(dict.fromkeys(lista_dup))
print(f"Sem duplicatas (dict): {sem_dup_dict}")  # [1, 2, 3, 4, 5]


# ============================================================================
#                    13. PARTICIONAMENTO E AGRUPAMENTO
# ============================================================================

print("\n=== PARTICIONAMENTO ===\n")

# Dividir lista em chunks
def dividir_chunks(lista, tamanho):
    return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunks = dividir_chunks(numeros, 3)
print(f"Chunks de 3: {chunks}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Separar pares e ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print(f"Pares: {pares}, Ímpares: {impares}")

# Agrupar por condição
from itertools import groupby
numeros = [1, 1, 2, 2, 2, 3, 4, 4, 5]
agrupados = {k: list(g) for k, g in groupby(numeros)}
print(f"Agrupados: {agrupados}")


# ============================================================================
#                    14. EXEMPLOS PRÁTICOS AVANÇADOS
# ============================================================================

print("\n=== EXEMPLOS PRÁTICOS ===\n")

# 1. Encontrar elementos únicos entre duas listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
unicos_lista1 = [x for x in lista1 if x not in lista2]
unicos_lista2 = [x for x in lista2 if x not in lista1]
print(f"Únicos em lista1: {unicos_lista1}")  # [1, 2, 3]
print(f"Únicos em lista2: {unicos_lista2}")  # [6, 7, 8]

# 2. Rotacionar lista
def rotacionar(lista, n):
    n = n % len(lista)
    return lista[n:] + lista[:n]

numeros = [1, 2, 3, 4, 5]
rotacionado = rotacionar(numeros, 2)
print(f"Rotacionado 2 posições: {rotacionado}")  # [3, 4, 5, 1, 2]

# 3. Encontrar pares de elementos que somam valor específico
def pares_soma(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

numeros = [1, 2, 3, 4, 5, 6]
pares_10 = pares_soma(numeros, 7)
print(f"Pares que somam 7: {pares_10}")  # [(1, 6), (2, 5), (3, 4)]

# 4. Calcular média móvel
def media_movel(lista, janela):
    return [sum(lista[i:i+janela])/janela for i in range(len(lista)-janela+1)]

valores = [10, 20, 30, 40, 50, 60]
medias = media_movel(valores, 3)
print(f"Média móvel (janela 3): {medias}")  # [20.0, 30.0, 40.0, 50.0]

# 5. Intercalar duas listas
lista_a = [1, 3, 5]
lista_b = [2, 4, 6]
intercalada = [item for par in zip(lista_a, lista_b) for item in par]
print(f"Intercalada: {intercalada}")  # [1, 2, 3, 4, 5, 6]


# ============================================================================
#                    15. PERFORMANCE E BOAS PRÁTICAS
# ============================================================================

print("\n=== BOAS PRÁTICAS ===\n")

# ❌ EVITAR: Modificar lista durante iteração
lista = [1, 2, 3, 4, 5]
# for item in lista:
#     if item % 2 == 0:
#         lista.remove(item)  # PERIGOSO!

# ✅ FAZER: Criar nova lista
lista = [1, 2, 3, 4, 5]
nova_lista = [item for item in lista if item % 2 != 0]
print(f"Lista filtrada: {nova_lista}")

# ✅ List comprehension é mais rápido que loop
# Mais lento
quadrados1 = []
for x in range(10):
    quadrados1.append(x**2)

# Mais rápido
quadrados2 = [x**2 for x in range(10)]

# ✅ Usar 'in' para verificar existência (não index com try/except)
lista = [1, 2, 3, 4, 5]
if 3 in lista:  # Rápido e limpo
    print("3 está na lista")

# ✅ Usar extend() ao invés de append() em loop
lista = [1, 2, 3]
novos = [4, 5, 6]
lista.extend(novos)  # Melhor que append em loop

print("\n" + "="*80)
print("FIM DO GUIA COMPLETO SOBRE LISTAS EM PYTHON")
print("="*80)
