import datetime
import pytz


class Account:
    """
    simple bank account
    """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._tx_list = [(Account._current_time(), balance)]
        print("\naccount created for " + name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._tx_list.append((Account._current_time(), amount))
        self.show_balance()

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self._tx_list.append((Account._current_time(), -amount))
        else:
            print("not enough money")
        self.show_balance()

    def show_balance(self):
        print("Balance: {}".format(self.__balance))

    def show_transactions(self):
        print("*" * 40)
        print("transactions for the account of " + self._name)
        for date, amount in self._tx_list:
            if amount > 0:
                tx_type = "deposit"
            else:
                tx_type = "withdraw"
                amount *= -1
            print("{:6} {} on {} (local time: {})".format(amount, tx_type, date, date.astimezone()))
        print("*" * 40)


if __name__ == '__main__':
    peter = Account("Peter", 0)
    peter.deposit(1000)
    peter.withdraw(300)
    peter.withdraw(1000)
    peter.show_transactions()

    anna = Account("Anna", 500)
    anna.deposit(100)
    anna.__balance = 1000  # nothing happens because of name mangling: '_Account__balance': 300
    anna.withdraw(300)
    anna.show_transactions()
    print(anna.__dict__)
