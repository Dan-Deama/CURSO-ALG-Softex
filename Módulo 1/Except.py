print('Calculadora de Juros')
capital = ()
emprestimo = False
while not emprestimo:
    print('Digite o valor pretendido, e em seguida a quantidade de parcelas desejadas. ')
    capital = input('Informe o valor pretendido: ')
    try:
        if capital.isnumeric():
            capital = int(capital)
            if capital <= 10000:
                juros = 3.7
            else:
                juros = 5.5
            try:
                parcelas = input('Digite a quantidade de parcelas: ')
                if parcelas.isdigit():
                    parcelas = int(parcelas)
                    emprestimo = True
                montante = capital*(1+juros/100)**parcelas
                print(f'O empréstimo solicitado foi de R${capital:.2f}, e será sujeito à um juros de {juros}%,'
                      f' resultando num montante de R${montante:.2f} a ser pago em {parcelas:.2f} meses.')
                print(f'Você pagará o total de R${(montante-capital):.2f} de juros, e parcelas de R${(montante/parcelas):.2f}.')
            except: print(f'A quantidade de parcelas digitadas não é válido, gentileza tentar novamente.')
        else:print(f'O valor "{capital}" digitado, não é válido, gentileza tentar novamente.')
    except: print(f'Houve um erro no input das informações, gentileza tentar novamente.')
