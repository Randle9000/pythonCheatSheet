from sql_alchemy.E4_declaring_tables_orm_approach import User
from sql_alchemy.E3_metadata import user_table, address_table
from sqlalchemy import select

print(
     select(address_table.c.email_address).
     where(user_table.c.name == 'Pat').
     where(address_table.c.user_id == user_table.c.id)
 )

print(
     select(address_table.c.email_address).
     where(
        user_table.c.name == 'Pat',
        address_table.c.user_id == user_table.c.id)
 )

print(select(User).filter_by(name='Pat', fullname='Pat the cat'))