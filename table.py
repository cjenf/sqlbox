from  creat_db import Database

class table(Database):
    def __init__(
            self, 
            *,
            database_name:str, 
            table_name:str
        ) -> None:
        """
        Initializes a new instance of the `table` class.

        Args:
            database_name (str): The name of the database.
            table_name (str): The name of the table.

        Returns:
            None
        """

        super().__init__(database=database_name)
        self._connect_database()
        self.table_name=table_name

    def max(
            self, 
            *, 
            field:str
        ) -> str:
        """
        Retrieves the maximum value of a specified field from a table.

        Args:
            field (str): The name of the field to retrieve the maximum value from.

        Returns:
            The maximum value of the specified field.

        Raises:
            Exception: If there is an error executing the SQL query.

        Example:
            ```
            table = Table("my_database", "my_table")
            max_value = table.max(field="my_field")
            print(max_value)
            ```
        """
        self._connect_database()
        self.cur.execute(f'SELECT MAX({field}) FROM {self.table_name}')
        max_=self.cur.fetchone()[0]
        self.con.commit()
        self.cur.close()
        return max_
    
    def min(
            self, 
            *, 
            field:str
        ) -> str:
        """
    	Retrieves the minimum value of a specified field from a table.
    	
    	Args:
    	    field (str): The name of the field to retrieve the minimum value from.
    	
    	Returns:
    	    The minimum value of the specified field.
    	"""
        self._connect_database()
        self.cur.execute(f'SELECT MIN({field}) FROM {self.table_name}')
        min_=self.cur.fetchone()[0]
        self.con.commit()
        self.cur.close()
        return min_
    
    def sum(
            self, 
            *, 
            field:str
        ) -> list:
        """
    	Retrieves the sum of a specified field from a table.
    	
    	Args:
    	    field (str): The name of the field to calculate the sum from.
    	
    	Returns:
    	    The sum of the specified field.
    	"""
        self._connect_database()
        self.cur.execute(f'SELECT SUM({field}) FROM {self.table_name}')
        sum_=self.cur.fetchone()[0]
        self.con.commit()
        self.cur.close()
        return sum_

    def average(
            self, 
            *, 
            field:str
        ) -> list:
        """
        Calculates the average value of a specified field from a table.

        Args:
            field (str): The name of the field to calculate the average value from.

        Returns:
            The average value of the specified field.
        """
        self._connect_database()
        self.cur.execute(f'SELECT AVG({field}) FROM {self.table_name}')
        avg_=self.cur.fetchone()[0]
        self.con.commit()
        self.cur.close()
        return avg_
    
    def groupby(
            self, 
            *, 
            field:list
        ) -> list:
        """
        Executes a group by operation on the specified table based on the provided field list.
        
        Args:
            field (list): A list of fields to group by.
        
        Returns:
            The grouped results based on the specified fields.
        """

        self._connect_database()
        self.cur.execute(f''' 
        SELECT {(t:=', '.join(field[0,len(field)]))}, SUM({field[-1]}) 
        FROM {self.table_name}
        GROUP BY {t}
        ''') 
        groupby_=self.cur.fetchall()
        self.con.commit()
        self.cur.close()
        return groupby_
    
    def replace(
            self,
            field:str,
            str1:str,
            str2:str
            ) -> None:
        """
        Replaces all occurrences of `str1` with `str2` in the specified `field` of the table.

        Args:
            field (str): The name of the field in the table where the replacement should be performed.
            str1 (str): The substring to be replaced.
            str2 (str): The substring to replace `str1` with.

        Returns:
            None
        """

        self._connect_database()
        self.cur.execute(f'SELECT REPLACE ({field}, "{str1}", "{str2}")
        FROM {self.table_name}')
        self.con.commit()
        self.cur.close()

    def delate_table(self) -> None:
        """
        Deletes the table specified by the `self.table_name` attribute.

        This function connects to the database using the `_connect_database()` method
        and then executes a SQL query to drop the table if it exists.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        self._connect_database()    
        self.cur.execute(f'DROP TABLE IF EXISTS {self.table_name}')