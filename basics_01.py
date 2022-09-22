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


# Create DB function
def create_db(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except connector.Error as err:
        print(f"Error: {err}")
        

# create db
query = """
    CREATE DATABASE IF NOT EXISTS tutorialDB_py;
"""
create_db(conn, query)


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


# drop tables to add new data
execute_query(conn, "DROP TABLE course")
execute_query(conn, "DROP TABLE student")

create_student_table = """
    CREATE TABLE IF NOT EXISTS student(
        student_id INT PRIMARY KEY AUTO_INCREMENT,
        firstName VARCHAR(50) NOT NULL,
        lastName VARCHAR(60) NOT NULL UNIQUE,
        homeAddress VARCHAR(80) NOT NULL,
        parentPhone VARCHAR(15) NOT NULL
    );
"""
execute_query(conn, create_student_table)

# create courses
create_course_table = """
    CREATE TABLE IF NOT EXISTS course(
        course_id INT PRIMARY KEY AUTO_INCREMENT,
        course_name VARCHAR(70) NOT NULL UNIQUE,
        course_duration VARCHAR(80) NOT NULL 
    );
"""

# Execute
execute_query(conn, create_course_table)

# Enrollments
create_enrollment_table = """
    CREATE TABLE IF NOT EXISTS enrollment(
      enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
      course_id INT NOT NULL,
      student_id INT NOT NULL
    );
"""


# Execute
execute_query(conn, create_enrollment_table)

# add foreign keys
alter_enrollment_table = """
    ALTER TABLE enrollment
    ADD FOREIGN KEY(course_id) 
    REFERENCES course(course_id) 
    ON DELETE CASCADE;
"""

alter_enrollment_table2 = """
    ALTER TABLE enrollment
    ADD FOREIGN KEY(student_id) 
    REFERENCES student(student_id) 
    ON DELETE CASCADE;
"""

# Execute
execute_query(conn, alter_enrollment_table)
execute_query(conn, alter_enrollment_table2)


# Insert data
insert_teachers = """
    INSERT INTO student(firstName, lastName, homeAddress, parentPhone) VALUES
    ("John", "Doe", "Nairobi 0222", "+2546879989"),
    ("Janet", "Thomas", "Mombasa 3445", "+2549099889");
"""

insert_courses = """
    INSERT INTO course(course_name, course_duration) VALUES
    ("BBIT", 4),
    ("BCOM", 4);
"""

insert_enrollments = """
    INSERT INTO enrollment(course_id, student_id) VALUES
    (1, 2),
    (2, 1)
"""

execute_query(conn, insert_teachers)
execute_query(conn, insert_courses)
execute_query(conn, insert_enrollments)

