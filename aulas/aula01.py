import matplotlib.pyplot as plt

categorias = ['Grupo A', 'Grupo B', 'Grupo C']
valores = [30, 45, 20]

plt.bar(categorias, valores)
plt.show()
plt.savefig('aula01.png')