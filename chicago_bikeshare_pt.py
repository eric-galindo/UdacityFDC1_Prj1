# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:", len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: \n", data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: \n", data_list[1])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

for i in range(len(data_list)):
    if i < 20:
        print(data_list[i])
    else:
        break

# Nós podemos acessar as features(colunas/campos) pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for i in range(len(data_list)):
    if i < 20:
        print(data_list[i][6])
    else:
        break
# Ótimo! Nós podemos pegar as linhas(samples/registros) iterando com um for, e
# as colunas(features/campos) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os
# gêneros

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em
# outra lista, na mesma ordem'''
def column_to_list(data, index):
    """
    Extrai coluna[index] de lista[data] previamente selecionada
    Argumentos:
      data: Lista multi-feature que contém a coluna a ser extraída
      index: Índice da coluna a ser extraída
    Retorna:
      A lista determinada em index sem conversão de tipos do objeto.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature
    # pelo seu índice e dar append para uma lista
    for i in range(len(data)):
        column_list.append(data[i][index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros
# 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos)
# e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
not_informed = 0

for i in range(len(data_list)): # Conta male e female
    if data_list[i][6] == 'Male':
        male+=1
    elif data_list[i][6] == 'Female':
        female+=1
    else:
        not_informed+=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: {} \nFemininos: {}".format(male, female))
print("Não informados: {} \nTotal lidos: {}".format(not_informed, male + female
+ not_informed))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10,
# 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0

    for i in range(len(data_list)): # Conta male e female
        if data_list[i][6] == 'Male':
            male+=1
        elif data_list[i][6] == 'Female':
            female+=1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero
# como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
    Determina qual o gênero de maior ocorrência
    Argumentos:
      data_list: Lista multi-feature que deve conter na feature de indice 6 o gênero
    Retorna:
      Texto (string) que identifica o gênero de maior frequência ou se são de mesma ocorrência.
    """
    answer = ""
    male = 0
    female = 0

    for i in range(len(data_list)): # Conta male e female
        if data_list[i][6] == 'Male':
            male+=1
        elif data_list[i][6] == 'Female':
            female+=1

    if male > female: # Analisa qual variável é maior e retorna como str(ptbr)
        answer = 'Masculino'
    elif female > male:
        answer = 'Feminino'
    else:
        answer = 'Igual'

    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Masculino", "Feminino"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda
# está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_types(data_list):
    """
    Conta ocorrência de cada tipo de types
    Argumentos:
      data_list: Lista multi-feature que deve conter na feature de indice 5 o types
    Retorna:
      Valor de ocorrência (integer) de cada um dos types.
    """
    subscriber = 0
    customer = 0
    dependent = 0

    for i in range(len(data_list)): # Conta male e female
        if data_list[i][5] == 'Subscriber':
            subscriber+=1
        elif data_list[i][5] == 'Customer':
            customer+=1
        elif data_list[i][5] == 'Dependent':
            dependent+=1

    return [subscriber, customer, dependent]

subscriber, customer, dependent = count_types(data_list)

print("Dados para validação de legendas:",
"Subscriber({}), Customer ({}) e Dependent ({}).".format(subscriber, customer, dependent))

# gender_list = column_to_list(data_list, -2) # Não preciso dessa informação
# para gerar gráfico!
types = ["Subscriber", "Customer","Dependent"]
quantity = count_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos')
plt.show(block=True)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Pois nem todas as samples (linhas/registros) possuem o feature genre informados.\n Do total de {} samples, {} não estão informados no arquivo {}. Daí, male ({}) + female ({}) resulta em {}, que é diferente da quantidade de samples da data_list ({}).".format(male + female + not_informed, not_informed, "'chicago.csv'", male, female, male + female, len(data_list))
print("Resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos
# tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

total_trip = 0.
count_trip = 0
trip_duration_list_int = []
min_trip = int(trip_duration_list[0])
max_trip = int(trip_duration_list[0])

for i in trip_duration_list:
    i = int(i)
    trip_duration_list_int.append(i)
    if i < min_trip: # Cond. para registrar Min
        min_trip = i
    if i > max_trip: # Cond. para registrar Max
        max_trip = i
    total_trip += i
    count_trip += 1

mean_trip = total_trip / count_trip # Calcula Média
tdlo = sorted(trip_duration_list_int)

if len(tdlo) % 2 == 0: # Registra a Mediana se for par (média entre 2 números centrais)
    index1 = int(len(tdlo)/2) - 1
    index2 = int(len(tdlo)/2)
    median_trip = (tdlo[index1] + tdlo[index2]) / 2
else: # Ou calcula a Mediana se for impar
    median_trip = tdlo[int(len(tdlo)/2)]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média e mediana")
print("Min: {}, Max: {}, Média: {}, Mediana: {}".format(min_trip, max_trip, mean_trip, median_trip))

# Agradecimentos à @luizabissoli pela ajuda ao @rodrigo.will no link https://discussions.udacity.com/t/projeto-1-tarefa-9-calculo-da-mediana/767296. Tive dificuldades em calcular a mediana pois estava usando a função sort() no trip_duration_list enquanto string. Efetuei a conversão dos dados em int, dei append() em uma nova variável (linha 268) conforme mensionado pela instrutora e consegui completar a tarefa 9.

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a
# start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

user_types_list = []

for i in range(len(data_list)):
    user_types_list.append(data_list[i][3])

user_types = set(user_types_list)

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os
# parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
'''
Função de exemplo com anotações.
Argumentos:
  param1: O primeiro parâmetro.
  param2: O segundo parâmetro.
Retorna:
  Uma lista de valores x.
'''

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes" # Definetelly :D

def count_items(column_list):
    """
    Conta diferentes samples dentro da lista unidimensional
    Argumentos:
      column_list: Lista unidimensional que contém a coluna a ser analisada
    Retorna:
      item_types: Lista dos itens diferentes (1 ocorrência cada)
      count_items: Lista da frequência de cada item, de acordo com a lista item_types (similar a estrutura csv)
    """
    item_types = []
    count_items = []

    for i in column_list:
        if i in item_types:
            count_items[item_types.index(i)] += 1
        else:
            item_types.append(i)
            count_items.append(1)

    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
