class OrderItem:
    def __init__(self, item_id: int, name: str, price: int):
        self.id = item_id
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, OrderItem):
            return self.name.strip().lower() == other.name.strip().lower()
        return False
