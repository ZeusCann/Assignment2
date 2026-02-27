class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = float(input("How many dollars?: "))
        half_dollars = float(input("How many half dollars?: ")) * 0.5
        quarters = float(input("How many quarters?: ")) * 0.25
        nickels = float(input("How many nickels?: ")) * 0.05
        payment = dollars + half_dollars + quarters + nickels
        return payment

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, there is not enough money..")
            return False

        change = coins - cost
        print(f"Here's your change: ${change:.2f}")
        return True