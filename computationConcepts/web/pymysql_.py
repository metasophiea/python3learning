import pymysql

connection = pymysql.connect (
    host = "192.168.1.19",
    user = "pythonProgram",
    passwd = "woodensword",
    db = "example"
    )
c = connection.cursor()

c.execute("SELECT * FROM numbers")

for item in c.fetchall():
    print(item)