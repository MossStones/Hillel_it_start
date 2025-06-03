from typing import Dict

class Item:
    def __init__(self, name: str, price: float, description: str, dimensions: str) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name: str, surname: str, numberphone: str) -> None:
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user: User) -> None:
        self.user: User = user
        self.products: Dict[Item, int] = {}

    def add_item(self, item: Item, cnt: int) -> None:

        self.products[item] = cnt

    def get_total(self) -> float:
        total_price = 0
        for item, cnt in self.products.items():
            total_price += item.price * cnt
        return total_price

    def __str__(self) -> str:
        lines = [f"User: {self.user}"]
        lines.append("Items:")
        for item, cnt in self.products.items():
            lines.append(f"{item.name}: {cnt} pcs.")
        return "\n".join(lines)



lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
