"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""


def calculadora():
    num1 = int(input('Digite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))
    operador = int(input('Digite 1 para Soma, 2 para subtração, 3 para divisão e 4 para multiplicação'))
    if operador == 1:
        print(f'O resultado de {num1} + {num2} é igual à: {num1 + num2}')
    elif operador == 2:
        print(f'O resultado de {num1} - {num2} é igual à: {num1 - num2}')
    elif operador == 3:
        print(f'O resultado de {num1} / {num2} é igual à: {num1 / num2}')
    elif operador == 4:
        print(f'O resultado de {num1} * {num2} é igual à: {num1 * num2}')
    else:
        print('Você digitou um código inválido, gentileza repetir a operação.')
calculadora()
