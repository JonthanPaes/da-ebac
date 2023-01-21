import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('gasolina.csv')
sns.lineplot(x='dia', y='venda', data=df)
plt.title('Preço da Gasolina por dia')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.savefig('gasolina.png')
