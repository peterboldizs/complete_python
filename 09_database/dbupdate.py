import sqlite3

db = sqlite3.connect("contacts.sqlite")

print("update")
new_email = input("enter email:")
new_phone = int(input("enter phone:"))
# update_sql = "update contacts set email = '{}' where phone = {}".format(new_email, new_phone)
update_sql = "update contacts set email = ? where phone = ?"
update_cursor = db.cursor()
# update_cursor.execute(update_sql)
update_cursor.execute(update_sql, (new_email, new_phone))
print("{} rows updated".format(update_cursor.rowcount))
update_cursor.connection.commit()
update_cursor.close()
print("using shortcut")
for r2 in db.execute("select * from contacts"):
    print(r2)

# db.commit()
db.close()
