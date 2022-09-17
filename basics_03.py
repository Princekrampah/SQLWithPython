from multiprocessing import connection
from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

################## Use List To Enter Data Into DB ###################

# Connect to DB function
def connect_to_db(host_name, user_name, password):
    conn = None
    try:
        conn = connector.connect(
            host=host_name, 
            user=user_name, 
            passwd=password
        )
        print("Connection to DB successfully")
    except connector.Error as err:
        print(f"Error: {err}")
        
    return conn

# connect to the database
conn = connect_to_db("localhost", "root", os.getenv("password"))

# Execute query function
def execute_query(conn, query):
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        print("Query execution successful")
    except connector.Error as err:
        print(f"Error: {err}")
        

# Execute query fnc can also be used to run queries

# select a DB to use
select_db = """
    USE tutorialDB_py;
"""

# execute query
execute_query(conn, select_db)


def fetch_data(conn, query):
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except connector.Error as err:
        print(f"Error: {err}")

# Execute query function
def execute_many_query(conn, query, val):
    cursor = conn.cursor()
    
    try:
        cursor.executemany(query, val)
        conn.commit()
        print("Query execution successful")
    except connector.Error as err:
        print(f"Error: {err}")
    
    
# select a DB to use
select_db = """
    USE tutorialDB_py;
"""
# execute query
execute_query(conn, select_db)    


insert_students = """
    INSERT INTO student(firstName, lastName, homeAddress, parentPhone)
    VALUES (%s, %s, %s, %s);
"""   

vals = [
    ("Thomas", "Editton", "NY 225", "+01119867"),
    ("Helena", "Helen", "Dar 223", "+34592309") 
]  
 
execute_many_query(conn, insert_students, vals)

select_all_students = """
    SELECT *
    FROM student;
"""

all_student_result = list(fetch_data(conn, select_all_students))

for student in all_student_result:
    print(student)      
       
        