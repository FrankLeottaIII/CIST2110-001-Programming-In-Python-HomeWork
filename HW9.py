# HW9.py
# Author: Frank R. Leotta III

# This homework will expand upon the code for Lab11.py. If you did not complete Lab11.py, you should do so before attempting this homework.

# Copy the code from Lab11.py into this file 1-11. I'll add some comments to help you out.


### INSERT CODE FROM LAB11.PY HERE Questions 1-11###
import tabulate #pip install tabulate first if need be.

#note: i am altering it to give it typehinting... 
class Product:
    def __init__(self, name: str, price: float, product_id: str):# self is ref that varible  regular and optional varibles. assume name product price is required
        self.name: str = name # self is a ref to the object, name is a varible, self.name is a attribute
        self.price: float = price 
        self.product_id: str = product_id

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
# 1. Create a method called add_product_to_customer_cart that takes in a Customer object and a Product object. 
# The method should add the product to the customer's cart. 
# The method should also print out the product that was added and the customer's name.
# Hint: You can use the add_to_cart method from the Customer class.
# Hint2: This method does not need to be in a class. 
# It should be a regular function that takes in a Customer object and a Product object.
def add_product_to_customer_cart(customer: Customer, product: Product)-> str: # self is the customer, product is the product
    """Summery:
        This function adds a product to a customer's cart.  It also prints out the product that was added and the customer's name in a string.
    
    Parameters:
        customer (Customer): The customer object.
        product (Product): The product object.
    
    Returns:
        str: the product that was added and the customer's name in a string.
    
    
    """
    customer.add_to_cart(product) # add the product to the cart list
    return print(f"{product.name} was added to {customer.name}'s cart") # print out the product that was added and the customer's name.

# 2. Create a method called remove_product_from_customer_cart that takes in a Customer object and a Product object. 
# The method should remove the product from the customer's cart. 
# The method should also print out the product that was removed and the customer's name.
# Hint: You can use the remove_from_cart method from the Customer class.
# Hint2: This method does not need to be in a class. 
# It should be a regular function that takes in a Customer object and a Product object.
def remove_product_from_customer_cart(customer: Customer, product: Product)-> None: # self is the customer, product is the product
    """Summery:
        This function removes a product from a customer's cart.  It also prints out the product that was removed and the 
        customer's name in a string.
        
    Parameters:
        customer (Customer): The customer object.
        product (Product): The product object.
    
    Returns:
        None
        
        
        """
    customer.remove_from_cart(product) # remove the product from the cart list
    print(f"{product.name} was removed from {customer.name}'s cart") # print out the product that was removed and the customer's name.

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


def check_customer_in_store(customer: Customer) -> bool:
    """Summary:
    This function checks if a customer is in the store.

    Parameters:
    customer (Customer): The customer object.

    Returns:
    bool: True if the customer is in the store, False otherwise.
    """
    if customer in store.customers:
        return True
    else:
        return False

def check_product_in_store(product: Product) -> bool:
    """Summary:
    This function checks if a product is in the store.

    Parameters:
    product (Product): The product object.

    Returns:
    bool: True if the product is in the store, False otherwise.
    """
    if product in store.products:
        return True
    else:
        return False
    
# def should_banish_to_menu(varible) -> None:
#     """Summary:
#     This function prints out a message and then returns to the menu.

#     Parameters:
#     Varible: The varible that is being checked to see if it is true or false

#     Returns:
#      if True, prints string and None, 
#      If False, menu() function.
#     """
#     if varible == True:
#         print("...authenticated... beep boop")
#         return None
#     if varible == False:
#         return False


# The menu function should return the user's choice as an integer.
# Hint: Print out the menu and then use the input() function to get the user's choice.
#nOTE
def menu()-> int:
    """Summery:
        This function displays a menu and returns the user's choice as an integer.  The menu is displayed using the input() function.  The input is then checked to make sure that it is a valid input.  If the user enters an invalid input, it will ask the user to enter a valid input.  The code is encapulated in a try and except block to catch any errors... and will run normally if there is errors.  This funtion is a crazy train, it will not stop for anything.  If this funtion breaks, the whole program will turn to useless code, floating in the void... until the program is restarted I guess.


    Parameters:
        None

    Returns:
        int: The user's choice as an integer.
    """
    try:
        print("welcome to the store Menu. What would you like to do?")
        print("press 1 to Add Product")
        print("press 2 to Add Customer")
        print("press 3 to Add Product to Customer's Cart")
        print("press 4 to Remove Product from Customer's Cart")
        print("press 5 to Display Products")
        print("press 6 to Display Customers")
        print("press 7 to Display Customer's Cart")
        choice = input("What would you like to do?: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7"]
        while choice not in choice_list:
            print("NOT COOL MAN!!!... sorry. please try again...")
            choice = input("What would you like to do?: ")
        return choice
    except Exception as e:
        print(f"error:{e}, taking you back to the menu.")
        print("")
        print("welcome to the store Menu. What would you like to do?")
        print("press 1 to Add Product")
        print("press 2 to Add Customer")
        print("press 3 to Add Product to Customer's Cart")
        print("press 4 to Remove Product from Customer's Cart")
        print("press 5 to Display Products")
        print("press 6 to Display Customers")
        print("press 7 to Display Customer's Cart")
        choice = input("What would you like to do?: ")
        choice_list = ["1", "2", "3", "4", "5", "6", "7"]
        while choice not in choice_list:
            print("NOT COOL MAN!!!... sorry. please try again...")
            choice = input("What would you like to do?: ")
        return choice

 


###########333
#4 though 7 options in menu



##############3
#check imput funtions
def add_price_now()-> float:
    """Summery:
        This funtion gets the price of the product from the user and returns it as a float.  It checks to make sure that the user only enters numbers and decimals.  It also checks to make sure that the user only enters positive numbers.  If the user enters a negative number, it will ask the user to enter a positive number.  If the user enters a letter, it will ask the user to enter a number.
        
    Parameters:
        none
        
    Returns:
        float: The price of the product.
        
        
        """
    try:
        print("ok, now lets enter the whole doller amount and cent amount for the item ")
        print("do not use decimal, I will insert it for you.")
        dollar = input("Please enter the dollar amount of the item: ") 
        switch = True
        while switch == True:
            if dollar.isalpha() != True:
                switch = False
            else:
                print("Please only use positive numbers.")
                dollar = input("Please enter the product price: ")
        print("ok, now lets enter the cent amount for the item ")
        print("do not use decimal, as that would be silly.")
        cent = input("Please enter the cent amount of the item: ")
        black_gum = True
        while black_gum == True:
            if cent.isalpha() != True:
                black_gum = False
            else:
                print("Please only use positive numbers.")
                cent = input("Please enter the product price: ")
        dollar = abs(int(dollar))
        cent = abs(int(cent))
        price = str(f"{dollar}.{cent}")
        price = float(price)
        print(f"the price of the product is ${price}, nice.")
        return price
    except Exception as e:
        print(f"error:{e}, not cool man")


def customer_check(customer_name: str, store: Store)-> str:
    """Summery:
        This function checks to see if the customer is in the store object.  If the customer is not in the store object, it will ask the user to enter a customer that is in the store.  If there are no customers in the store, it will tell the user that there are no customers in the store and return False. If the customer is in the store, the function will return the name of the customer.  If the user enters "quit", it will return False
        
    Parameters:
        customer_name (str): The name of the customer.
        store (Store): The store object.
        
    Returns:
        str: The name of the customer.
        False: If there are no customers in the store.
        """
    if customer_name not in store.customers or store.customers == [] or customer_name == "quit":
        print("There are no customers in the store.")
        return False
    else:
        return customer_name

def product_check(product_name: str, store: Store)-> str:
    """Summery:
        This function checks to see if the product is in the store object.  If the product is not in the store object, it will ask the user to enter a product that is in the store. If there are no products in the store, it will tell the user that there are no products in the store and return none. The function will return the name of the product. If the user enters "quit", it will return  None.
        
    Parameters:
        product_name (str): The name of the product.
        store (Store): The store object.
        
    Returns:
        str: The name of the product.
        False: If there are no products in the store.
        False: If the user enters "quit".
        
        """
    if product_name not in store.products or store.products == []:
        return False
    else:
        return product_name


def imput_product_id()-> str:
    """Summery:
        This function gets the product id from the user and returns it as a string, since product identifiers can have letters and numbers in them.  It strips the white spaces off of the user input, and returns the product id as a string.
        
        Args:
            None

        Returns:
            str: The product id.
        """
    product_id = input("Please enter the product id: ").strip()
    product_id = str(product_id)
    return product_id

    



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
    store = Store()
    waldo = True
    while waldo == True:
        imput = menu()
        if imput == "0":# exit program
            try:
                print("Exiting Program...")
                quit()
            except Exception as e: #this is a catch all, it will catch any error
                print(f"error:{e}, taking you back to the menu.")  
        elif imput == "1":
            try:
                print("Add Product selected")
                print("Please enter the product information in the following prompts.")
                name = str(input("Please enter the product name: ")).upper()
                price = add_price_now()
                product_id = imput_product_id()
                store.add_product(Product(name, price, product_id))
            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")
        elif imput == "2":
            try:
                print("Add Customer")
                name = str(input("Please enter the customer name: ")).capitalize()
                customer_id = input("Please enter the customer id: ")
                store.add_customer(Customer(name, customer_id))
            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")
        elif imput == "3":
            try:
                print("Add Product to Customer's Cart")
                customer_name = str(input("Please enter the customer name: ")).capitalize()
                customer_string = customer_check(customer_name, store)
                if customer_string != False:     
                    product_name = str(input("Please enter the product name: ")).upper()
                    product_string = product_check(product_name, store)
                    if product_string != False:
                # customer = store.find_customer(customer_name)
                # product = store.find_product(product_name)
                        add_product_to_customer_cart(customer_string, product_string)
                    elif product_string == False:
                        print("Product not found!!!")
                elif customer_string == False:
                    print("Customer not found!!!")
            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")   
        elif imput == "4":
            try:
                print("Remove Product from Customer's Cart")
                customer_name = input("Please enter the customer name: ")
                customer_string = customer_check(customer_name, store)
                if customer_string != False:
                    product_name = input("Please enter the product name: ")
                    product_string = product_check(product_name, store)
                    if product_string != False:
                        remove_product_from_customer_cart(customer_string, product_string)
                    elif product_string == False:
                        print("Product not found!!!")
                elif customer_string == False:
                    print("Customer not found!!!")
            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")
        elif imput == "5":
            try:
                print("Display Products")
                store.display_products()
            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")
        elif imput == "6":
            try:
                print("Display Customers")
                store.display_customers()
            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")
        elif imput == "7":
            try:
                print("Display Customer's Cart")
                customer_name = str(input("Please enter the customer name: ")).capitalize()
                shopper = customer_check(customer_name, store)
                if shopper != False:
                    shopper.display_products_pretty()
                elif shopper == False:
                    print("Customer not found!!!")

            except Exception as e:
                print(f"error:{e}, taking you back to the menu.")




if __name__ == "__main__":
    """
    Leave this code at the bottom of the file. It will call the main function when you run the file.
    """

    main()
