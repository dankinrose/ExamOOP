from abc import ABC, abstractmethod
from customer import Customer
from order_item import OrderItem
from payment_type import PaymentType


class Order(ABC):
    @abstractmethod
    def __init__(self, order_id: int, name: str, delivery_address: str, items: list[OrderItem], customer: Customer, payment_type: PaymentType, order_date):
        self.id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.total_price = self.calculate_total_price()
        self.customer.add_favorites_from_order(self.items)


    def base_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price


    @abstractmethod
    def calculate_total_price(self):
        pass

    def print_order(self):
        print(f"\n --- Order id: {self.id} ---")
        print(f"name: {self.name}")
        print(f"Date: {self.order_date}")
        print(f"Customer: {self.customer.first_name} {self.customer.last_name} ({self.customer.customer_type.value})")
        print(f"Delivery: {self.delivery_address}")
        print(f"Payment: {self.payment_type.value}")
        print("Items:")
        for it in self.items:
            print(f"  - {it.name} (id={it.id}, price={it.price})")
        print(f"Total price: {self.total_price}")