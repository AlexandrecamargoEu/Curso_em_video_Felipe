"""🚗 Exercício: Estruturas Condicionais — If Encadeado com Validação de Dados

Crie um programa que ajude uma locadora a calcular o valor total de uma locação de veículo. O programa deve solicitar ao usuário:

Tipo do veículo (E para Econômico, S para SUV)

Quantidade de dias alugados

Quantidade de quilômetros rodados

O cálculo deve seguir estas regras:

Valide as entradas:

Se o tipo não for E nem S, mostre “Tipo de veículo inválido.”

Se os dias ou km forem menores ou iguais a 0, mostre “Valores inválidos.” 👉 Somente se os dados forem válidos, prossiga para o cálculo.

Para veículos do tipo Econômico (E):

Diária: R$ 90

Até 100 km rodados → R$ 0,50 por km

Acima de 100 km → R$ 0,40 por km (desconto progressivo)

Para veículos do tipo SUV (S):

Diária: R$ 150

Até 200 km rodados → R$ 0,70 por km

Acima de 200 km → R$ 0,60 por km

Ao final, mostre:

O tipo de veículo

Total de dias e quilômetros

Valor total da locação (diárias + km)"""

tipoveiculo = input("Digite o tipo de veiculo E para Econômico, S para SUV:")

qtydias = int(input("Digite a quantidade de dias:"))

kmrodados = float(input("Digite a estimativa de Km rodados:"))

diaria_e = 90

diaria_s = 150

if tipoveiculo != "E" and tipoveiculo != "S":
  print("Tipo de veiculo invalido!")
elif qtydias <= 0 or kmrodados <= 0:
  print("Valores inválidos.")
else:
  if tipoveiculo == "E" and kmrodados <= 100:
    kmprice = kmrodados*0.50
    print(f"Contrato Efetuado\nTipo de veiculo:{tipoveiculo}\nTotal de dias Alugados:{qtydias}\nQuilometros contratados:{kmrodados}\nValor total da alocacao:{(diaria_e*qtydias) + kmprice}")
  elif tipoveiculo == "E" and kmrodados > 100:
    kmpricef = 100*0.50
    kmprice = (kmrodados-100)*0.40
    print(f"Contrato Efetuado\nTipo de veiculo:{tipoveiculo}\nTotal de dias Alugados:{qtydias}\nQuilometros contratados:{kmrodados}\nValor total da alocacao:{(diaria_e*qtydias) + (kmprice+kmpricef)}")

  elif tipoveiculo == "S" and kmrodados <= 200:
    kmprice = kmrodados*0.70
    print(f"Contrato Efetuado\nTipo de veiculo:{tipoveiculo}\nTotal de dias Alugados:{qtydias}\nQuilometros contratados:{kmrodados}\nValor total da alocacao:{(diaria_s*qtydias) + kmprice}")
  elif tipoveiculo == "S" and kmrodados > 200:
    kmpricef = 200*0.70
    kmprice = (kmrodados-200)*0.60
    print(f"Contrato Efetuado\nTipo de veiculo:{tipoveiculo}\nTotal de dias Alugados:{qtydias}\nQuilometros contratados:{kmrodados}\nValor total da alocacao:{(diaria_s*qtydias) + (kmprice+kmpricef)}")


