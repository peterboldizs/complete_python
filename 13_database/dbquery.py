import sqlite3

db = sqlite3.connect("contacts.sqlite")

print("query a person")
p_name = input("enter name:")  # param must be entered as a tuple
query_cursor = db.cursor()
# for r1 in query_cursor.execute("select * from contacts where name = ?", (p_name,)):
for r1 in query_cursor.execute("select * from contacts where name like ?", (p_name,)):
    print(r1)

db.close()
