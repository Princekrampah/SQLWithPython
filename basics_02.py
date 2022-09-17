from multiprocessing import connection
from mysql import connector
from dotenv import load_dotenv
import os

load_dotenv()

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
        

select_all_students = """
    SELECT *
    FROM student;
"""

all_student_result = list(fetch_data(conn, select_all_students))


for student in all_student_result:
    print(student)


# update
update_student = """
    UPDATE student
    SET lastName = 'UpdatedName'
    WHERE student_id = 1;
"""
execute_query(conn, update_student)

all_student_result = list(fetch_data(conn, select_all_students))

for student in all_student_result:
    print(student)

   
# Delete functionality
delete_student = """
    DELETE FROM student
    WHERE student_id = 1;
"""
 
execute_query(conn, delete_student)

all_student_result = list(fetch_data(conn, select_all_students))

for student in all_student_result:
    print(student)
 
   