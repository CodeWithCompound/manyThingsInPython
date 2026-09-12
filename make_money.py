import sys


class Game:
    def __init__(
        self,
        running: bool = True,
        money: float = 0.0,
        income: float = 0.1,
        income_mult: float = 1.0,
    ):
        self.running = running
        self.money: float = money
        self.income: float = income
        self.income_mult: float = income_mult

        self.upgrade_income_cost: float = self.income * (20 + self.income)
        self.upgrade_income_mult_cost: float = self.income * (20 * self.income_mult)

        self.first_load: bool = True

    def make_money(self):
        self.money = self.money + self.income * self.income_mult

    def upgrade_income(self):
        if self.upgrade_income_cost <= self.money:
            self.income = self.income + 0.1
            self.money = self.money - self.upgrade_income_cost
            self.upgrade_income_cost = self.income * (20 + self.income)

    def upgrade_income_mult(self):
        if self.upgrade_income_mult_cost <= self.money:
            self.income_mult = self.income_mult + 0.1
            self.money = self.money - self.upgrade_income_mult_cost
            self.upgrade_income_mult_cost = self.income * (20 * self.income_mult)


def u_sure(what: str) -> bool:
    while True:
        print(f"are you sure that you want to {what}? (y/n)")

        cmd = input().strip().lower()

        if cmd == "y":
            return True
        elif cmd == "n":
            print("okay. maybe next time")
            return False


# i should format the below better
def welc():
    print(
        "Welcome to this little game. please do not expect anything other than a waste of time"
    )
    print("v 0.0.2")
    print("simply a little thing i did to pass time and practice.")
    help()


def help():
    print(
        "use + to make money once\n use ++ to make money 10 times\n use ? to see all stats\n u1 and u2 for upgrading your income and income multiplicator\nuse x! to quit"
    )


instance: Game = Game()
while True:
    if instance.first_load:
        welc()
        instance.first_load = not instance.first_load

    cmd = input().strip().lower()

    if cmd == "help":
        help()

    elif cmd == "+":
        instance.make_money()

    elif cmd == "u1":
        if u_sure("upgrade your income?"):
            # add cost of upgrade in the question
            old = instance.income
            instance.upgrade_income()
            print(f"old income: {old}")
            print(f"new income: {instance.income}")
        else:
            continue

    elif cmd == "u2":
        if u_sure("upgrade your incomes multiplyer"):
            # add cost of upgrade in the question
            old = instance.income_mult
            instance.upgrade_income_mult()
            print(f"old income *: {old}")
            print(f"new income *: {instance.income_mult}")

        else:
            continue

    elif cmd == "++":
        for _ in range(10):
            instance.make_money()

    elif cmd == "?":
        print(f"\nincome: {instance.income}")
        print(f"income_mult: {instance.income_mult}")
        print(f"\ncost1: {instance.upgrade_income_cost}")
        print(f"cost2: {instance.upgrade_income_mult_cost}i\n")

    elif cmd == "x!":
        sys.exit("bye bye.")

    print(f"$ = {instance.money:.2f}")
