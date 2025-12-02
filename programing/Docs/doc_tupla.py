"""
================================================================================
                    GUIA COMPLETO E AVANÇADO SOBRE TUPLAS EM PYTHON
================================================================================

DEFINIÇÃO:
-----------
Uma tupla em Python é uma estrutura de dados IMUTÁVEL que permite armazenar
múltiplos valores em uma única variável. Tuplas são ordenadas, podem conter
elementos duplicados e permitem diferentes tipos de dados, mas NÃO podem ser
modificadas após a criação.

CARACTERÍSTICAS:
- Imutáveis (NÃO podem ser modificadas após criação)
- Ordenadas (mantêm a ordem de inserção)
- Indexadas (acesso por índice começando em 0)
- Permitem duplicatas
- Podem conter diferentes tipos de dados
- Representadas por parênteses ()
- Mais rápidas que listas (devido à imutabilidade)
- Usam menos memória que listas

QUANDO USAR TUPLAS:
- Dados que não devem ser modificados
- Chaves de dicionários (listas não podem ser chaves)
- Retornar múltiplos valores de funções
- Garantir integridade de dados
- Performance em iterações

================================================================================
"""

# ============================================================================
#                           1. CRIANDO TUPLAS
# ============================================================================

# Tupla vazia
tupla_vazia = ()
tupla_vazia2 = tuple()

# Tupla com valores
numeros = (1, 2, 3, 4, 5)
frutas = ("maçã", "banana", "laranja")
mista = (1, "texto", 3.14, True, None)

# Tupla com um elemento (IMPORTANTE: precisa da vírgula!)
tupla_um = (5,)  # Correto
nao_tupla = (5)  # Errado - isso é só um número entre parênteses
print(f"Tipo de (5,): {type(tupla_um)}")    # <class 'tuple'>
print(f"Tipo de (5): {type(nao_tupla)}")    # <class 'int'>

# Tupla sem parênteses (empacotamento)
coordenadas = 10, 20, 30  # Também é uma tupla!
print(f"coordenadas: {coordenadas}, tipo: {type(coordenadas)}")

# Tupla a partir de lista
lista = [1, 2, 3, 4]
tupla_da_lista = tuple(lista)
print(f"Tupla da lista: {tupla_da_lista}")

# Tupla a partir de string
tupla_string = tuple("Python")
print(f"Tupla de string: {tupla_string}")  # ('P', 'y', 't', 'h', 'o', 'n')

# Tupla aninhada
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# Tupla com repetição
zeros = (0,) * 5
print(f"Tupla repetida: {zeros}")  # (0, 0, 0, 0, 0)


# ============================================================================
#                       2. ACESSANDO ELEMENTOS
# ============================================================================

cores = ("vermelho", "azul", "verde", "amarelo", "roxo")

# Acesso por índice (começa em 0)
primeira = cores[0]        # "vermelho"
segunda = cores[1]         # "azul"
print(f"Primeira cor: {primeira}")

# Índices negativos (começam do final)
ultima = cores[-1]         # "roxo"
penultima = cores[-2]      # "amarelo"
print(f"Última cor: {ultima}")

# Fatiamento (slicing) - igual às listas
primeiras_tres = cores[0:3]     # ("vermelho", "azul", "verde")
do_meio = cores[1:4]            # ("azul", "verde", "amarelo")
ultimas_duas = cores[-2:]       # ("amarelo", "roxo")
pular_elementos = cores[::2]    # ("vermelho", "verde", "roxo")
reverso = cores[::-1]           # Inverte a tupla
print(f"Reverso: {reverso}")

# Desempacotamento de tupla
ponto = (10, 20, 30)
x, y, z = ponto
print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=30

# Desempacotamento parcial com *
numeros = (1, 2, 3, 4, 5, 6)
primeiro, segundo, *resto = numeros
print(f"primeiro={primeiro}, segundo={segundo}, resto={resto}")  # resto é lista!

primeiro, *meio, ultimo = numeros
print(f"primeiro={primeiro}, meio={meio}, ultimo={ultimo}")


# ============================================================================
#                    3. MÉTODOS DE TUPLA (APENAS 2!)
# ============================================================================

print("\n=== MÉTODOS DE TUPLA ===\n")

# Tuplas têm apenas 2 métodos (porque são imutáveis):

tupla = (1, 2, 3, 2, 4, 2, 5)

# count() - Conta ocorrências de um valor
qtd_2 = tupla.count(2)
print(f"Quantidade de 2: {qtd_2}")  # 3

qtd_10 = tupla.count(10)
print(f"Quantidade de 10: {qtd_10}")  # 0

# index() - Retorna índice da primeira ocorrência
indice = tupla.index(3)
print(f"Índice de 3: {indice}")  # 2

# index com início e fim
indice_2 = tupla.index(2, 2)  # Busca a partir do índice 2
print(f"Índice de 2 (a partir de 2): {indice_2}")  # 3

# Tratando erro quando elemento não existe
try:
    indice_inexistente = tupla.index(100)
except ValueError:
    print("Elemento 100 não encontrado na tupla")


# ============================================================================
#                    4. OPERAÇÕES COM TUPLAS
# ============================================================================

print("\n=== OPERAÇÕES ===\n")

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação (cria nova tupla)
tupla_concat = tupla1 + tupla2
print(f"Concatenação: {tupla_concat}")  # (1, 2, 3, 4, 5, 6)

# Repetição (cria nova tupla)
tupla_repetida = tupla1 * 3
print(f"Repetição: {tupla_repetida}")  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Comparação
print(f"(1, 2, 3) < (1, 2, 4): {(1, 2, 3) < (1, 2, 4)}")  # True
print(f"(1, 2, 3) == (1, 2, 3): {(1, 2, 3) == (1, 2, 3)}")  # True

# Verificar se elemento existe
print(f"2 in tupla1: {2 in tupla1}")  # True
print(f"10 not in tupla1: {10 not in tupla1}")  # True

# Comprimento
tamanho = len(tupla1)
print(f"Tamanho: {tamanho}")  # 3


# ============================================================================
#                    5. FUNÇÕES BUILT-IN COM TUPLAS
# ============================================================================

print("\n=== FUNÇÕES BUILT-IN ===\n")

numeros = (3, 1, 4, 1, 5, 9, 2, 6)

# Soma
total = sum(numeros)
print(f"Soma: {total}")  # 31

# Máximo e mínimo
maximo = max(numeros)
minimo = min(numeros)
print(f"Máximo: {maximo}, Mínimo: {minimo}")  # 9, 1

# Ordenação (retorna lista!)
ordenados = sorted(numeros)
print(f"Ordenados: {ordenados}, tipo: {type(ordenados)}")  # É lista!

# Reverso (retorna lista!)
reverso = list(reversed(numeros))
print(f"Reverso: {reverso}")

# Conversão para lista
lista = list(numeros)
print(f"Lista: {lista}, tipo: {type(lista)}")

# enumerate
frutas = ("maçã", "banana", "laranja")
with_index = list(enumerate(frutas))
print(f"Com índice: {with_index}")  # [(0, 'maçã'), (1, 'banana'), (2, 'laranja')]

# zip
nomes = ("Ana", "Bruno", "Carlos")
idades = (25, 30, 35)
combinado = tuple(zip(nomes, idades))
print(f"Zip: {combinado}")  # (('Ana', 25), ('Bruno', 30), ('Carlos', 35))

# all e any
todos_positivos = all((1, 2, 3, 4))
print(f"Todos positivos: {todos_positivos}")  # True

algum_zero = any((0, 0, 1, 0))
print(f"Algum diferente de zero: {algum_zero}")  # True


# ============================================================================
#                    6. IMUTABILIDADE - O QUE VOCÊ NÃO PODE FAZER
# ============================================================================

print("\n=== IMUTABILIDADE ===\n")

tupla = (1, 2, 3, 4, 5)

# ❌ NÃO PODE modificar elemento
# tupla[0] = 10  # TypeError: 'tuple' object does not support item assignment

# ❌ NÃO PODE adicionar elemento
# tupla.append(6)  # AttributeError: 'tuple' object has no attribute 'append'

# ❌ NÃO PODE remover elemento
# tupla.remove(3)  # AttributeError: 'tuple' object has no attribute 'remove'
# del tupla[0]     # TypeError: 'tuple' object doesn't support item deletion

# ✅ PODE deletar a tupla inteira
# del tupla
# print(tupla)  # NameError: name 'tupla' is not defined

# ✅ PODE criar nova tupla
tupla_original = (1, 2, 3)
tupla_nova = tupla_original + (4, 5)
print(f"Nova tupla: {tupla_nova}")  # (1, 2, 3, 4, 5)

# ⚠️ ATENÇÃO: Tupla com objetos mutáveis
tupla_com_lista = (1, 2, [3, 4])
tupla_com_lista[2].append(5)  # Isso funciona! A lista dentro pode mudar
print(f"Tupla com lista modificada: {tupla_com_lista}")  # (1, 2, [3, 4, 5])
# A tupla em si não mudou, mas o conteúdo da lista mudou!


# ============================================================================
#                    7. TUPLE COMPREHENSION? NÃO EXISTE!
# ============================================================================

print("\n=== GERADORES VS TUPLAS ===\n")

# ❌ Isso NÃO é tuple comprehension - é um gerador!
gerador = (x**2 for x in range(5))
print(f"Tipo: {type(gerador)}")  # <class 'generator'>

# ✅ Para criar tupla com comprehension, use tuple()
tupla_quadrados = tuple(x**2 for x in range(5))
print(f"Tupla de quadrados: {tupla_quadrados}")  # (0, 1, 4, 9, 16)

# Comparação de memória
import sys
lista = [x for x in range(1000)]
tupla = tuple(x for x in range(1000))
print(f"Tamanho lista: {sys.getsizeof(lista)} bytes")
print(f"Tamanho tupla: {sys.getsizeof(tupla)} bytes")
# Tupla usa menos memória!


# ============================================================================
#                    8. TUPLAS NOMEADAS (namedtuple)
# ============================================================================

print("\n=== NAMEDTUPLE ===\n")

from collections import namedtuple

# Criar classe de tupla nomeada
Ponto = namedtuple('Ponto', ['x', 'y', 'z'])

# Criar instância
p1 = Ponto(10, 20, 30)

# Acessar por nome (mais legível!)
print(f"x: {p1.x}, y: {p1.y}, z: {p1.z}")  # x: 10, y: 20, z: 30

# Ainda funciona como tupla normal
print(f"p1[0]: {p1[0]}")  # 10

# Desempacotamento
x, y, z = p1
print(f"Desempacotado: x={x}, y={y}, z={z}")

# Exemplo prático: Pessoa
Pessoa = namedtuple('Pessoa', ['nome', 'idade', 'cidade'])
pessoa1 = Pessoa('Ana', 25, 'São Paulo')
pessoa2 = Pessoa('Bruno', 30, 'Rio de Janeiro')

print(f"{pessoa1.nome} tem {pessoa1.idade} anos e mora em {pessoa1.cidade}")

# Converter para dicionário
pessoa_dict = pessoa1._asdict()
print(f"Como dicionário: {pessoa_dict}")

# Substituir valores (cria nova instância)
pessoa_modificada = pessoa1._replace(idade=26)
print(f"Idade modificada: {pessoa_modificada}")


# ============================================================================
#                    9. CASOS DE USO PRÁTICOS
# ============================================================================

print("\n=== CASOS DE USO ===\n")

# 1. Retornar múltiplos valores de função
def calcular_estatisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

valores = [10, 20, 30, 40, 50]
minimo, maximo, media = calcular_estatisticas(valores)
print(f"Min: {minimo}, Max: {maximo}, Média: {media}")

# 2. Coordenadas geográficas (não devem mudar)
LOCALIZACAO_SAO_PAULO = (-23.5505, -46.6333)
lat, lon = LOCALIZACAO_SAO_PAULO
print(f"São Paulo: Latitude {lat}, Longitude {lon}")

# 3. Constantes
DIAS_SEMANA = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
CORES_RGB = {
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255)
}
print(f"Vermelho RGB: {CORES_RGB['vermelho']}")

# 4. Chaves de dicionário (listas não podem!)
coordenadas_cidades = {
    (40.7128, -74.0060): 'Nova York',
    (51.5074, -0.1278): 'Londres',
    (-23.5505, -46.6333): 'São Paulo'
}
print(f"Cidade em (40.7128, -74.0060): {coordenadas_cidades[(40.7128, -74.0060)]}")

# 5. Swap de variáveis
a = 10
b = 20
a, b = b, a  # Usa tupla temporária internamente
print(f"Depois do swap: a={a}, b={b}")

# 6. Formato de data/hora
data = (2025, 1, 15)
ano, mes, dia = data
print(f"Data: {dia}/{mes}/{ano}")


# ============================================================================
#                    10. MANIPULAÇÃO AVANÇADA
# ============================================================================

print("\n=== MANIPULAÇÃO AVANÇADA ===\n")

# Filtrar tupla (retorna tupla)
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pares = tuple(x for x in numeros if x % 2 == 0)
print(f"Pares: {pares}")

# Map em tupla
dobrados = tuple(map(lambda x: x * 2, numeros))
print(f"Dobrados: {dobrados}")

# Encontrar índices de valor
tupla = (1, 2, 3, 2, 4, 2, 5)
valor = 2
indices = tuple(i for i, x in enumerate(tupla) if x == valor)
print(f"Índices de {valor}: {indices}")

# Concatenar múltiplas tuplas
tuplas = ((1, 2), (3, 4), (5, 6))
concatenada = tuple(x for tupla in tuplas for x in tupla)
print(f"Concatenada: {concatenada}")

# Rotação
def rotacionar_tupla(tupla, n):
    n = n % len(tupla)
    return tupla[n:] + tupla[:n]

original = (1, 2, 3, 4, 5)
rotacionada = rotacionar_tupla(original, 2)
print(f"Rotacionada: {rotacionada}")

# Intercalar tuplas
tupla1 = (1, 3, 5)
tupla2 = (2, 4, 6)
intercalada = tuple(item for par in zip(tupla1, tupla2) for item in par)
print(f"Intercalada: {intercalada}")


# ============================================================================
#                    11. TUPLAS VS LISTAS - COMPARAÇÃO
# ============================================================================

print("\n=== TUPLAS VS LISTAS ===\n")

import sys
import timeit

# Comparação de tamanho
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
print(f"Tamanho lista: {sys.getsizeof(lista)} bytes")
print(f"Tamanho tupla: {sys.getsizeof(tupla)} bytes")

# Comparação de velocidade - Criação
tempo_lista = timeit.timeit('[1, 2, 3, 4, 5]', number=1000000)
tempo_tupla = timeit.timeit('(1, 2, 3, 4, 5)', number=1000000)
print(f"Tempo criação lista: {tempo_lista:.6f}s")
print(f"Tempo criação tupla: {tempo_tupla:.6f}s")

# Comparação de velocidade - Acesso
tempo_acesso_lista = timeit.timeit('x[2]', setup='x=[1,2,3,4,5]', number=1000000)
tempo_acesso_tupla = timeit.timeit('x[2]', setup='x=(1,2,3,4,5)', number=1000000)
print(f"Tempo acesso lista: {tempo_acesso_lista:.6f}s")
print(f"Tempo acesso tupla: {tempo_acesso_tupla:.6f}s")

print("\n📊 QUANDO USAR CADA UMA:")
print("TUPLA:")
print("  ✅ Dados não devem mudar")
print("  ✅ Performance é importante")
print("  ✅ Usar como chave de dicionário")
print("  ✅ Retornar múltiplos valores de função")
print("  ✅ Garantir integridade de dados")
print("\nLISTA:")
print("  ✅ Dados precisam ser modificados")
print("  ✅ Adicionar/remover elementos frequentemente")
print("  ✅ Precisa de métodos como append, remove, sort")
print("  ✅ Tamanho variável")


# ============================================================================
#                    12. EXEMPLOS PRÁTICOS AVANÇADOS
# ============================================================================

print("\n=== EXEMPLOS PRÁTICOS ===\n")

# 1. Sistema de coordenadas 3D
class Ponto3D:
    def __init__(self, x, y, z):
        self.coordenadas = (x, y, z)  # Imutável!

    def distancia_origem(self):
        x, y, z = self.coordenadas
        return (x**2 + y**2 + z**2) ** 0.5

p = Ponto3D(3, 4, 5)
print(f"Distância da origem: {p.distancia_origem():.2f}")

# 2. Registro de transações
Transacao = namedtuple('Transacao', ['id', 'valor', 'data', 'tipo'])
transacoes = [
    Transacao(1, 100.50, '2025-01-15', 'credito'),
    Transacao(2, -50.00, '2025-01-16', 'debito'),
    Transacao(3, 200.00, '2025-01-17', 'credito')
]

total = sum(t.valor for t in transacoes)
print(f"Saldo total: R$ {total:.2f}")

# 3. Cache de resultados (tuplas como chaves)
cache_fibonacci = {}

def fibonacci_cache(n):
    if n in cache_fibonacci:
        return cache_fibonacci[n]

    if n <= 1:
        return n

    resultado = fibonacci_cache(n-1) + fibonacci_cache(n-2)
    cache_fibonacci[n] = resultado
    return resultado

print(f"Fibonacci(10): {fibonacci_cache(10)}")

# 4. Configurações imutáveis
CONFIG = (
    ('host', 'localhost'),
    ('port', 8080),
    ('debug', True),
    ('timeout', 30)
)

config_dict = dict(CONFIG)
print(f"Configuração: {config_dict}")

# 5. Matriz de dados (tupla de tuplas)
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Transpor
transposta = tuple(zip(*matriz))
print(f"Matriz original: {matriz}")
print(f"Matriz transposta: {transposta}")

# Soma das diagonais
diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
diagonal_secundaria = sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))
print(f"Diagonal principal: {diagonal_principal}")
print(f"Diagonal secundária: {diagonal_secundaria}")


# ============================================================================
#                    13. BOAS PRÁTICAS COM TUPLAS
# ============================================================================

print("\n=== BOAS PRÁTICAS ===\n")

# ✅ Use tuplas para dados que não devem mudar
COORDENADAS_FIXAS = (10.5, 20.3)

# ✅ Use namedtuple para clareza
from collections import namedtuple
Usuario = namedtuple('Usuario', ['id', 'nome', 'email'])
usuario = Usuario(1, 'Ana', 'ana@email.com')
print(f"Nome: {usuario.nome}")  # Mais claro que usuario[1]

# ✅ Desempacote tuplas para código mais legível
def get_coordenadas():
    return (10, 20)

x, y = get_coordenadas()  # Melhor que acessar por índice

# ✅ Use tuplas para retornar múltiplos valores
def dividir_com_resto(a, b):
    return a // b, a % b

quociente, resto = dividir_com_resto(17, 5)
print(f"17 ÷ 5 = {quociente} com resto {resto}")

# ✅ Use tuplas como chaves de dicionário para dados compostos
cache = {
    ('funcao1', 10): 'resultado1',
    ('funcao2', 20): 'resultado2'
}

# ❌ Evite tuplas muito longas - use namedtuple ou classe
# tupla_ruim = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Difícil de entender

# ✅ Melhor
Dados = namedtuple('Dados', ['campo1', 'campo2', 'campo3'])

# ✅ Use typing para documentar
from typing import Tuple

def processar() -> Tuple[int, str, bool]:
    return 42, "sucesso", True


# ============================================================================
#                    14. CONVERSÕES E INTEROPERABILIDADE
# ============================================================================

print("\n=== CONVERSÕES ===\n")

# Tupla ↔ Lista
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
nova_tupla = tuple(lista)
print(f"Tupla → Lista → Tupla: {nova_tupla}")

# Tupla ↔ Set
tupla_com_dup = (1, 2, 2, 3, 3, 3)
set_unico = set(tupla_com_dup)
tupla_unica = tuple(set_unico)
print(f"Removendo duplicatas: {tupla_unica}")

# Tupla ↔ String
tupla_chars = ('P', 'y', 't', 'h', 'o', 'n')
string = ''.join(tupla_chars)
print(f"Tupla → String: {string}")

string2 = "Hello"
tupla_string = tuple(string2)
print(f"String → Tupla: {tupla_string}")

# Tupla ↔ Dicionário
tupla_pares = (('a', 1), ('b', 2), ('c', 3))
dicionario = dict(tupla_pares)
print(f"Tupla → Dict: {dicionario}")

dict_original = {'x': 10, 'y': 20}
tupla_items = tuple(dict_original.items())
print(f"Dict → Tupla: {tupla_items}")


# ============================================================================
#                    15. TRUQUES E TÉCNICAS AVANÇADAS
# ============================================================================

print("\n=== TRUQUES AVANÇADOS ===\n")

# 1. Singleton tupla (garantir instância única)
class Configuracao:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = ('localhost', 8080, True)
        return cls._instance

config1 = Configuracao()
config2 = Configuracao()
print(f"São a mesma instância?: {config1 is config2}")

# 2. Validação de tupla
def validar_ponto_3d(ponto):
    if not isinstance(ponto, tuple):
        raise TypeError("Deve ser uma tupla")
    if len(ponto) != 3:
        raise ValueError("Deve ter 3 coordenadas")
    if not all(isinstance(x, (int, float)) for x in ponto):
        raise ValueError("Coordenadas devem ser números")
    return True

try:
    validar_ponto_3d((10, 20, 30))
    print("Ponto válido!")
except (TypeError, ValueError) as e:
    print(f"Erro: {e}")

# 3. Tupla como estado imutável
class EstadoJogo:
    def __init__(self):
        self._estado = (0, 0, 100)  # (x, y, vida)

    def mover(self, dx, dy):
        x, y, vida = self._estado
        self._estado = (x + dx, y + dy, vida)
        return self._estado

    def receber_dano(self, dano):
        x, y, vida = self._estado
        self._estado = (x, y, max(0, vida - dano))
        return self._estado

jogo = EstadoJogo()
print(f"Posição inicial: {jogo._estado}")
jogo.mover(5, 10)
print(f"Após mover: {jogo._estado}")

# 4. Memoization com tuplas
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:  # args já é uma tupla!
            return cache[args]
        resultado = func(*args)
        cache[args] = resultado
        return resultado
    return wrapper

@memoize
def soma_complexa(a, b, c):
    print(f"Calculando {a} + {b} + {c}")
    return a + b + c

print(soma_complexa(1, 2, 3))  # Calcula
print(soma_complexa(1, 2, 3))  # Usa cache


print("\n" + "="*80)
print("FIM DO GUIA COMPLETO SOBRE TUPLAS EM PYTHON")
print("="*80)
print("\n💡 RESUMO FINAL:")
print("• Tuplas são IMUTÁVEIS - não podem ser modificadas")
print("• Mais rápidas e usam menos memória que listas")
print("• Perfeitas para dados constantes e chaves de dicionários")
print("• Use namedtuple para código mais legível")
print("• Ideais para retornar múltiplos valores de funções")
print("="*80)
