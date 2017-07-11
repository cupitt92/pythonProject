import sqlite3

# Declare connection to database and create cursor.
# If database already exists it will connect otherwise it will create it. 
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

# Create a table by executing sql columns specified as parameters of table. 
def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

# Insert data example
def enter_data_hard_coded():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    # Equivalent to saving
    conn.commit()

# Insert dynamic data
def enter_dynamic_data():
    Lang = input("What Language? ")
    Version = float(input("What Version? "))
    Skill  = input("What skill level? ")
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (Lang, Version, Skill))
    conn.commit()
    
# Read from db example Limit
def read_from_database():
    sql = "SELECT * FROM example LIMIT 2"
    for row in c.execute(sql):
        print(row)

# Update example
def update_database():
    sql = "UPDATE example SET Skill = 'beginner' WHERE skill = 'Beginner'"
    c.execute(sql)
    conn.commit()
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)

# Delete example
def delete_data():
    sql = "DELETE FROM example WHERE Skill = 'Beginner'"
    c.execute(sql)
    conn.commit()
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)


# Read from db example
def read_from_dynamic_database():
    what_skill = input("What skill level are we looking for?")
    what_lang = input("What language? ")

    sql = "SELECT * FROM example WHERE Skill = ? AND Language = ?"
    for row in c.execute(sql, [(what_skill),(what_lang)]):
        print(row)
        

# Call functions here to run them.
delete_data()

#Close connection to db.
conn.close()
