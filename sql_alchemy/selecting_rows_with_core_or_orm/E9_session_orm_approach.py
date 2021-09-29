
from sqlalchemy import select
from sqlalchemy.orm import Session
from sql_alchemy.E4_declaring_tables_orm_approach import User
from sql_alchemy.database import engine
from sql_alchemy.utils import insert_fake_data_to_db

insert_fake_data_to_db()

# orm part
stmt = select(User).where(User.name == "Pat")

with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(row) # returns the User object with mapped values from table User

#--------------------
## selecting columns and from clause
# print(select(User)) # returns select 'columns' from 'table'

# Selecting ORM Entities and Columns
# print(select(user_table))


"""
select() from a Table vs. ORM class
While the SQL generated in these examples looks the same
whether we invoke select(user_table) or select(User),
in the more general case they do not necessarily render the same thing,
as an ORM-mapped class may be mapped to other kinds of “selectables” besides tables.
The select() that’s against an ORM entity also indicates that 
ORM-mapped instances should be returned in a result, which
 is not the case when SELECTing from a Table object.
"""