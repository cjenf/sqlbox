import sqlite3
import creat_db
from table_chain import table
from typing import Optional, Union, Dict, Tuple


_sql_type=dict(
        int_primary_key='INTEGER PRIMARY KEY',
        integer='INTEGER',
        int='INT',           # -2^31 to 2^31-1
        bigint='BIGINT',     # -2^63 to 2^63-1
        smallint='SMALLINT', # -2^15 to 2^15-1
        tinyint='TINYINT',   # 2^0-1 to 2^8-1
        real='REAL',         # type: ignore
        float='FLOAT',
        text='TEXT',
        blob='BLOB',
        null='NULL',    
    )


class sqlbox(creat_db.Database):
    def __init__(self,database_name:str) -> None:
        
        super().__init__(database=database_name) # type: ignore
        self.database_name=database_name
        self._creat_database()

    def create_table(
            self, 
            table_name:str,
            columns:Union[Dict[str, _sql_type]],  # type: ignore
            ): 
        
        self.table_name=table_name
        if isinstance(columns, dict):
            self._connect_database()
            v=','.join(tuple((f'{c} {_sql_type[t]}'  for c, t in columns.items())))
            self.cur.execute(f'''
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        {v}
                    )
                    ''')
            
        self.con.commit()
        self.con.close()

        return table
    def insert_into(
                self, 
                *, 
                field:tuple, 
                value:tuple
            ):
        if self.table_name:
            self._connect_database()
            self.cur.execute(f'INSERT INTO {self.table_name} {field} VALUES ({(t:=','.join('?'*len(value)))})', value)
            self.con.commit()
            self.con.close()

        else:
            import exception_
            raise exception_.TableNotFoundError("Table not found")

        return table
    
    def get(
            self,
            field_name:Optional[str]=None,
            all:bool=True
        ):
        
        if all and self.table_name:
            self._connect_database()
            self.cur.execute(f'SELECT * FROM {self.table_name}')
            rows=self.cur.fetchall()
            self.cur.close()
            return rows

        elif not all and self.table_name:
            self._connect_database()
            self.cur.execute(f'SELECT {field_name} FROM {self.table_name}')
            rows=self.cur.fetchall()
            self.cur.close()
            return rows
        
    def update(
            self,
            *,
            field_name:Tuple,
            value:Tuple
        ):

        if not self.table_name:
            self._connect_database()
            self.cur.execute(f'UPDATE {self.table_name} SET {field_name[1]} = ? WHERE {field_name[0]} = ?', (value[1], value[0]))
            self.con.commit()
            self.con.close()
        
    def delete(
            self,
            *,
            field:str,
            value
        ):
        if not self.table_name:
            self._connect_database()
            self.cur.execute(f'DELETE FROM {self.table_name} WHERE {field} = ?', (value,))
            self.con.commit()
            self.con.close()

# sqlbox('test.db').create_table('mine', {'id':'int', 'name':'text', 'age':'int'})
# sqlbox('test.db').insert_into(field=('id','name','age'), value=(1,'test',22))

db = sqlbox('test.db')

print(db.get(all=True)) 