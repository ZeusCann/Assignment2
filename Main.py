import Data
from sandwich_makerr import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = Data.resources
recipes = Data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        user_choice = input("What would you like? (small/medium/large): ").lower()

        if user_choice == "off":
            print("Shutting down machine.")
            break

        # Validate choice
        if user_choice not in recipes:
            print("Invalid option. Please choose small, medium, or large.")
            continue

        # Get sandwich data
        sandwich_data = recipes[user_choice]
        ingredients = sandwich_data["ingredients"]
        cost = sandwich_data["cost"]

        # Step 1: Check resources
        if not sandwich_maker_instance.check_resources(ingredients):
            continue

        # Step 2: Process coins
        inserted_money = cashier_instance.process_coins()

        # Step 3: Handle transaction
        if cashier_instance.transaction_result(inserted_money, cost):
            sandwich_maker_instance.make_sandwich(user_choice, ingredients)

if __name__=="__main__":
    main()