class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ₹{self.price}")
product1 = Product("Laptop", 55000)
product2 = Product("Smartphone", 25000)
product1.display()
product2.display()
