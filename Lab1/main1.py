import math


def get_valid_input(prompt):
    """
    Pobiera dane od użytkownika i weryfikuje, czy są to dodatnie liczby.
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print("Wartość musi być dodatnia. Spróbuj ponownie.")
                continue
            # Walidacja wprowadzonych danych
            return value
        except ValueError:
            print("Wprowadzono nieprawidłową wartość. Proszę wprowadzić liczbę.")


def calculate_bmi(masa_kg, wzrost_cm):
    """
    Oblicza BMI (Body Mass Index) wg wzoru.
    """
    # Przekształcenie wzrostu (w cm) na metry (wzrost/100)
    wzrost_m = wzrost_cm / 100.0

    # Obliczenie BMI: masa / (wzrost/100)^2
    bmi = masa_kg / (wzrost_m ** 2)

    # Zaokrąglenie wyniku BMI do 2 miejsc po przecinku
    return round(bmi, 2)


def interpret_bmi(bmi):
    """
    Zwraca interpretację wyniku BMI opartą na powszechnie przyjętych i logicznych zakresach.
    """
    # 1. Poniżej 18.5 -> niedowaga
    if bmi < 18.5:
        return "niedowaga"

    # 2. 18.5 <= BMI < 25.0 -> waga prawidłowa
    elif bmi < 25.0:
        return "waga prawidłowa"

    # 3. 25.0 <= BMI < 30.0 -> nadwaga
    elif bmi < 30.0:
        return "nadwaga"

    # 4. BMI >= 30.0 -> otyłość
    else:
        return "otyłość"


def main():
    """
    Główna funkcja programu, obsługująca wielokrotne obliczenia.
    """
    print("---  Kalkulator BMI  ---")

    while True:
        print("\n--- Rozpoczęcie obliczeń dla nowej osoby ---")

        # Pobiera od użytkownika dane: wzrost (w cm), masę ciała (w kg.)
        wzrost_cm = get_valid_input("Podaj swój wzrost (w cm): ")
        masa_kg = get_valid_input("Podaj swoją masę ciała (w kg.): ")

        # Obliczenie BMI
        bmi_result = calculate_bmi(masa_kg, wzrost_cm)

        # Interpretacja wyniku
        interpretation = interpret_bmi(bmi_result)

        # Wyświetla wynik wraz z interpretacją
        print(f"\n Twoje BMI wynosi: {bmi_result}")
        print(f"Interpretacja: {interpretation.upper()}")

        # Pytanie o kontynuację (wymagane: możliwość obliczenia BMI dla kilku osób w jednej sesji)
        if input("\nCzy chcesz obliczyć BMI dla kolejnej osoby? (T/N): ").upper() != 'T':
            break

    print("\n--- Koniec pracy kalkulatora. ---")


if __name__ == "__main__":
    main()