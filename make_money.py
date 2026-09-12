import sys


class Game:
    def __init__(
        self,
        running: bool = True,
        money: float = 0.0,
        income: float = 0.1,
        income_mult: float = 1.0,
    ):
        self.running: bool = running
        self.money: float = money
        self.income: float = income
        self.income_mult: float = income_mult

        self.upgrade_income_cost: float = self.income * (20 + self.income)
        self.upgrade_income_mult_cost: float = self.income * (20 * self.income_mult)

        self.first_load: bool = True

    def make_money(self) -> None:
        self.money = self.money + self.income * self.income_mult

    def upgrade_income(self) -> None:
        if self.upgrade_income_cost <= self.money:
            old: float = self.income
            self.income = self.income + 0.1
            self.money = self.money - self.upgrade_income_cost
            self.upgrade_income_cost = self.income * (20 + self.income)

            print(f"old income: {old}")
            print(f"new income: {self.income}")
        elif self.money < 0:
            print("how did you get debt?..\n")
        else:
            short: float = self.upgrade_income_cost - self.money
            print(f"you do not have enough money. you are {short:.1f} short\n")

    def upgrade_income_mult(self) -> None:
        if self.upgrade_income_mult_cost <= self.money:
            old: float = self.income_mult
            self.income_mult = self.income_mult + 0.1
            self.money = self.money - self.upgrade_income_mult_cost
            self.upgrade_income_mult_cost = self.income * (20 * self.income_mult)
            print(f"old income *: {old}")
            print(f"new income *: {self.income_mult}")

        elif self.money < 0:
            print("how did you get debt?..\n")
        else:
            short: float = self.upgrade_income_mult_cost - self.money
            print(f"you do not have enough money. you are {short:.1f} short\n")


def u_sure(what: str) -> bool:
    while True:
        print(f"are you sure that you want to {what}? (y/n)")
        cmd: str = input().strip().lower()

        if cmd == "y":
            return True
        elif cmd == "n":
            print("okay. maybe next time")
            return False


# i should format the below better
def welc():
    print(
        "\n................................\nWelcome to this little game. please do not expect anything other than a waste of time"
    )
    print("v 0.0.3")
    print("simply a little thing i did to pass time and practice coding\n")
    help()


def help():
    print(
        "use + to make money once\nuse ++ to make money 10 times\nuse ? to see all stats\nu1 and u2 for upgrading your income and income multiplicator\nuse x! to quit\n"
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
        if u_sure(f"upgrade your income (cost: {instance.upgrade_income_cost:.2f})"):
            instance.upgrade_income()
        else:
            continue

    elif cmd == "u2":
        if u_sure(
            f"upgrade your incomes multiplyer (cost: {instance.upgrade_income_mult_cost:.2f})"
        ):
            instance.upgrade_income_mult()

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
