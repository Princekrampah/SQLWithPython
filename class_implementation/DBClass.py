from mysql import connector


class Database:
    def __init__(self, url, user, password) -> None:
        # user crendentials, we not storing the password for security
        # reasons.
        self.user = user
        self.url = url
        
        # connection
        self.connection = self.connect_to_db(password)
                
        
    # connect to db
    def connect_to_db(self, password):
        conn = None
        try:
            conn = connector.connect(
                host=self.url, 
                user=self.user, 
                passwd=password
            )
            print("Connection to DB successfully")
        except connector.Error as err:
            print(f"Error: {err}")
            
        return conn
        
        
    # Create DB function
    def create_db(self, database):
        cursor = self.connection.cursor()
        
        query = f"""
            CREATE DATABASE IF NOT EXISTS {database};
        """
        try:
            cursor.execute(query)
            print("Database created successfully")
        except connector.Error as err:
            print(f"Error: {err}")
            
            
    # Execute query function
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query execution successful")
        except connector.Error as err:
            print(f"Error: {err}")
           
            
    # Fetch data
    def fetch_data(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except connector.Error as err:
            print(f"Error: {err}")
            
        return result
    
    
    # Execute query function
    def execute_many_query(self, query, val):
        cursor = self.connection.cursor()
        
        try:
            cursor.executemany(query, val)
            self.connection.commit()
            print("Query execution successful")
        except connector.Error as err:
            print(f"Error: {err}")
                            
