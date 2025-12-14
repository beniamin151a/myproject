import time


# --- MODUŁ GŁÓWNY: Klasa Board ---

class Board:
    """
    Reprezentuje szachownicę dla problemu N Królowych.
    """

    def __init__(self, n=8):
        # Inicjalizuje szachownicę o rozmiarze n x n (domyślnie 8x8)[cite: 64, 65].
        self.n = n
        # Lista przechowująca pozycje królowych jako krotki (wiersz, kolumna).
        self.queens = []

    # --- METODY API DO ZARZĄDZANIA KRÓLOWYMI ---

    def place(self, row, col):
        # Umieszcza królową na pozycji (row, col).
        # W algorytmie backtracking to jest 'próba' ruchu.
        self.queens.append((row, col))

    def remove(self, row, col):
        # Usuwa królową z pozycji (row, col).
        # Jest to operacja 'backtrack' (cofanie)[cite: 48].
        if (row, col) in self.queens:
            self.queens.remove((row, col))

    def is_safe(self, row, col):
        """
        Sprawdza, czy pozycja (row, col) jest bezpieczna dla nowej królowej.
        Wiersz nie musi być sprawdzany, ponieważ algorytm umieszcza tylko jedną królową na wiersz.
        """
        for r, c in self.queens:
            # Sprawdzenie kolumny: Jeśli kolumna jest taka sama, jest atak.
            if c == col:
                return False
            # Sprawdzenie przekątnych: Atak następuje, gdy różnica wierszy 
            # jest równa różnicy kolumn (abs(r1 - r2) == abs(c1 - c2)).
            if abs(r - row) == abs(c - col):
                return False
        return True

    # --- ALGORYTM BACKTRACKING ---

    def solve_recursive(self, row):
        """
        Rekurencyjna funkcja rozwiązująca problem.
        Zwraca listę wszystkich znalezionych rozwiązań.
        """
        solutions = []

        # Warunek bazowy: Jeśli wszystkie wiersze zostały wypełnione, mamy rozwiązanie.
        if row == self.n:
            # Musimy zwrócić KOPIĘ listy, ponieważ self.queens zostanie zmienione 
            # przez dalsze operacje backtracking.
            solutions.append(list(self.queens))
            return solutions

        # Iteracja przez wszystkie kolumny w danym wierszu.
        for col in range(self.n):
            if self.is_safe(row, col):
                # Krok wprzód: Jeśli jest bezpiecznie, umieszczamy królową.
                self.place(row, col)

                # Rekurencyjne przejście do następnego wiersza.
                solutions.extend(self.solve_recursive(row + 1))

                # Backtracking: Cofamy ruch, aby spróbować innej kolumny w obecnym wierszu[cite: 50].
                self.remove(row, col)

        return solutions

    def solve(self):
        # Publiczna metoda uruchamiająca rozwiązanie.
        return self.solve_recursive(row=0)

    # --- FUNKCJE MAGICZNE (SPECIAL METHODS) ---

    def __str__(self):
        """
        Funkcja magiczna __str__ - zwraca czytelną reprezentację szachownicy.
        """
        board_str = ""
        for r in range(self.n):
            row_str = ""
            for c in range(self.n):
                if (r, c) in self.queens:
                    row_str += " Q "  # Królowa
                else:
                    row_str += " . "  # Puste pole
            board_str += row_str + "\n"
        return board_str

    def __repr__(self):
        """
        Funkcja magiczna __repr__ - zwraca jednoznaczną reprezentację obiektu 
        (przydatną dla deweloperów) .
        """
        return f"Board(n={self.n}, queens_count={len(self.queens)})"

    def __len__(self):
        """
        Funkcja magiczna __len__ - pozwala użyć len(board), zwraca liczbę królowych.
        """
        return len(self.queens)

    def __iter__(self):
        """
        Funkcja magiczna __iter__ - pozwala na iterowanie po pozycjach królowych (np. for pos in board).
        """
        yield from self.queens

    def __contains__(self, pos):
        """
        Funkcja magiczna __contains__ - pozwala użyć operatora 'in' (np. if (row, col) in board).
        """
        return pos in self.queens


# --- ZEWNĘTRZNA FUNKCJA API ---

def solve_n_queens(n=8):
    """
    Modularna funkcja publiczna uruchamiająca rozwiązanie dla N królowych.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Rozmiar N musi być dodatnią liczbą całkowitą.")

    board = Board(n)
    return board.solve()


# --- PRZYKŁAD UŻYCIA I TESTY ---

if __name__ == "__main__":

    print(" Testy jednostkowe ")

    # Rozmiar N = 4
    n4_solutions = solve_n_queens(4)
    print(f"\nRozmiar N=4: Znaleziono {len(n4_solutions)} rozwiązań. (Oczekiwano: 2)")

    # --- NOWA PĘTLA WYŚWIETLAJĄCA WSZYSTKIE ROZWIĄZANIA ---
    if n4_solutions:
        for i, solution in enumerate(n4_solutions):
            print(f"\nRozwiązanie N=4 #{i + 1}:")
            # Tworzymy tymczasowy obiekt Board na podstawie bieżącego rozwiązania,
            # aby wykorzystać magię __str__ do wydruku szachownicy
            temp_board = Board(4)
            temp_board.queens = solution
            print(temp_board)

        # Przykład użycia funkcji magicznych z pierwszego rozwiązania
        b4 = Board(4)
        b4.queens = n4_solutions[0]
        print(f"Ilość królowych (len(b4)): {len(b4)}")
        print(f"Czy (0, 1) jest na planszy? {'Tak' if (0, 1) in b4 else 'Nie'}")
        # ------------------------------------------------------------------

    # Rozmiar N = 8
    start_time = time.time()
    n8_solutions = solve_n_queens(8)
    end_time = time.time()

    print(f"\nRozmiar N=8: Znaleziono {len(n8_solutions)} rozwiązań. (Oczekiwano: 92) [cite: 96]")
    print(f"Czas obliczeń: {end_time - start_time:.4f}s")

    # Inne testy
    print(f"N=1: {len(solve_n_queens(1))} rozwiązań (Oczekiwano: 1) [cite: 92]")
    print(f"N=2: {len(solve_n_queens(2))} rozwiązań (Oczekiwano: 0) [cite: 93]")
    print(f"N=3: {len(solve_n_queens(3))} rozwiązań (Oczekiwano: 0) [cite: 94]")