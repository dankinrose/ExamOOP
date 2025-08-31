from overrides import overrides
from order import Order

class RegularOrder(Order):
    def __init__(self,order_id, name, delivery_address, items, customer, payment_type, order_date):
        super().__init__(order_id, name, delivery_address, items, customer, payment_type, order_date)

    @overrides
    def calculate_total_price(self):
        return self.base_total_price()