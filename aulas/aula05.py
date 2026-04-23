import pandas as pd
import matplotlib.pyplot as plt

# Cria um DataFrame a partir de um arquivo CSV
df = pd.read_csv('./dados/dados.csv')

# Exibe as primeiras linhas do DataFrame
print(df.head())

# Gráfico de boxplot
plt.boxplot(df['nota'])
plt.title('Boxplot das notas')
plt.ylabel('Notas')
plt.show()
plt.savefig('aula05-boxplot')