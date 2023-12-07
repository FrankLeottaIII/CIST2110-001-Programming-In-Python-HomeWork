# HW9.py
# Author: Frank R. Leotta III

# This homework will expand upon the code for Lab11.py. If you did not complete Lab11.py, you should do so before attempting this homework.

# Copy the code from Lab11.py into this file 1-11. I'll add some comments to help you out.


### INSERT CODE FROM LAB11.PY HERE 1-11###
import tabulate #pip install tabulate first if need be.
class Product:
    def __init__(self, name, price: float, product_id):# self is ref that varible  regular and optional varibles. assume name product price is required
        self.name = name # self is a ref to the object, name is a varible, self.name is a attribute
        self.price = price 
        self.product_id = product_id

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, ID: {self.product_id}" # could tpye haha  you will never get this, its always typing it up in the stirng format


class Customer:
    def __init__(self, name, customer_id): #all of these are required
        self.name = name #diff over time
        self.customer_id = customer_id # diff over time
        self.cart = [] # its going to be the same every time, so no need to pass it in as a paramiter
    
    def __str__(self): #need to pass in self as paramiter
        return f"Customer: {self.name}, ID: {self.customer_id}" # this is a string, not a list, so no brackets, just a string

    def add_to_cart(self, product: Product): # self is the customer, product is the product  #taking a product and add it to cart.  List can hold anything inside of them.  sting as an object is, lists can hold objects. cart can hold product objects inside of it.
            self.cart.append(product) # add the product to the cart class 
            print(f"{product.name} was added to {self.name}'s cart") # print out the product that was added and the customer's name.
   
    def remove_from_cart(self, product: Product): # self is the customer, product is the product
        self.cart.remove(product) # remove the product from the cart list
        print(f"{product.name} was removed from {self.name}'s cart") # print out the product that was removed and the customer's name.

    def checkout(self): # self is the customer
        total = 0 # create a total variable and set it to 0
        for product in self.cart:
            total += product.price  #all way upp  here the products have price associated with them, so you can add them up... remember datetime having . associated with that headach only different
        print(f"{self.name}'s total is {total}") # print out the customer's name and the total price of all the products in the cart. #api in website, take the total charge and add taxes to it. 
        self.cart = [] # empty the cart list

    def display_products(self): # self is the customer  
        print(f"{self.name}'s cart:") # print out the customer's name and the total price of all the products in the cart.  Self.name is whatever funtion you are currently in
        for product in self.cart:
            print(product)

    def display_products_pretty(self): # self is the customer  
        print(f"{self.name}'s cart:") # print out the customer's name and the total price of all the products in the cart.  Self.name is whatever funtion you are currently in
        print(tabulate.tabulate(
        [{"Name": Product.name, "Price": Product.price, "ID": Product.product_id} for Product in self.cart], 
        headers="keys", tablefmt="fancy_grid"))

class Store:      
    def __init__(self): # self is the store
        self.products = [] # this should be a list that contains Product objects.
        self.customers = [] # this should be a list that contains Customer objects.

    def add_product(self, product: Product): # self is the store, product is the product
        self.products.append(product) # add the product to the products list
        print(f"{product.name} was added to the store") # print out the product that was added and the store name.

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name} was added to the store")

    def display_products(self):
        print("Products:")
        for product in self.products:
            print(product)

    def display_customers(self):
        print("Customers:")
        for customer in self.customers:
            print(customer)

store = Store() # create a store object called store
product1 =  Product("iPhone 12", 799.99, 1)
product2 = Product("iPhone 12 Pro", 999.99, 2) # this is how you create a product object
product3 = Product("iPhone 12 Pro Max", 1099.99, 3) # this is how you create a product object
customer1 = Customer("John", 1) # this is how you create a customer object
customer2 = Customer("Jane", 2)

### END CODE FROM LAB11.PY ###

# START OF HOMEWORK Questions
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. The method should add the product to the customer's cart. The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.


# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. The method should remove the product from the customer's cart. The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. It should be a regular function that takes in a Customer object and a Product object.


# 3. Create a menu function that will display the following menu:
# 1. Add Product
# 2. Add Customer
# 3. Add Product to Customer's Cart
# 4. Remove Product from Customer's Cart
# 5. Display Products
# 6. Display Customers
# 7. Display Customer's Cart
# 8. Checkout
# 9. Exit


# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.

# 4. Create a main function that will call the menu function and then call the appropriate methods based on the user's choice. The main function should be in a while loop that will continue to call the menu function until the user enters 0 to exit the program.
# IMPORTANT: The main function should create a Store object and then call the appropriate methods on the Store object. Without the Store object, you will not be able to add products or customers.
# IE main function should look something like this:
# def main():
#     store = Store()
#     while True:
#         choice = menu()
#         if choice == 1:
#             # call add_product method
#         elif choice == 2:
#             # call add_customer method
#         elif choice == 3:
#             # call add_product_to_customer_cart method
# ETC...

# Hint 1: If you need informtation from the user about a product or customer, you can ask for it in the main function and then pass it to the appropriate method. Don't be afraid to use input() in the main function.
# Hint 2: Some of the methods take in a Product object or a Customer object. You will need to create a Product object or a Customer object before calling the method. You can create a Product object or a Customer object in the main function and then pass it to the appropriate method.
# Hint 3: You can use the display_products and display_customers methods to help you out.
# Hint 4: Some Methods take in parameters. You will need to pass in the correct parameters to the method. For example, the add_product method takes in a Product object. You will need to pass in a Product object to the method. You can pass in a Product as a parameter.
# IE. store.add_product(product) where product is a Product object.
# store.add_product(Product(name, price, product_id))
# You can either ask the user for the name, price, and product_id or you can hard code it in the main function.


def main():
    pass  # remove this line when you start working on the main function


if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()
