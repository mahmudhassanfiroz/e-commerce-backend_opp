
import hashlib
import uuid
import re
from cart import Cart
from order import Order

class User:
    def __init__(self, name, email, password):
        """ 
        Initializes a User object.
        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password for the user's account.
        """
        self.name = name 
        self.email = email
        self.user_id = str(uuid.uuid4())[:8]
        self.password = self.hash_password(password)
    
    def hash_password(self, password):
        """
        Hashes a password using the md5 for more secure password storage.
        Args:
            password (str): The password to hash.
        Returns:
            str: The hashed password. 
        """
        return hashlib.md5(password.encode()).hexdigest()
    
    def authenticate(self, password):
        """
        Authenticates the user by comparing the provided password with the stored hash.
        Args:
            password (str): The password to authenticate
        Returns:
            bool: True if the password matches, False otherwise.  
        """
        return self.password == self.hash_password(password)
    
    def __str__(self):
        return f"User(name={self.name}, email={self.email}, id={self.user_id})"

class Customer(User):
    def __init__(self, name, email, password, phone, address):
        """ 
        Initializes a Customer objcects, inheriting from User.
        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.
            password (str): The password for the customer's account.
            phone (str): The phone number of the customer.
            address (str): The address of the customer.
        """
        super().__init__(name, email, password)
        self.phone = phone
        self.address = address
        self.cart = Cart(self)
        self.order_history = []
    
    def validate_email(self):
        """
        Validates the customer's email using a regular expression.
        Returns:
            bool: True if the email is valid, False otherwise. 
        """
        pattern = r'^[a-zA-Z0-9_.+=]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, self.email) is not None
    
    # def place_order(self):
        """
        places an order for the items in the customer's cart.
        Returns:
            order: The created order. 
        """
        # if not self.cart.items:
            # return "Cart is empty. Cannot place an order."
        # order = Order(self.cart)
        # self.order_history.append(order)
        # self.cart = Cart(self)
        # return order 
    
    # def view_order_history(self):
        """
        Displays the customer's order history.
        Returns:
            str: A formatted srting of all past orders. 
        """
        # if not self.order_history:
            # return "No orders place yet."
        # history = "".join([f"Order ID: {order.order_id}, Total: ${order.total} for order in self.order_history"])
        # return f"Order History: {history}"
    def view_profile(self):
        """
        Returns the customer's profile information.
        Returns:
            str: A string containing the customer's profile details. 
        """
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, User ID: {self.user_id}"

class Admin(User):
    def __init__(self, name, email, password):
        """
        Initializes an Admin objects, inherithing from User.
        Args:
            name (str): The name of the admin.
            email (str): The email of the admin.
            password (str): The password for the admin's account. 
        """ 
        super().__init__(name, email, password)
        self.role = 'Admin'
    
    def manager_user(self):
        """
        Returns a string indicating the admin's ability to manage users.
        Returns:
            str: A message confirming the admin's management capabilities. 
        """
        return f"Admin {self.name} can manage users."

    def view_profile(self):
        """
        Returns the admin's profile information.
        Returns:
            str: A string containing the admin's profile details. 
        """
        return (f"Admin Name: {self.name}, Email: {self.email}, Role: {self.role}, "f"User ID: {self.user_id}")

# Usage:
customer = Customer("Mahmud", "mahmud@gmail.com", "Dog4legs", "01764810384", "Lalmonirhat")
admin = Admin('Hasan', 'hassan@gamil.com', 'dog4Legs')
print(customer.view_profile())
print(f"Email valid: {customer.validate_email()}")
print(f"Authentication Success: {customer.authenticate('Dog4legs')}")
print(admin.view_profile())
print(admin.manager_user())
