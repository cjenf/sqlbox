import sqlite3
import os

class Database:
    def __init__(
            self, 
            *, 
            database:str
        ) -> None:
        self .database=database
        
    def _creat_database(self) -> None:
        """
        Connects to the specified database, creates a cursor, and then closes the cursor if the database name is provided. 
        Raises a NamingError with the message "Database name must be str" if the database name is not provided.
        """
        if self.database:
            self.con = sqlite3.connect(self.database)
            self.cur = self.con.cursor()
            self.cur.close()

        else:
            import exception_
            raise exception_.NamingError("Database name must be str")
        
    def _connect_database(self) -> None: 
        """
        Connects to the specified database, creates a cursor, and then closes the cursor if the database name is provided. 
        Raises a DatabaseNotFoundError if the database file is not found.
        """   
        if os.path.exists(file:=f'{self.database}'):
            self.con = sqlite3.connect(file)
            self.cur = self.con.cursor()

        else:
            import exception_
            raise exception_.DatabaseNotFoundError(f"{file} not found")