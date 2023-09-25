print('Please select menu :\n 1.Display Heroes \n 2.Add Heroes \n 3.Insert Heroes \n 4.Remove Heroes \n 5.Display Sorted Heroes (Ascending / Descending)')
string_heroes = input('โปรดเลือกตัวเลขที่แสดงจาก menu :')
if string_heroes == 1 :
    
heroes = ['Ironman', 'Thor', 'hulk', 'superman', 'Spiderman',]
h2 = ['Dr.Strange', 'Cpt. America', 'Black Panther', 'Ant Man']

print(heroes + h2)


newheroes = heroes
newheroes[-1] = 'Woder Women'
print(newheroes)

heroes.remove('Woder Women')
print(heroes)

heroesnew = heroes + h2
heroesnew.reverse()
print(heroesnew)

heroesnew.sort()
print(heroesnew)