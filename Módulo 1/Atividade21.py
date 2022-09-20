"""PROBLEMA:
Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:
- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.
No sistema, todos os valores devem estar armazenados em variáveis."""

aluno = input('Digite o nome do(a) aluno(a): ')
nota1 = float(input('Digite sua 1ªnota: '))
nota2 = float(input('Agora, digite sua 2ªnota: '))
faltas = int(input(f'Quantas faltas {aluno} teve nesse periodo? '))
media = (nota1+nota2)/2

if (media <7) or (faltas>3):
    print(f'{aluno} está REPROVADO')
else:
    print(f'{aluno} está aprovado.')
