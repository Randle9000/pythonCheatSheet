from sql_alchemy import E3_metadata
from sqlalchemy import select, insert
from sql_alchemy.E3_metadata import user_table
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


stmt = select(user_table).where(user_table.c.name == "Pat")

with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row) # returns raw tuple