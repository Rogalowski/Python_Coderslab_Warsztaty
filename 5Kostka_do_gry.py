from random import randint

dism = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def game_cube(code):
###wyciagniecie pierwszej wartosci mnoznika
    print(type(code))
    print(code[0])
    if code[0].isdigit():
        x = int(code[0])
    else:
        x = 1

    y = []
    if code[1] =="D":
        y.append(code[1])
        y.append(code[2])
        d = int(y[1]) #ktory indeks ma D?


    wylosowana = randint(1, d)


    print(y) #rozdzielona kostak D6

    for i in range(len(code)):
        print(code[i], end="")

    if "+" in code:
        znak = code.split("+")
        koniec = x * wylosowana + int(znak[1])
    else:
        znak = code.split("-")
        koniec = x * wylosowana - int(znak[1])

    print(znak)

    #koniec = x * wylosowana

    #for i in code:
   #     print(code.index(i), code.join(","))


    print("Indeks D:", code.index("D"))
    print("Składowe---> Mnoznik:", x, "Kostka:",d, "wylosowana:", wylosowana, "dopelniacz:", znak[1])
    print("Konicowy wynik:", koniec)




print("BONES:")
letters = "2D6+5"
print(game_cube(letters))


# #################################################################################

# import random
#
# POSSIBLE_DICES = (
#
#     "D100",
#
#     "D20",
#
#     "D12",
#
#     "D10",
#
#     "D8",
#
#     "D6",
#
#     "D4",
#
#     "D3"
#
# )
#
#
# def roll_the_dice(dice_code):
#     """
#
#     Calculate dice roll from dice pattern.
#
#
#
#     :param str dice_code: dice pattern ex. `7D12-5`
#
#
#
#     :rtype: int, str
#
#     :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
#
#     """
#
#     for dice in POSSIBLE_DICES:
#
#         if dice in dice_code:
#
#             try:
#
#                 multiply, modifier = dice_code.split(dice)
#
#             except ValueError:
#
#                 return "Wrong Input"
#
#             dice_value = int(dice[1:])
#
#             break
#
#     else:
#
#         return "Wrong Input"
#
#     try:
#
#         multiply = int(multiply) if multiply else 1
#
#     except ValueError:
#
#         return "Wrong Input"
#
#     try:
#
#         modifier = int(modifier) if modifier else 0
#
#     except ValueError:
#
#         return "Wrong Input"
#
#     return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier
#
#
# if __name__ == '__main__':
#     print(roll_the_dice("2D10+10"))
#
#     print(roll_the_dice("D6"))
#
#     print(roll_the_dice("2D3"))
#
#     print(roll_the_dice("D12-1"))
#
#     print(roll_the_dice("DD34"))
#
#     print(roll_the_dice("4-3D6"))