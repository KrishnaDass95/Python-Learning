class Item:
    # class attributes belongs to class, it can be accessed through instance level
    payRate = 0.8 # the pay rate after 20% discount
    all = [] # a list to capture all instances
    def __init__(self, name: str, price: float, quantity=0): # when qty is 0, the default itself expects an integer
        # testing the received values
        assert price >= 0, "price is negative"
        assert quantity >= 0, "quantity recieved is negative" # adding messages to assertion

        # assign to self object
        self.name = name   # instance attributes
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculatePrice(self): # self passed as the first argument takes in the
        # object itself, so the method has access to all the attributes of that object
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.payRate # to use the class attribute, you need to use class
        # like Item.payRate, but its best practice to use self.payRate incase the class attribute needs
        # to be changed.

    # repr -> represents your objects, it helps you to control how the object is displayed when printed
    def __repr__(self): # magic method to make good sense of the instances when printed
        return f"Item(`{self.name}`, {self.price}, {self.quantity})"


item1 = Item("Phone",  600, 9)
item2 = Item("Laptop", 2000, 2)

item1.packaging = "cardboard"
print(item1.packaging) # unique attributes for an instance
# print(item1.calculatePrice())
print(Item.payRate) # printing class attribute using class
print(item1.payRate) # using the instance to use the class attribute
# the hierearchy is, instance tries to first search it on instance level, if it fails then it checks class level

# magic attribute to see all the attributes of an object, good for debugging
print(Item.__dict__)
print("----------------------------------------")

item1.applyDiscount()
print(item1.price)

# you have a general discount rate in the class, but what if another item needs 30% and you want to
# preserve the original 20%?
item2.payRate = 0.7 # for item2 instance, we have assigned it's class attribute to 30% discount. It's only for
# item2 discount
item2.applyDiscount()
print(item2.price)

print("-----------------all instances-----------------------")


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
print(Item.all) # handy to see what instances are created

for instance in Item.all: # print names of all instances
    print(instance.name)

print("-----------------all instances-----------------------")
print(item1)  # because of the __repr__ method, it prints this -> Item(`Phone`, 100, 1)
# it has converted the item1 object into some sensible form
