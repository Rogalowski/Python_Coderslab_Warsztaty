from random import randint

lotto = []
wybrane = []


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
    while len(wybrane) != 6:  # losuje tak dlugo az lista wybranych liczb nie bedzie dluga do 6
        i = i + 1

        print("Podaj", i, "liczbe od 1 do 49:", end=" ")
        liczba = int(input())

        if liczba in wybrane:
            print("Ta liczba już istnieje, podaj inną!")
            i = i - 1
        elif liczba < 1 or liczba > 49:
            print("Ta liczba z poza zakresu, podaj inną!")
            i = i - 1
        else:
            wybrane.append(liczba)
    return sorted(wybrane)

def main_lotto_def():
    i = 0

    for j in range(6):



        if wybrane[j] in lotto:
            j += 1
            print("Trafione lotki", j)
            i += 1
    if i >= 3 and i <= 6:
        print("BRAWO, trafiles:", i, "liczb")
    else:
        print("Przykro mi,to za malo. Liczba trafionych:", i)


print("GAME LOTTO")
print("Podane liczby przez gracza to:", shooting_def())
print("Wylosowane liczby to:", lotto_def())
print(main_lotto_def())