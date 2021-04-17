print("Imagine number between 0 and 1000!")


def guess_def(mini=0, maxi=1000, j=1):
    guess = int((maxi - mini) / 2) + mini
    print("\n")

    # Proba dodania mozliwosci poprawy komendy przy jej blednym wprowadzeniu. W innym przypadku konyczl program
    while j <= 10:

        print(j, "chance ---> Guess: " + str(guess))

        answer = input("Available answers: \n - Correct \n - Too big \n - To small\nType here: ")

        if j < 10 and answer == "Correct" or "Too big" or "Too small":
            print(j + 1)

            if answer == "Correct" and j < 10:
                print("You WIN!!!")
                break
            elif answer == "Too big" and j < 10:
                j += 1
                print("Too much?")
                guess_def(mini, guess, j)
            elif answer == "Too small" and j < 10:
                j += 1
                print("Too less?")
                guess_def(guess, maxi, j)
            elif j == 9:
                print("Koniec Szans\n")
                j += 1

            else:
                if j == 10:
                    print("DO NOT CHEAT!!!\n")
                    break
    else:
        print("KONIEC")


if __name__ == '__main__':
    guess_def(0, 1000, )

###################MY SIMPLER:
# def guess_def(mini = 0, maxi = 1000, j = 1, flag = True):
#     guess = int((maxi-mini)/2)+mini
#     print("\n")
#     print(j, "chance ---> Guess: " + str(guess))
#
#
#
#
#     answer = input("Available answers: \n - Correct \n - Too big \n - To small\nType here: ")
#     if answer == "Correct" or "Too big" or "Too small":
#
#         if answer == "Correct" and j < 10:
#             print("You WIN!!!")
#         elif answer == "Too big" and j < 10:
#             print("Too much?")
#             guess_def(mini, guess, j + 1)
#         elif answer == "Too small" and j < 10:
#             print("Too less?")
#             guess_def(guess, maxi, j + 1)
#         else:
#             print("Do not cheat! Try again!!!\n")


##########################ODP Z LMS CODERSLAB:
# def user_input():
# """Return proper value provided by user.
# :rtype: str
# :return: value provided by user from ["to small", "to big", "you win"]
# """
#   possible_input = ["to small", "to big", "you win"]
#     while True:
#         user_answer = input().lower()
#         if user_answer in possible_input:
#             break
#         print("Input is not in ['to small', 'to big', 'you win']")
#     return user_answer
#
#
#
# def guess_the_number():
#     """Main function for our program."""
#     print("Imagine number between 0 and 1000!")
#     print("Press 'Enter' to continue")
#     input()
#     min_number = 0
#     max_number = 1000
#     user_answer = ""
#     while user_answer != "you win":
#         guess = (max_number - min_number) // 2 + min_number
#         print(f"Your number is: {guess}")
#         user_answer = user_input()
#         if user_answer == "to big":
#             max_number = guess
#         elif user_answer == "to small":
#             min_number = guess
#     print("Hurra! I guess!")
#
# if __name__ == '__main__':
#     guess_the_number()
