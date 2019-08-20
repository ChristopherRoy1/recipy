

class FoodItem:
    def __init__(self, item_name, item_unit):
        self.item_name = item_name
        self.item_unit = item_unit

class FoodOrder:
    def __init__(self, food_item, price, quantity, frequency=1):
        self.price = price
        self.food_item = food_item
        self.quantity = quantity



class FoodVendor:
    def __init__(self, name):
        self.name = name
        self.contacts = []


class Recipe:
    def __init__(self, title):
        self.ingredients = []
