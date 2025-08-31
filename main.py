from payment_type import PaymentType
from customer_type import CustomerType
from order_item import OrderItem
from customer import Customer
from regular_order import RegularOrder
from vip_order import VipOrder
from some_gift import SomeGift
from datetime import date

if __name__ == '__main__':

    customer1 = Customer(customer_id=1, first_name="Daniel", last_name="Roze", email="daniel@roze.com", delivery_address="Moria 5, Ariel", customer_type=CustomerType.REGULAR, customer_discount=0)
    customer2 = Customer(customer_id=1, first_name="Zohar", last_name="Halamish", email="zohar@halamish.com", delivery_address="egoz 10, alon shvut", customer_type=CustomerType.VIP, customer_discount=10)

    milk1 = OrderItem(101, "Milk", 6)
    bread = OrderItem(102, "Bread", 8)
    coffee = OrderItem(103, "Coffee", 22)
    milk2 = OrderItem(999, "milk", 5)

    print(f"\n-before any {customer1.first_name} order-")
    customer1.print_favorites()
    order1 = RegularOrder(order_id= 5001, name="Order #5001", delivery_address= customer1.delivery_address, items= [milk1, bread], customer = customer1, payment_type =PaymentType.CREDIT_CARD, order_date = date.today())
    order1.print_order()
    print("\n-after order-")
    customer1.print_favorites()

    print(f"\n-before any {customer2.first_name} order-")
    customer2.print_favorites()
    order2 = VipOrder(order_id= 5002, name="Order #5002", delivery_address=customer2.delivery_address, items=[bread, coffee], customer= customer2, payment_type=PaymentType.CASH, order_date=date.today())
    order2.print_order()
    print("\n-after order-")
    customer2.print_favorites()

    print(f"\n-before {customer1.first_name} order with same item name (milk)-")
    customer1.print_favorites()
    order3 = RegularOrder(order_id= 5003, name="Order #5003", delivery_address=customer1.delivery_address, items=[milk2], customer= customer1, payment_type=PaymentType.OTHER, order_date=date.today())
    order3.print_order()
    print("\n-after order(expected: favorite list remains the same)-")
    customer1.print_favorites()
    print()

    print(f"{customer1.first_name} make changes in favorite list:")
    customer1.add_favorite(coffee)
    customer1.remove_favorite(bread)
    customer1.print_favorites()

    customer1.take_gift(SomeGift())
    print(f"\n{customer1.first_name} Opening gift:")
    customer1.open_gift()
    print()

    print("starting attempt to create VIP order for regular customer:")
    try:
        order4 = VipOrder(
            order_id=5004,
            name="Invalid VIP attempt",
            delivery_address=customer1.delivery_address,
            items=[coffee],
            customer=customer1,
            payment_type=PaymentType.CHECK,
            order_date=date.today(),
        )
    except Exception as e:
        print(e)




