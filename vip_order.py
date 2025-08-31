from overrides import overrides
from customer_type import CustomerType
from order import Order


class VipOrder(Order):
    def __init__(self,order_id, name, delivery_address, items, customer, payment_type, order_date):
        super().__init__(order_id, name, delivery_address, items, customer, payment_type, order_date)

    @overrides
    def calculate_total_price(self):
        if self.customer.customer_type is not CustomerType.VIP:
            raise Exception ("Error!!! VIP order requires a VIP customer")
        base_price = super().base_total_price()
        discount = self.customer.customer_discount
        return base_price - discount
