from random import randint

randomized = randint(1, 100)

print("GAME GUESS NUMBER 1-100\n", end="")

def guess(goal):
    number_int = -1
    while number_int > 0 and number_int < 100 or goal == True:
        try:

            number = input("Guess the number: ")
            number_int = int(number)
            goal = False
            if number_int < randomized:
                print("Too samll")
            elif number_int > randomized:
                print("Too big")
            else:
                print("You win")

        except ValueError:
            print("It's not a number!")
    else:
        print("Number out of range")
        print(guess(True))


print(guess(True))


#######################################OK##################################################
#
# from random import randint
# print("GRA W ZGADYWANIE LICZB 1-100\n", end="")
#
# #number = -1
# randomized = randint(1, 100)
# trafiona = False
#
#
# while not trafiona:
#     try:
#         number = input("Guess the number: ")
#         number = int(number)
#
#         if number > 0 and number < 100:
#
#
#             if number < randomized:
#                 print("Too samll")
#             elif number > randomized:
#                 print("Too big")
#             else:
#                 trafiona = True
#                 print("You win")
#
#
#         else:
#              print("Podales liczbe z poza zakresu")
#
#
#     except ValueError:
#         print("It's not a number!")