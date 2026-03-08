import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('/home/tristeza/Documents/trabalho mae/projetoPessoal/dataScience_desafio/microDesafio_-_dueloDeTabelas-/src/microDesafio/planilhaCopa.csv')

df["total_gols"] = 0
for i in range(len(df['id_partida'])):
    gols_partida_atual = df['numero_gols_Brasil'][i]
    if gols_partida_atual > 0:
        df['total_gols'] += gols_partida_atual

df['mediasGols'] = df['total_gols'] / df['id_partida'].max()
print(f"{df['mediasGols'].mean():.2f}") 

x = df['id_partida'] + 1
y = df['numero_gols_Brasil']
z = df['mediasGols']

plt.plot(x, y, z)
plt.xlabel('qual partida da copa de 2022')
plt.ylabel('quantidade de gols do Brasil')
plt.title('Gols do Brasil por rodada da Copa')
plt.show()
