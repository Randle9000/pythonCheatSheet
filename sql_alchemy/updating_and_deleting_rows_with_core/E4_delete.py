from sql_alchemy.database import engine
from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import update, select, bindparam, delete
from sql_alchemy.E3_metadata import user_table, address_table

insert_fake_data_to_db()

stmt = delete(user_table).where(user_table.c.name == "Rex")

with engine.connect() as conn:
    result = conn.execute(select(user_table))
    print('\n', result.all())

    result = conn.execute(stmt)
    print('\n', result.rowcount)

    result = conn.execute(select(user_table))
    print('\n', result.all())