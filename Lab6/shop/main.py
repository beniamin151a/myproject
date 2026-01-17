from shop.models.product import Product
from shop.logic.cart import Cart

def main():
    # Tworzenie produktów
    print("--- Tworzenie produktów ---")
    p1 = Product("Laptop", 3500.00, "Elektronika")
    p2 = Product("Jabłko", 2.50, "Spożywcze")
    p3 = Product("Myszka", 150.00, "Elektronika")
    p4 = Product("Chleb", 4.00, "Spożywcze")

    print(f"Utworzono: {p1}, {p2}, {p3}, {p4}")

    # Testowanie operatorów
    print("\n--- Testowanie operatorów ---")
    print(f"Czy {p1.name} == {p2.name}? {p1 == p2}")
    print(f"Czy {p1.name} == {p1.name}? {p1 == p1}") # Powinno być True
    print(f"Czy {p2.name} < {p1.name}? {p2 < p1}") # 2.50 < 3500.00 -> True
    
    products_list = [p1, p2, p3, p4]
    print(f"Przed sortowaniem: {[p.name for p in products_list]}")
    products_list.sort() # Sortowanie po cenie (__lt__)
    print(f"Po sortowaniu (cena): {[p.name for p in products_list]}")
    
    print(f"Długość nazwy '{p1.name}': {len(p1)}")

    # Obsługa koszyka
    print("\n--- Obsługa koszyka ---")
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    
    print(f"Liczba produktów w koszyku: {len(cart)}")
    print(f"Czy {p2.name} jest w koszyku? {p2 in cart}")
    print(f"Czy {p4.name} jest w koszyku? {p4 in cart}")
    
    print("\n--- Zawartość koszyka ---")
    print(cart)
    
    print("\n--- Usuwanie produktu ---")
    cart.remove_product(p2)
    print(f"Usunięto {p2.name}. Liczba produktów: {len(cart)}")
    print(cart)

if __name__ == "__main__":
    main()
