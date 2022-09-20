"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.
"""


def calculadora(num1, num2, op,):
    if op == 1:
        res = num1 + num2
        print(f'O resultado de {num1} + {num2} é igual à: {res}')
    elif op == 2:
        res = num1 - num2
        print(f'O resultado de {num1} - {num2} é igual à: {res}')
    elif op == 3:
        res = num1 * num2
        print(f'O resultado de {num1} * {num2} é igual à: {res}')
    elif op == 4:
        res = num1 / num2
        print(f'O resultado de {num1} / {num2} é igual à: {res}')
    else:
        res = 0
        return res

def opcoes():
    print('Calculadora em funcionamento')
    print('_'*10)
    print('Escolha uma opção para definir a operação: ')
    print(f'1: Soma \n2: Subtração \n3: Multiplicação \n4: Divisão \n')

n = 1
while n !=0:
    opcoes()
    op = int(input('Favor indicar o código da operação: '))
    if op >=1 <= 4:
        print('Calculadora em Funcionamento')
    else:
        print('Essa opção não existe.')
        opcoes()
        op = int(input('Favor indicar o código da operação: '))
    num1 = int(input('Digite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))
    calculadora(num1,num2, op)
    n = int(input('Digite [0] para encerrar a aplicação, para continuar digite [1]'))
print('fim!')