import csv  # reads the csv file


class Item:
    # class attributes belongs to class, it can be accessed through instance level
    payRate = 0.8  # the pay rate after 20% discount
    all = []  # a list to capture all instances

    def __init__(self, name: str, price: float, quantity=0):  # when qty is 0, the default itself expects an integer
        # testing the received values
        assert price >= 0, "price is negative"
        assert quantity >= 0, "quantity recieved is negative"  # adding messages to assertion

        # assign to self object
        self.name = name  # instance attributes
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculatePrice(self):  # self passed as the first argument takes in the
        # object itself, so the method has access to all the attributes of that object
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * self.payRate  # to use the class attribute, you need to use class
        # like Item.payRate, but its best practice to use self.payRate incase the class attribute needs
        # to be changed.

    # instead of creating objects from the python file, we can create objects using CSV
    # to do that, we can instantiate from the class, without creating instances outside the class
    # we need to use a class method for it, using a decorater, which changes a functions behaviour
    @classmethod
    # the cls, class itself is passed as the first argument by default
    def instantiateFromCSV(cls):  # we aren't passing self cause we're not creating any objects that get passed
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    # we are using context manager to open csv in read variable f, using csv.
    # read the csv as a dict, store the reader in list format.
    # go through the list, create objects by reading them from CSV

    @staticmethod # we never send objects as argument to static method
    def is_integer(num): # static method is like isolated function
        if isinstance(num, float):
            # remove the decimal point
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # repr -> represents your objects, it helps you to control how the object is displayed when printed
    def __repr__(self):  # magic method to make good sense of the instances when printed
        return f"Item(`{self.name}`, {self.price}, {self.quantity})"


Item.instantiateFromCSV()
print(Item.all)

# when do you use static methods? It's like a standlone function outside a class,
# it has nothing to do with an instance. But maybe somewhat related to a class so use a static method


# class method is used to instantiate an instance from a structured data
# static methods do not pass any arguments like self or cls for it.