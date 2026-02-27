
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if ingredients["bread"] > self.machine_resources["bread"]:
            print("Sorry, there is not enough bread")
            return False
        elif ingredients["ham"] > self.machine_resources["ham"]:
            print("Sorry, there is not enough ham")
            return False
        elif ingredients["cheese"] > self.machine_resources["cheese"]:
            print("Sorry, there is not enough cheese")
            return False
        else:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon Appetit!")