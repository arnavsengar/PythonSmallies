import random
while True:
    print(''' r:roll the dice         s. stop    ''')
    user=(input("tell: "))
    if user=='r':
        number=random.randint(1,17)
        print(number)
    else:
        break