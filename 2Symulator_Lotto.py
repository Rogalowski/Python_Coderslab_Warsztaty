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


    print("Podaj 6 liczb ktore sie nie powtorza:")
    while len(choosen) != 6:  # losuje tak dlugo az lista wybranych liczb nie bedzie dluga do 6
        try:
            i = i + 1

            print("Podaj", i, "liczbe od 1 do 49:", end=" ")
            number = int(input())

            if number in choosen:
                print("Ta liczba już istnieje, podaj inną!")
                i = i - 1
            elif number < 1 or number > 49:
                print("Ta liczba z poza zakresu, podaj inną!")
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
            print("Trafiona lotka to:", j)
            i += 1
    if i >= 3 and i <= 6:
        print("BRAWO, trafiles:", i, "liczb")
    else:
        print("Przykro mi,to za malo. Liczba ogolna trafionych:", i)


print("GAME LOTTO")
print("Podane liczby przez gracza to:", shooting_def())
print("Wylosowane liczby to:", lotto_def())
print(main_lotto_def())