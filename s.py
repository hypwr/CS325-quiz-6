

class Item: # Responsibility: contains item name and cost
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost

    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost

class Order: # Responsibility: contains items in the order
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
    
    def get_items(self):
        return self.items

class CustomerInfo: # Responsiblity: contains customer info
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_name(self):
        return self.name
    
    def update_name(self, new):
        self.name = new
    
    def get_address(self):
        return self.address
    
    def update_name(self, address):
        self.address = address

class TotalCost: # Responsiblity: calculate the total with taxes and discounts
    def __init__(self, taxRate, discounts, order):
        self.total = 0
        self.rate = taxRate # rate should be given in decimal form, not percentage.
        self.discount = discounts # discount must be a dollar amount, not a percentage.
        self.order = order

    def get_gross_cost(self):
        self.total = 0
        items = self.order.get_items()
        for item in items:
            cost = item.get_cost()
            self.total = self.total + cost
        return self.total
    
    def get_tax(self):
        tax_total = self.total * self.rate
        return tax_total
    
    def get_discount(self):
        discounted_price = self.total - self.discount
        return discounted_price
    
    def get_total(self):
        total = self.get_gross_cost() + self.get_tax() - self.get_discount()
        return total

class ValidateOrder: # Responsibility: validate the order and the customer address to see if it can be shibbed
    def __init__(self, order, database, customer):
        self.order = order
        self.data = database
        self.customer = customer

    def link_database(self):
        #link the database
        print("Connection made.")

    def validateOrder(self):
        for item in self.order.get_items():
            # check if items in the order are avalible in the database
            if(item != self.data): # assume this compares to all the items in the database
                return False, item
                # if its not found, return False and what item isn't valid
        return True
    
    def validateCustomer(self):
        status = True
        #check if the customers address is able to be shipped to/a valid address
        #if not, set status to false
        return status
    
    def get_validation_message(self):
        if(self.validateCustomer() and self.validateOrder()):
            print("Order Valid!")
        elif(self.validateCustomer()==False):
            print("Order Invalid, Unable to Validate Address")
        else:
            print("Order Invalid, Unable to Validate All Items",self.validateOrder())
    
class OrderComfirmation: # Responsibility: send order confirmation email
    def __init__(self, email_system):
        self.email_system = email_system

    def send_confirmation_email(self, order, cost, email):
        items = order.get_items()
        # include the items, total, and shipping address
        print("Order successfully made!")
        print("Total:",cost)
        for item in items:
            print(item.get_name())
        # self.email_system.send_email(email)

class UpdateInventory: # Responsibility: remove ordered items from the database
    def __init__(self, database, order):
        self.data=database
        self.order=order

    def link_database(self):
        #link the database
        print("Connection made.")
        
    def update_database(self):
        for item in self.order.get_items():
            #remove the item from the database
            print("Item removed from database.")

def main():
    database = 'mydatabase'
    order1 = Order()
    egg = Item("Egg",0.99)
    bacon = Item("Bacon",5.50)
    cheese = Item("Cheese",3.33)

    order1.add_item(egg)
    order1.add_item(bacon)
    order1.add_item(cheese)
    
    customer = CustomerInfo("Jack","123 Street St, Big Town, USA")
    order1_cost = TotalCost(0.05, 5, order1)
    cost = order1_cost.get_total()
    valid = ValidateOrder(order1, database, customer)
    valid.link_database()
    valid.get_validation_message()
    # should be an if statement here seeing if the order is valid, however with the current lack of info, every order will be valid
    confirmation = OrderComfirmation('gmail')
    confirmation.send_confirmation_email(order1, cost, "abc@gmail.com")

    inventory = UpdateInventory(database,order1)
    inventory.link_database()
    inventory.update_database()

main()