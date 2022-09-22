# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 00:08:27 2022

@author: Danilo
"""

import pandas as pd
 
df = pd.read_csv('notas_alunos.csv')
media = df['nota_1'] + df['nota_2'] / 2
df['media'] = media

situacao = df['situcao']
df.loc[df['media'] < 7, 'situacao'] = 'REPROVADO'
df.loc[df['media'] >= 7, 'situacao'] = 'APROVADO'
df.loc[df['faltas'] <= 5, 'situacao'] = 'APROVADO'
df.loc[df['faltas'] > 5, 'situacao'] = 'REPROVADO'
df.to_csv('alunos_situacao.csv')

maior_faltas = df['faltas'].max()
media_geral = df['media'].sum() / df['media'].count()
maior_media = df['media'].max()

print(f'\nMaior número de faltas:', maior_faltas)
print(f'Média da turma', media_geral)
print(f'A maior média foi:', maior_media)
