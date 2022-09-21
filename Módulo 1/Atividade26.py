anocorreto = False
while not anocorreto:
    print("Digite seu nome completo, e em seguida seu ano de nascimento.")
    try:
        nome = input('Gentileza informar seu nome completo: ')
        ano_nasc = int(input('Agora informe o ano do seu nascimento: '))
        if ano_nasc >= 1922 <= 2021:
            anocorreto = True
            idade = 2022 - ano_nasc
            print(f'Obrigado {nome}. Você nasceu em {ano_nasc}, e completou ou completará {idade} anos de idade no ano atual.')
        else:
            print("Você digitou um ano inválido")
    except:
        print("Caracter inválido, por favor digite um ano válido entre 1922 e 2021.")
