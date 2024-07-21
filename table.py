from  creat_db import Database

class table(Database):
    def __init__(self, database_name:str, table_name:str) -> None:
        super().__init__(database=database_name)
        self._connect_database()
        self.table_name=table_name

    def max(
        self, 
         *, 
         field:str
    ):

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
        ):

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
        ):

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
        ):

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
        ):
        t=', '.join(field)
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
            ):
        self._connect_database()
        self.cur.execute(f'SELECT REPLACE ({field}, "{str1}", "{str2}")
        FROM {self.table_name}')
        self.con.commit()
        self.cur.close()