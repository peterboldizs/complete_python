import sqlite3

db = sqlite3.connect("contacts.sqlite")

print("query a person")
# p_name = input("enter name:")  # param must be entered as a tuple
p_name = "Peter Boldizs"
query_cursor = db.cursor()
# for r1 in query_cursor.execute("select * from contacts where name = ?", (p_name,)):
for r1 in query_cursor.execute("select * from contacts where name like ?", (p_name,)):
    print(r1)
db.close()

print("query history table 1")
db2 = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
for row in db2.execute("select * from history"):
    local_time = row[0]
    print("{}\t{}".format(local_time, type(local_time)))
db2.close()

print("query history table 2")
db3 = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
for row in db3.execute("select strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') as localtime, "
                       "history.account, history.amount from history order by history.time"):
    print(row)
db3.close()
