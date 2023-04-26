MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


class CoffeeMachine:
    """Creates coffee machine object"""
    def __init__(self) -> None:
        self.profit = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water: {self.resources['water']} ml")
        print(f"Milk: {self.resources['milk']} ml")
        print(f"Coffee: {self.resources['coffee']} g")
        print(f"Money: ${self.profit:.2f}")
        pass

    def off(self):
        exit()

    def process_order(self, drink):
        self.drink = drink
        step_success = self.check_resources()
        if step_success:
            step_success = self.coin_collect()
        if step_success:
            self.dispense_drink()
        del self.drink
        del self.recipe
        pass

    def check_resources(self):
        sufficent_resources = True
        self.recipe = MENU[self.drink]['ingredients']
        for ingredient in self.recipe:
            if self.recipe[ingredient] > self.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                sufficent_resources = False
        return sufficent_resources

    def coin_collect(self):
        def _request(coin):
            submit = input(f"How many {coin}?: ")
            try:
                submit = int(submit) * COINS[coin]
            except Exception:
                print("Please input an integer value.")
                submit = _request(coin)
            return submit

        cost = MENU[self.drink]['cost']
        print(f"{self.drink.title()} costs ${cost:.2f}.")
        print("Please insert coins.")
        total = 0
        for coin in COINS:
            total += _request(coin)
        if total >= cost:
            print(f"Here is ${total - cost:.2f} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that is not enough money. Money refunded.")
            return False

    def dispense_drink(self):
        for ingredient in self.recipe:
            self.resources[ingredient] -= self.recipe[ingredient]
        print(f"Here is your {self.drink} ☕️. Enjoy!")


if __name__ == "__main__":
    is_on = True
    machine = CoffeeMachine()
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        choice = choice.lower()
        if choice == "off":
            is_on = machine.off()
        elif choice == "report":
            machine.report()
        elif choice in MENU:
            machine.process_order(choice)
        else:
            print("Invalid option. Please try again.")
