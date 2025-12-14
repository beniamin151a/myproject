# library.py
# Definicje klas Book i Library

class Book:
    """Reprezentuje pojedynczą książkę w bibliotece."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow_book(self):
        """Wypożycza książkę, jeśli jest dostępna."""
        if self.is_available:
            self.is_available = False
            return f"Książka '{self.title}' została wypożyczona."
        else:
            return f"Książka '{self.title}' jest już wypożyczona."

    def return_book(self):
        """Zwraca książkę do biblioteki."""
        self.is_available = True
        return f"Książka '{self.title}' została zwrócona."

    def __str__(self):
        status = "Dostępna" if self.is_available else "Wypożyczona"
        return f"'{self.title}' — {self.author} ({self.year}), {status}"


class Library:
    """Zarządza zbiorem książek w bibliotece."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Dodaje książkę do zbioru."""
        self.books.append(book)
        return f"Dodano książkę: {book.title}"

    def list_books(self):
        """Wyświetla wszystkie książki."""
        if not self.books:
            return "Biblioteka jest pusta."
        result = "\n".join(f"{i+1}. {book}" for i, book in enumerate(self.books))
        return result

    def borrow_book(self, title):
        """Wypożycza książkę po tytule."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow_book()
        return f"Nie znaleziono książki o tytule '{title}'."

    def return_book(self, title):
        """Zwraca książkę po tytule."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"Nie znaleziono książki o tytule '{title}'."
