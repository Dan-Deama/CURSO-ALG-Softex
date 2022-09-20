"""Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que outros desenvolvedores possam analisá-lo."""

rodas = int(input("Quantas rodas possui o seu veículo? "))
peso = int(input('Qual o peso bruto do seu veículo (em KG)? '))
passageiros = int(input('Quantos passageiros ele é capaz de transportar? '))
if rodas <= 3:
    print(f'Para dirigir veículos com {rodas} rodas, o ideal é tirar uma habilitação A.')
elif rodas == 4 and passageiros <= 8 and peso < 3500:
    print(f'Para dirigir veículos com {rodas} rodas, com até {peso} kg, e que levem {passageiros} passageiros o ideal é tirar uma habilitação B.')
elif rodas >= 4 and (peso >= 3500 <= 6000):
    print(f'Para dirigir veículos com {rodas} rodas e com até {peso} kg, o ideal é tirar uma habilitação C.')
elif rodas >= 4 and passageiros > 8:
    print(f'Para dirigir veículos com {rodas} rodas, e que levem {passageiros} passageiros o ideal é tirar uma habilitação D.')
elif rodas >= 4 and peso > 6000:
    print(f'Para dirigir veículos com {rodas} rodas e com até {peso} kg, o ideal é tirar uma habilitação E')
else:
    print('Os dados foram preenchidos corretamente? Vamos tentar outra vez!')