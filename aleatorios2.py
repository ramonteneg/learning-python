from random import randint


def dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)

    return dice1, dice2

d = dices()
d1 = d[0]
d2 = d[1]

print("Dices:", d)
print("Dice 1:", d1)
print("Dice 2:", d2)

if d1 == d2:
    print("Felicidades, eres el ganador")
else:
    print("Sigue intentando")
