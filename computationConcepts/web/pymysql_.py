import pymysql
#   This module is used to connect to and work with a MySQL server. One can
# execute all the regular SQL commands with it.

# # connecting to the server
# connection = pymysql.connect (
#     host = "192.168.1.19",
#     user = "pythonProgram",
#     passwd = "woodensword",
#     db = "example"
#     )
# cursor = connection.cursor()

# # closing conenctions
# cursor.close()
# connection.close()




# # Get the server version data
# connection = pymysql.connect(host = "192.168.1.19", user = "pythonProgram", passwd = "woodensword", db = "example")
# cursor = connection.cursor()

# cursor.execute ("SELECT VERSION()")
# row = cursor.fetchone()
# print("server version:", row[0])

# cursor.close()
# connection.close()




# # Fetch all the data from the 'numbers' table and print it all out
# connection = pymysql.connect(host = "192.168.1.19", user = "pythonProgram", passwd = "woodensword", db = "example")
# cursor = connection.cursor()

# cursor.execute("SELECT * FROM numbers")
# for item in cursor.fetchall():
#     print(item)

# cursor.close()
# connection.close()




# Create a table and populate it
# connect
connection = pymysql.connect(host = "192.168.1.19", user = "pythonProgram", passwd = "woodensword", db = "example")
cursor = connection.cursor()

# create table
cursor.execute ("drop table if exists employee") # produces error if there is no table, but not a screeching halt
sql_command = """
create table employee ( 
    staff_number integer primary key, 
    fname varchar(20), 
    lname varchar(30), 
    gender char(1), 
    joining date,
    birth_date date);
"""
cursor.execute(sql_command)

# populate table
staff_data = [
    ("William", "Shakespeare", "m", "1961-10-25"),
    ("Frank", "Schiller", "m", "1955-08-17"),
    ("Jane", "Wall", "f", "1989-03-14")
    ]

format_str = """
insert into employee (
    staff_number, 
    fname, 
    lname, 
    gender, 
    birth_date) 
values (
    {staff_no}, 
    '{first}', 
    '{last}', 
    '{gender}', 
    '{birthdate}'
);"""
for staff, p in enumerate(staff_data):
    sql_command = format_str.format(
        staff_no=staff, 
        first=p[0], 
        last=p[1], 
        gender=p[2], 
        birthdate = p[3]
    )
    cursor.execute(sql_command)

# commit changes
connection.commit()

# disconnect
cursor.close()
connection.close()