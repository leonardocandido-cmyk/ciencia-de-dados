import matplotlib.pyplot as plt
import pandas as pd

# Análise qualitativa
frutas = [
    "Maçã", "Banana", "Maçã",
    "Laranja", "Banana", "Banana",
    "Maçã", "Uva", "Laranja"
]

serie = pd.Series(frutas)
frequencia = serie.value_counts()

print(frequencia)

# Criando gráfico de barras
frequencia.plot(kind="bar")

plt.title("Frutas Preferidas dos Alunos")
plt.xlabel("Frutas")
plt.ylabel("Frequência")

plt.show()
plt.savefig("aula06-qualitativo")

plt.clf()

# Análise quantitativa
notas = [
    5, 6, 7, 8, 7,
    6, 5, 9, 10, 8,
    7, 6, 5, 8, 9
]

serie = pd.Series(notas)
frequencia = serie.value_counts()

print(frequencia)

serie.plot(kind="hist")

plt.title("Distribuição das Notas")
plt.xlabel("Notas")
plt.ylabel("Frequência")

plt.show()
plt.savefig("aula06-quantitativo")