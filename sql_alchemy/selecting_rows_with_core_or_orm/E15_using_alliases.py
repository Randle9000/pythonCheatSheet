from sql_alchemy.E3_metadata import user_table, address_table
from sql_alchemy.E4_declaring_tables_orm_approach import User, Address
from sqlalchemy import select


user_alias_1 = user_table.alias()
user_alias_2 = user_table.alias()

print(
    select(user_alias_1.c.name, user_alias_2.c.name).
    join_from(user_alias_1, user_alias_2, user_alias_1.c.id > user_alias_2.c.id)
)


### orm  Entity aliaases
from sqlalchemy.orm import aliased
address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)
print(
    select(User).
    join_from(User, address_alias_1).
    where(address_alias_1.email_address == 'patrick@aol.com').
    join_from(User, address_alias_2).
    where(address_alias_2.email_address == 'patrick@gmail.com')
)