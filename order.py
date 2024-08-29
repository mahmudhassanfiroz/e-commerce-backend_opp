
import uuid
from datetime import datetime
from cart import Cart 
from user import Customer, User 
from product import Product, electronics
class Order:
    def __init__(self, cart):
        """
        Initializes an order object.
        Args:
            cart (Cart): The shopping cart containing the items for the order. 
        """
        self.cart = cart
        self.status = 'Pending'
        # self.order_id = None
        self.order_id = str(uuid.uuid4())[:8]
        self.total_amount = cart.total_price()
        self.order_date = datetime.now()
    
    def process_payment(self, payment_method):
        """
        Processes the payment for the order.
        Args:
            payment_method (str): The payment method used by the customer.
        Returns:
            bool: True if payment is successful, False otherwise. 
        """
        # Simulate payment processing (you could integrate with a real payment gateway)
        if payment_method:
            print(f"Processing payment using {payment_method}....")
            return True # Assume payment is successful
        return False
    
    def complete_order(self, payment_method):
        """
        Completes the order, updating the status and adjusting stock levels.
        Args:
            payment_method (str): The payment method used for completing the order.
        Returns:
            str: Confirmation message after order completion. 
        """
        if self.process_payment(payment_method):
            self.status = 'Completed'
            for item in self.cart.items:
                item.product.update_stock(item.quantity)
            self.cart.clear_cart()
            return f"Order {self.order_id} completed successfully."
        else:
            self.status = 'Failed'
            return f"Order {self.order_id} failed. Payment unsuccessful."
        # for item in self.cart.items:
            # item.product.update_stock(item.quantity)
    
    def generate_invoice(self):
        """
        Generates an invoice for the order.
        Returns:
            str: A detailed invoice of the order. 
        """
        invoice = f"Order ID: {self.order_id}, Date: {self.order_date}\n"
        invoice += f"Customer: {self.cart.customer.name}\n"
        invoice += "Items Purchased: \n"
        for item in self.cart.items:
            invoice += f"{item.product.name} (x{item.quantity}) - ${item.calculate_price():.2f}\n"
        invoice += f"Total Amount: ${self.total_amount:.2f}, Status: {self.status}\n"
        return invoice  
    def __str__(self):
        """
        Returns a String representation of the order.
        Returns:
            str: Summary of the order details. 
        """
        return f"Order for Order ID: {self.order_id} | {self.cart.customer.name} | Total: ${self.total_amount}, Status: {self.status}"

# Usage:
customer = Customer("Mahmud", "mahmud@gmail.com", "Dog4Legs", "01764810384", "Lalmonirhat")
cart = Cart(customer)
product1 = Product("Laptop", 999.99, "High-end laptop", electronics)
cart.add_item(product1, 1)
order = Order(cart)
print(order)
print(order.complete_order("Credit Card"))
print(order.generate_invoice())
