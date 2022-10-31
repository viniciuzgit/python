import matplotlib.pyplot as pyplot
import numpy as np

data = np.array([50, 20, 10, 15, 5])
labels = ['Python', 'JavaScript', 'C#', 'Java', 'PHP']

pyplot.pie(data, labels= labels, shadow=False)
pyplot.title('Linguagens de Programação mais famosas 2022')
pyplot.show()