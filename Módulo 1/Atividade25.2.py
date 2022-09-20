def calculadora(num1, num2, op):
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


op = ''
n = 1
while n != 0 or (0 == op > 4):
    opcoes()
    print()
    op = int(input('Favor indicar o código da operação: '))
    if 1 <= op <= 4:
        print('Calculadora em Funcionamento')
    else:
        print('Essa opção não existe.')
        continue
    num1 = int(input('Digite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))
    calculadora(num1, num2, op)
    n = int(input('Digite [0] para encerrar a aplicação, para continuar digite [1]'))
print('Aplicação encerrada pelo usuário!')
