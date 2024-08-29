
class Category:
    def __init__(self, name, description="", parent=None):
        """
        Initializes a Category object.
        Args:
            name (str): The name of the category.
            description (str, optional): A brief description of the category. Deffault is an empty string.
            parent (Category, optional): The parent category, if this category is subcategory.Default is None.  
        """
        self.name = name
        self.description = description
        self.parent = parent
        self.subcategories = []
        
        if parent:
            parent.add_subcategory(self)
    
    def add_subcategory(self, subcategory):
        """
        Adds a subcategory to the current category.
        Args:
            subcategory (Category): The subcategory to add. 
        """
        self.subcategories.append(subcategory)
    
    def get_full_category_path(self):
        """
        Returns the full path of the category, including parent categories .
        Returns:
            str: The full path of the category.
        """
        if self.parent:
            return f"{self.parent.get_full_category_path()} > {self.name}"
        return self.name
    
    def __str__(self):
        # return self.name
        return self.get_full_category_path()

class Product:
    def __init__(self, name, price, stock, description, category, sku=None, manufacture=None):
        """
        Initializes a Product object.
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            stock (int): The quantity available.
            description (str): A brief description of the product.
            category (Category): The category to which the product belongs.
            sku (str, optional): The stock keeping unit (sku) for the product. Default is None.
            manufacture (str, optional): The manufacturer of the product. Default is None.             
        """
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description
        self.category = category
        self.sku = sku
        self.manufacture = manufacture
    
    def update_stock(self, quantity):
        """
        Updates the stock level for the product.
        Args:
            quantity (int): The quantity to reduce from the stock.
        Raises:
            ValueError: If the quantity exceeds available stock. 
        """
        if quantity > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= quantity
    
    def restock(self, quantity):
        """
        Increases the stock level for the product.
        Args:
            quantity (int): The quantity to increase the stock. 
        """
        if quantity < 0:
            raise ValueError("Restock quantity cannto be negative")
        self.stock += quantity
    def __str__(self):
        """
        Returns a string representation of the product.
        Returns:
            str: A detailed string description of the product. 
        """
        details = f"Product: {self.name}\nCategory: {self.category}\nPrice: ${self.price}\nStock: {self.stock}\n"
        if self.sku:
            details += f"SKU: {self.sku}\n"
        if self.manufacture:
            details += f"Manufacture: {self.manufacture}\n"
        details += f"Description: {self.description}"
        return details
        # return f"{self.name} - {self.category} - ${self.price}"

# Usage:
electronics = Category("Electronics")
smartphones = Category("Smartphone", parent=electronics)
product = Product(
    name="Apple iphone 14",
    price=1000.99,
    stock=10,
    description="Latest iphone model with improved camera and battery life.",
    category=smartphones,
    sku="APL-IP14-BLK",
    manufacture="Apple Inc")
print(product)
product.update_stock(5)
print(f"Stock after update: {product.stock}")
product.restock(20)
print(f"Stock after restock: {product.stock}")

