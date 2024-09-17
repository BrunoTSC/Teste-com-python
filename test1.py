'''Técnica:

1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA? 91'''

indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k
    print(soma)

'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''
def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia [-2]
        sequencia.append(proximo)
    return sequencia

def verificação(num):
    sequencia = fibonacci(num)
    if num in sequencia:
        print (f'O número {num} pertence à sequência de Fibonacci.')

    else:
        print(f'O número {num} não pertence à sequência de Fibonacci.')

num = int(input('Digite um número: '))
verificação(num)

'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json

with open ('dados.json', 'r') as file:
    dados_faturamento = json.load(file)

def calc_faturamento(faturamento):
    valores = [dia['valor'] for dia in faturamento if dia ['valor'] > 0]
    valor_menor = min(valores)
    valor_maior = max(valores)
    media_faturamento = sum(valores) / len(valores)

    dias_acima_media = len ([valor for valor in valores if valor > media_faturamento])

    print(f'Menor valor do faturamento:{valor_menor}')
    print(f'Maior valor do faturamento:{valor_maior}')
    #print(media_faturamento) usado para confirmar a média e contar os dias.
    print(f'Quantidade de dias com o faturamento acima da média:{dias_acima_media}')

calc_faturamento(dados_faturamento)

'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
'''
#Colocando os valores dentro de um dicionário:
dici_faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(dici_faturamento.values())

for estado, valor in dici_faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f'{estado} teve {percentual:.2f}% do faturamento total.')



'''5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;'''

def inverter_carac(c):
    return c[::-1] #inversão

string = str(input("Informe a string que deseja inverter: "))
print(f'String invertida: {inverter_carac(string)}')