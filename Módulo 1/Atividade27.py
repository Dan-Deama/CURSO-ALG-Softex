import enum


class eleicao(enum.Enum):
    x = 889
    y = 847
    z = 515
    branco = 0


x = 0
y = 0
z = 0
branco = 0


n = 'N'
while True and n != 'S':

      try:
        print('INÍCIO DA VOTAÇÃO \nPara eleger o candidato X, vote 889. \nPara eleger o candidato Y, vote 847. \nPara eleger o candidato Z, vote 515.')
        voto = int(input(f'digite o número do seu cadidato: '))
        if voto == 889:
            x += 1
        elif voto == 847:
            y += 1
        elif voto == 515:
            z += 1
        else:
            branco += 1
      except(ValueError, TypeError):
          print('você deve digitar apenas numeros, tente outra vez!')
          voto = int(input(f'digite o número do seu cadidato'))

      n = input('Você deseja encerrar a eleição? [S/N]')
      print('-' *50)
      if n == 'S':
        print('\n >>>APURAÇÃO DOS VOTOS<<< \n')
        if x > y and x> z:
          eleito = eleicao.x
          print('CANDIDATO ELEITO>>>', eleito.name)
        elif y > x and y > z:
           eleito = eleicao.y
           print('CANDIDATO ELEITO>>>', eleito.name)
        elif z > x and z > y:
           eleito = eleicao.z
           print('CANDIDATO ELEITO>>', eleito.name)
        else:
          print('Brancos e nulos tiveram percentual de votos')
        print(' \n TOTAL DE VOTOS x:', x, ' \n TOTAL DE VOTOS y:', y, '\n TOTAL DE VOTOS z:', z, ' \n TOTAL DE VOTOS brancos e nulos:',branco,'\n')
