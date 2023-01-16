import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
    user = "root",
    password = "",
    database = "esa_unggul"
)

mycursor = mydb.cursor()

mycursor.execute("select * from mahasiswa")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
