class LogReader:
    """
   
    """
    def __init__(self, filename, keyword):
        # POPRAWKA: Używamy argumentu 'keyword'
        self.keyword = keyword 
        try:
            # Otwórz plik w trybie do odczytu
            self.file = open(filename, 'r')
        except FileNotFoundError:
            # Jeśli plik nie istnieje, ustaw file na None
            self.file = None

    def __iter__(self):
        # Iterator zwraca sam siebie
        return self

    def __next__(self):
        # Jeśli plik nie został otwarty
        if self.file is None:
            raise StopIteration

        while True:
            # Czytanie pliku linia po linii (wymaganie odczytu liniowego)
            line = self.file.readline()

            # Koniec pliku
            if not line:
                # Zadbaj o zamknięcie pliku i rzuć StopIteration
                self.file.close()
                self.file = None
                raise StopIteration

            # Zwróć linie zawierające słowo kluczowe
            if self.keyword in line:
                return line.strip()

# --- BLOK TESTOWY ---

def create_mock_log(filename="log.txt"):
    """Tworzy przykładowy plik logów do testów, zawierający słowo 'word'."""
    log_content = """
2025-12-14 INFO: System started successfully.
2025-12-14 WARNING: Missing configuration file.
2025-12-14 ERROR: Failed to load user profile.
2025-12-14 DEBUG: Found the search word in this line.
2025-12-14 INFO: Processing completed.
2025-12-14 WORD: This line contains the keyword word, so it should be printed.
2025-12-14 INFO: Another line without the keyword.
"""
    with open(filename, 'w') as f:
        f.write(log_content.strip())
    print(f"Utworzono plik testowy: {filename}")

if __name__ == "__main__":
    
    FILENAME = "log.txt"
    KEYWORD = "word"
    
    # 1. Tworzymy plik log.txt
    create_mock_log(FILENAME)
    
    print(f"\n--- Wyszukiwanie frazy '{KEYWORD}' w pliku '{FILENAME}' ---")
    
    try:
        # Tworzymy instancję LogReader
        lr = LogReader(FILENAME, KEYWORD)
        
        # Testujemy działanie w pętli for (wymagane w lab)
        for line in lr:
            print("Z NALEZIONO:", line)
            
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")