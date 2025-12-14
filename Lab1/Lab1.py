def mathematical_remainder(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed!")
    return ((x % y) + abs(y)) % abs(y)

# Zalety działania operatora % w ten sposób:
# • Jest zgodny z operatorem //, więc łatwiej tworzyć obliczenia oparte na dzieleniu całkowitym, np. w szyfrowaniu lub kompresji danych.
# • Dobrze sprawdza się w sytuacjach, gdzie wynik ma się „zawijać”, np. w pętlach lub tablicach cyklicznych.
#   Przykład: przesunięcie o -1 w liście [A, B, C] -> (-1 % 3) = 2 -> wskazuje na element C.
# • Działa podobnie jak w niektórych innych językach (np. Ruby), co ułatwia przenoszenie kodu między różnymi środowiskami.