import mysql.connector

db=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "indices_bd"
)

#print(type(db))
# cursor = db.cursor()
# cursor.execute("show tables")
# print(cursor)
# for dbs in cursor:
#     print(dbs)

cursor = db.cursor()
cursor.execute("show tables")
print(cursor)
for dbs in cursor:
     print(dbs)