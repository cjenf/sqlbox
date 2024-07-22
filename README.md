# 📦sqlbox v0.0.1
### sqlbox is a package written in Python that allows people who don't know how to write SQL to write and manage databases using Python syntax.
### Install package
```py
pip install sqlbox
```
> [!NOTE]
> **sqlbox v0.01 has only some basic table operations**
## Usage
### Creat Database
```py
import sqlbox
db=sqlbox.sqlbox(database_name="test.db")
```
### Table
> [!NOTE]
> **data type**<br>
> ```py
> int_primary_key='INTEGER PRIMARY KEY', 
> text_primary_key='TEXT PRIMARY KEY',
> int='INTEGER',
        float='FLOAT',
        text='TEXT',
        blob='BLOB',
        null='NULL',    
        ```

```py
db.create_table("users",{"id":"int_prinary_key","name":"text","age":"int"})
```
