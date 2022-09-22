from DBClass import Database
from dotenv import load_dotenv
import os

load_dotenv()

db = Database("localhost", "root", os.getenv("password"))

db.create_db(database="test")

# select a DB to use
select_db = """
    USE test;
"""

# execute query
db.execute_query(query=select_db)

create_table = """
    CREATE TABLE IF NOT EXISTS person(
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(30) NOT NULL,
        year VARCHAR(5) NOT NULL
    );
"""


db.execute_query(query=create_table)

insert_query = """
    INSERT INTO person
    VALUE (NULL, 'John Doe', '2022');
"""

# db.execute_query(query=insert_query)

fetch_query = """
    SELECT * FROM person
"""

persons = db.fetch_data(query=fetch_query)

for data in persons:
    print(data)
    
    