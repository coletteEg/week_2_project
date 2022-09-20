from abc import ABC,abstractmethod

from pprint import pprint

with open("sample.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        pprint(row)

read_csv("sample.csv")


class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price

my_cupcake_mini = Mini("vanilla", 1.99, "strawberry", "white")
print(my_cupcake_mini.name)
print(my_cupcake_mini.price)
print(my_cupcake_mini.size)

my_cupcake = Cupcake("Banana Nut", 3.99, "Banana", "Vanilla", "Banana creme", True)

my_cupcake.frosting = "Chocolate"
my_cupcake.filling = "Chocolate"
my_cupcake.name = "Triple Chocolate"

my_cupcake.is_miniature = False
print(my_cupcake.is_miniature)

my_cupcake.add_sprinkles("Nilla Wafer crumbs", "Rainbow")

print(my_cupcake.add_sprinkles)

cupcake1 = Regular("Stary Night", 3.99, "Blue Vanilla", "Blue Chocolate chip")
cupcake1.add_sprinkles("White Stars")
cupcake2 = Regular("Nutella", 3.99, "Vanilla", "Nutella Whipped Cream")
cupcake2.add_sprinkles("Strawberry")
cupcake3 = Mini("Blueberry", .99, "Vanilla", "Blueberry cream cheese")
cupcake3.add_sprinkles("Blueberry")
cupcake4= Large("Vanilla", 5.00, "Vanilla", "Buttercream frosting")
cupcake4.add_sprinkles("multi-colored sprinkles")
cupcake5= Mini("Devils food cake", .99, "chocolate", "Devils food frosting")
cupcake5.add_sprinkles("brownie crumbs")

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3,
    cupcake4,
    cupcake5
]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

write_new_csv("sample.csv", cupcake_list)

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)        