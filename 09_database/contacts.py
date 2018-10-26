import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("drop table if exists contacts")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name text, phone integer, email text)")
db.execute("INSERT INTO contacts VALUES('Peter Boldizs',12345678,'peter.boldizs@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Anna Boldizs',87654321,'anna.boldizs@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Marta B Tatar',87654321,'tatar.marta@gmail.com')")
db.execute("INSERT INTO contacts VALUES('David Boldizs','+36-20-2347021','david.boldizs@gmail.com')")

cursor1 = db.cursor()
cursor1.execute("select * from contacts")

print("returns tuple")
for row in cursor1:
    print(row)
cursor1.close()

cursor2 = db.cursor()
cursor2.execute("select name, phone, email from contacts")
for name, phone, email in cursor2:
    print("Name: {} Phone: {} Email: {}".format(name, phone, email))

print("need to query again to re-use cursor")
cursor2.execute("select name from contacts")
for r in cursor2:
    print(r)
    print("-" * 20)

print("fetchall")
cursor2.execute("select * from contacts")
print(cursor2.fetchall())
cursor2.close()

print("using shortcut")
for r2 in db.execute("select * from contacts"):
    print(r2)

print("db info:")
for r1 in db.execute("select * from sqlite_master"):
    print(r1)

db.commit()
db.close()

# print(db.execute("select * from contacts"))
