from sql_alchemy.E3_metadata import user_table, address_table
from sqlalchemy import select, bindparam, insert
from sql_alchemy.database import engine

with engine.connect() as conn:
    resource = conn.execute(
        insert(user_table),
        [
            {"name": "Pat", "fullname": "Pat the cat"},
            {"name": "Rex", "fullname": "Rex the dog"},
        ]
    )
    conn.commit()

select_stmt = select(user_table.c.id, user_table.c.name + "@animal.org")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)
# insert_stmt = insert(address_table).returning(address_table.c.id, address_table.c.email_address)

print(insert_stmt)
with engine.connect() as conn:
    result = conn.execute(insert_stmt)
    print(result)
