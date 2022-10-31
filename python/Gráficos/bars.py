from matplotlib import pyplot as plt

players = ['João', 'Ronaldo', 'Vinícius', 'David']
score = [21, 30, 67, 45]
plt.bar(players, score, color='green')
plt.title('Score Card')
plt.xlabel('Jogadores')
plt.ylabel('Rodadas')
plt.show()
