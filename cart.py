
from user import Customer
from product import Product, smartphones, electronics
class CartItem:
    """
    Initializes a CartItem object.
    Args:
        product (Product): The product associated with the cart item.
        quantity (int): The quantity of the product. 
    """
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def calculate_price(self):
        """
        Calculates the botal price for the cart item.
        Returns:
            float: The total price of the product multiplied by its quantity. 
        """
        return self.product.price * self.quantity

    def __str__(self):
        """
        Returns a string representation of the cart item.
        Returns:
            str: The product name, quantity, and total price. 
        """
        return f"{self.product.name} (x{self.quantity}) - ${self.calculate_price():.2f}"
class Cart:
    def __init__(self, customer):
        """
        Initializes a Cart object.
        Args:
            customer (Customer): The customer who owns the cart. 
        """
        self.customer = customer
        self.items = []
    
    def add_item(self, product, quantity):
        """
        Adds a product to the cart.
        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product. 
        """
        # Check if the product is already in the cart
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return 
        # If not, add a new CartItem
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)
    
    def remove_item(self, product_name):
        """
        Removes a product from the cart by name.
        Args:
            product_name (str): The name of the product to remove. 
        """
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
            return
    
    def total_price(self):
        """
        Calculates the total price of all items in the cart.
        Returns:
            float: The total price of all cart items. 
        """
        price = 0
        for item in self.items:
            price += item.calculate_price()
        return price
    
    def view_cart(self):
        """
        Displays the contents of the cart.
        Returns:
            str: A formatted string of all cart items and their total price. 
        """
        if not self.items:
            return "Your cart is empty."
        for item in self.items:
            cart_contents = "".join(str(item))
        return f"Cart Contents: {cart_contents} Total: ${self.total_price():.2f}"
    
    def __str__(self):
        """
        Returns a string representation of the cart.
        Returns:
            str: The customer's name and the total price of the cart. 
        """
        return f"Cart for {self.customer.name} - Total: ${self.total_price():.2f}"

# Usage:
customer = Customer("Mahmud", "mahmud@gmail.com", 'Dog4logs', '01764810384', 'Lalmonirhat')
iphone = Product('iphone 14', 1000.99, 25, 'Latest iphone model', smartphones)
laptop = Product('MacBook Pro', 1000.99, 25, "Apple's flagship laptop", electronics)
cart = Cart(customer)
cart.add_item(iphone, 1)
cart.add_item(laptop, 2)
print(cart.view_cart())
cart.remove_item('iphone 14')
print(cart.view_cart())
