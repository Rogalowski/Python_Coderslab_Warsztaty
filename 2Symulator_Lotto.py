from random import randint

lotto = [] #numbers randomized in lotto
choosen = [] #numbers choosen by player

#i,j - counters

def lotto_def(i = 0):

    # for i in range(6):
    while len(lotto) != 6:  # losuje tak dlugo az lista lotto nie bedzie dluga do 6
        i = i + 1
        rand_num = randint(1, 49)

        # print(i, "wylosowana:", rand_num) #sprawdzenie ile liczb musial wylosowac i jakich aby sie nie powtarzaly
        if rand_num not in lotto:
            lotto.append(rand_num)
    return sorted(lotto)

def shooting_def(i = 0):

    while len(choosen) != 6:  # losuje tak dlugo az lista wybranych liczb nie bedzie dluga do 6
        try:
            i = i + 1

            print("Provide", i, "number:", end=" ")
            number = int(input())

            if number in choosen:
                print("This number exist, try with another!")
                i = i - 1
            elif number < 1 or number > 49:
                print("This number out of range, try with another!")
                i = i - 1
            else:
                choosen.append(number)
        except ValueError:
            print("Please provide int number")
            i = i - 1
    return sorted(choosen)

def main_lotto_def():
    i = 0

    for j in range(6):



        if choosen[j] in lotto:
            j += 1
            print("You hit:", j)
            i += 1
    if i >= 3 and i <= 6:
        print("BRAVO, You hit in total:", i, "numbers")
    else:
        print("Unfourtenally its too less. You hit in total:", i)
    return ""

print("GAME LOTTO, Please Choose 6 numbers from 1 - 49")
print("Numbers of user:", shooting_def())
print("Numbers radomized by lotto:", lotto_def())
print(main_lotto_def())