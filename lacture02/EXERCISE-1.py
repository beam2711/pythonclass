Score_1 =int(input('Enter the score for test 1: '))
Score_2 =int(input('Enter the score for test 2: '))
Score_3 =int(input('Enter the score for test 3: '))

average = ( Score_1 + Score_2 + Score_3)/3
print('The average score is',average)
if average > 95:
    print('Congrstulations')
    print('Thas is a great average')