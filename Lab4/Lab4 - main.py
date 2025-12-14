# main.py
# Główny program korzystający z klas Book i Library

from library import Book, Library

def main():
    library = Library()

    while True:
        print("\n=== SYSTEM BIBLIOTECZNY ===")
        print("1. Dodaj książkę")
        print("2. Wypożycz książkę")
        print("3. Zwróć książkę")
        print("4. Wyświetl listę książek")
        print("5. Zakończ")

        choice = input("Wybierz opcję (1–5): ")

        if choice == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            year = input("Rok wydania: ")
            book = Book(title, author, year)
            print(library.add_book(book))

        elif choice == "2":
            title = input("Podaj tytuł książki do wypożyczenia: ")
            print(library.borrow_book(title))

        elif choice == "3":
            title = input("Podaj tytuł książki do zwrotu: ")
            print(library.return_book(title))

        elif choice == "4":
            print("\nLista książek:")
            print(library.list_books())

        elif choice == "5":
            print("Zamykanie programu...")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()



