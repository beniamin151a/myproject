import statistics

def analyze_numbers():
    while True:
        data = input("Podaj liczby całkowite oddzielone spacją: ")
        if not data:
            print("Nie wprowadzono żadnych danych.")
            continue
        try:
            numbers = [int(x) for x in data.strip().split()]
        except ValueError:
            print("Podaj liczby całkowite oddzielone spacją!")
            continue
        
        length = len(numbers)
        total = sum(numbers)
        average = statistics.mean(numbers)
        positive_numbers = len([x for x in numbers if x > 0])
        negative_numbers = len([x for x in numbers if x < 0])
        zeros = numbers.count(0)
        maximum = max(numbers)
        minimum = min(numbers)
        reversed_order = numbers[::-1]
        variance = statistics.variance(numbers) if length > 1 else 0
        deviation = statistics.stdev(numbers) if length > 1 else 0

        results = f"""
Wyniki analizy:

Liczba wszystkich wartości: {length}
Suma liczb: {total}
Średnia: {average}
Liczba dodatnich liczb: {positive_numbers}
Liczba ujemnych liczb: {negative_numbers}
Liczba zer: {zeros}
Wariancja: {variance}
Odchylenie standardowe: {deviation}
Największa wartość: {maximum}
Najmniejsza wartość: {minimum}
Liczby w odwrotnej kolejności: {reversed_order}
"""
        print(results)

        if input("Czy chcesz zapisać wyniki do pliku? (t/n): ").lower() == 't':
            with open("wyniki_analizy.txt", "w", encoding="utf-8") as file:
                file.write(results)
            print("Wyniki zapisano do pliku o nazwie 'wyniki_analizy.txt'")

        if input("Czy chcesz przeprowadzić kolejną analizę? (t/n): ").lower() != 't':
            print("Zakończono działanie programu!")
            break

analyze_numbers()