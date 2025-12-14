class LogReader:
    """
    Klasa iteratora czytająca plik liniowo i filtrująca wg słowa kluczowego.
    """
    def __init__(self, filename, keyword):
        self.keyword = keyword
        try:
            self.file = open(filename, 'r')
        except FileNotFoundError:
            self.file = None

    def __iter__(self):
        return self  # iterator zwraca sam siebie

    def __next__(self):
        # Jeśli plik nie został otwarty
        if self.file is None:
            raise StopIteration

        while True:
            line = self.file.readline()

            # Koniec pliku
            if not line:
                self.file.close()
                self.file = None
                raise StopIteration

            # Zwróć linie zawierające słowo kluczowe
            if self.keyword in line:
                return line.strip()
