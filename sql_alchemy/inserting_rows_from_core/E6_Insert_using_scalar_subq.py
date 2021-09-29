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

scalar_subq = (
    select(user_table.c.id).
    where(user_table.c.name == bindparam('name'))
    .scalar_subquery())

with engine.connect() as conn:
    print(insert(address_table).values(user_id=scalar_subq),
        [{"name": "Pat", "email_address": "Pat@thecat.org"}],
        [{"name": "Rex", "email_address": "rex@thedog.org"}])

    result = conn.execute(
        insert(address_table).values(user_id=scalar_subq),
        [{"name": "Pat", "email_address": "Pat@thecat.org"}],
        [{"name": "Rex", "email_address": "rex@thedog.org"}],
    )

