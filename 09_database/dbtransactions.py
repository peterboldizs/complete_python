import datetime
import sqlite3

import pytz

db = sqlite3.connect('accounts.sqlite')
db.execute("create table if not exists accounts(name text primary key not null, "
           "balance integer not null)")
db.execute("create table if not exists history(time timestamp not null, account text not null, "
           "amount integer not null, primary key(time, account))")


class Account(object):

    @staticmethod
    def _current_time():
        local_time = pytz.utc.localize(datetime.datetime.utcnow())
        return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("select name, balance from accounts where (name = ?)", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row
            print("retrieve record for {}".format(self.name))
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("insert into accounts(name, balance) values (?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("account created for {}".format(name))

    def deposit(self, amount: int) -> int:
        if amount > 0:
            self._save_update(amount)
            print("{} deposited".format(amount))
        return self._balance

    def withdraw(self, amount: int) -> int:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{} withdrawn".format(amount))
            return amount
        else:
            print("invalid amount")
            return 0

    def _save_update(self, amount):
        new_balance = self._balance + amount
        dep_time = Account._current_time()
        try:
            db.execute("update accounts set balance = ? where (name = ?)", (new_balance, self.name))
            db.execute("insert into history(time, account, amount) values(?,?,?)", (dep_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance

    def show_balance(self):
        print("Balance for {} is {}".format(self.name, self._balance))


if __name__ == '__main__':
    peter = Account("Peter", 400)
    marti = Account("Marti", 1000)
    anna = Account("Anna", 1000)
    peter.show_balance()
    peter.deposit(300)
    peter.show_balance()
    marti.withdraw(600)
    marti.show_balance()
    anna.withdraw(200)
    anna.deposit(100)

    db.close()
