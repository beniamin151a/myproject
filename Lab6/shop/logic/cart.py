from shop.models.product import Product

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def total_price(self):
        return sum(p.price for p in self.products)

    def __len__(self):
        return len(self.products)

    def __contains__(self, product: Product):
        return product in self.products

    def __str__(self):
        if not self.products:
            return "Koszyk jest pusty."
        result = "Zawartość koszyka:\n"
        for p in self.products:
            result += f"- {p}\n"
        result += f"Suma: {self.total_price()} PLN"
        return result
