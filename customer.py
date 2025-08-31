from customer_type import CustomerType
from order_item import OrderItem


class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, delivery_address: str, customer_type: CustomerType, customer_discount: int):
        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.customer_gift = None

    def add_favorite(self, item: OrderItem):
        if item not in self.favorite_items:
            self.favorite_items.append(item)

    def remove_favorite(self, item):
        if item in self.favorite_items:
            self.favorite_items.remove(item)

    def add_favorites_from_order(self, items: list[OrderItem]):
        for it in items:
            self.add_favorite(it)

    def print_favorites(self):
        print(f"{self.first_name} favorites: {[it.name for it in self.favorite_items] or None}")

    def take_gift(self, gift):
        self.customer_gift = gift

    def open_gift(self):
        if self.customer_gift:
            self.customer_gift.open_gift()



