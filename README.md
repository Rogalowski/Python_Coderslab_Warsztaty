#ZADANIE1
Warsztat: Gra w zgadywanie liczb.

Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:

    Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
    Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po czym wrócić do pkt. 1
    Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", po czym wrócić do pkt. 1.
    Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", po czym wrócić do pkt. 1.
    Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć działanie programu.

Przykład:
Guess the number: cześć
It's not a number!
Guess the number: 50
To small!
Guess the number: 75
To big!
Guess the number: 63
You win!
    Pamiętaj, aby obsłużyć odpowiednie błędy!

#ZADANIE2
Symulator LOTTO
Warsztat: Symulator LOTTO.

Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49. 
Zadaniem gracza jest poprawne wytypowanie losowanych liczb. 
Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.

Napisz program, który:

    zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
        czy wprowadzony ciąg znaków jest poprawną liczbą,
        czy użytkownik nie wpisał tej liczby już poprzednio,
        czy liczba należy do zakresu 1-49,
    po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
    wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
    poinformuje gracza, ile liczb trafił.

#ZADANIE3
Gra w zgadywanie liczb 2
Warsztat: Gra w zgadywanie liczb 2

Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb"). Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał. Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).

Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".

Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie. flowchart

#ZADANIE4
Gra w zgadywanie liczb 3
Warsztat: Gra w zgadywanie liczb 3

Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy frameworka Flask. Użytkownik dostaje do dyspozycji formularz z trzema guzikami: To small, To big, You win.

Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).

    Uwaga – nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla, np. przy pomocy Firebuga. W tej sytuacji jednak zupełnie wystarczające. Najwyżej zepsuje sobie zabawę ;)

#ZADANIE5
Kostka do gry
Warsztat: Kostka do gry

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, sześciennych. Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna! Ponieważ w grach kośćmi rzuca się często, pisanie za każdym razem np. "rzuć dwiema kostkami dziesięciościennymi, a do wyniku dodaj 20" byłoby nudne, trudne i marnowałoby ogromne ilości papieru. W takich sytuacjach używa się kodu "rzuć 2D10+20".

Kod takiej kostki wygląda następująco:
xDy+z

gdzie:

    y – rodzaj kostek, których należy użyć (np. D6, D10),
    x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
    z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

Przykłady:

    2D10+10: 2 rzuty D10, do wyniku dodaj 10,
    D6: zwykły rzut kostką sześcienną,
    2D3: rzut dwiema kostkami trójściennymi,
    D12-1: rzut kością D12, od wyniku odejmij 1.

Napisz funkcję, która:

    przyjmie w parametrze taki kod w postaci łańcucha znaków,
    rozpozna wszystkie dane wejściowe:
        rodzaj kostki,
        liczbę rzutów,
        modyfikator,
    jeśli podany ciąg znaków jest niepoprawny, zwróci odpowiedni komunikat,
    wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.

#ZADANIE6
2001
Warsztat: Salon gier (*)

Zaimplementuj grę 2001. Poniżej znajdziesz zasady.
2001 – Zasady Gry

    Każdy z graczy zaczyna z liczbą punktów równą 0.
    W swojej turze, gracz rzuca 2 kośćmi do gry (standardowe kości sześciościenne).
    Wyrzucona liczba oczek jest dodawana do sumarycznej liczby punktów.
    Począwszy od drugiej tury:
        jeśli gracz wyrzuci 7, dzieli swoją liczbę punktów przez tę wartość odrzucając część ułamkową,
        jeśli wyrzuci 11, mnoży aktualną liczbę punktów przez tę wartość.
    Wygrywa gracz, który jako pierwszy uzyska 2001 punktów.

Implementacja

    Zaimplementuj grę w wersji dla dwóch graczy.
    Niech będzie to aplikacja konsolowa.
    Niech drugim graczem będzie komputer.
    Po każdej turze wyświetl aktualną liczbę punktów.
    Rzut gracza, powinien odbywać się po naciśnięciu przez użytkownika klawisza enter. Rzut komputera następuje automatycznie, po rzucie gracza. Zakończ program w momencie, gdy gracz, lub komputer osiągnie więcej niż 2001 punktów.

Modyfikacja 1

Zauważyłeś pewno, że gra w obecnej wersji jest mało interaktywna i sprowadza się tylko i wyłącznie, do klikania klawisza enter. Spróbujmy uczynić ją trochę bardziej interaktywną.

    Przed każdym rzutem, daj graczowi wybór.
    Niech wybierze 2 kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100.
    Kości mogą się powtarzać, gracz może też użyć 2 różnych kości.
    Niech wybór kości odbywa się za pomocą wprowadzenia odpowiedniego łańcucha znaków przez gracza (po jednym na każdą z kości).
    Możesz wykorzystać kod z zadania Kostka do gry.
    Wybór kości przez komputer niech będzie losowy.

Reszta zasad pozostaje bez zmian.
Modyfikacja 2

Spróbuj teraz przenieść swoją grę na serwer przy użyciu Flaska. Aby przechowywać informację między turami, wykorzystaj ukryte pola formularza. Nie jest to najlepsze rozwiązanie (może być podatne na oszukiwanie), ale na tę chwilę się tym nie przejmujemy. Wybór kości przed rzutem, powinien odbywać się za pomocą formularza.
