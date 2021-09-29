
from sql_alchemy.E3_metadata import user_table, address_table
from sqlalchemy import select



print(
    select(user_table.c.name, address_table.c.email_address).
    join_from(user_table, address_table) # allows us to indicate the left and right side of the JOIN explicitly:
)
# "ON user_account.id = address.user_id appears because this table have relation by foreign key constrant definition

print(
    select(address_table.c.email_address).
    select_from(user_table).
    join(address_table, user_table.c.id == address_table.c.user_id)
)

#LEFT OUTER JOIN
print(
    select(user_table).join(address_table, isouter=True)
)

#full join
print(
    select(user_table).join(address_table, full=True)
)