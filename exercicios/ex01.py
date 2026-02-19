import matplotlib.pyplot as plt

# Exercício 01 - Construa um gráfico de barras que compare a nota de popularidade de séries em 2025
series = ['Stranger Things', 'It', 'Game of Thrones', 'Friends']
notas = [5.0, 5.0, 4.8, 3.5]

plt.bar(series, notas)
plt.show()
plt.savefig('./exercicios/ex01.png')

# Construa um gráfico de barras que compare os celulares mais vendidos em 2026

# Ele limpa o gráfico criado, para criar novos
plt.clf()

celulares = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
faturamento = [200000, 320000, 500000]

plt.bar(celulares, faturamento)
plt.show()
plt.savefig('./exercicios/ex02.png')