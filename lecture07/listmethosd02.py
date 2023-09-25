heroes = ['Ironman', 'Thor', 'hulk', 'Superman', 'Spiderman',]
h2 = ['Dr.Strange', 'Cpt. America', 'Black Panther', 'Ant Man']

heroes.insert(0, h2[0])
print(heroes.index('Thor')), h2[1]

heroes.insert(heroes.index('Thor'), h2[1])
print(heroes)

heroes.remove('Superman')
heroes.append('Ant Man')
print(heroes)

heroes.sort()
print(heroes)

heroes.reverse()
print(heroes)

newheroes = heroes
newheroes[0] = 'Woder Women'
print(heroes)

copyheroes = [] + heroes
print(copyheroes)

copyheroes[0] = 'Henman'
print(heroes)
print(copyheroes)