from sql_alchemy.database import engine
from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import update, select, bindparam
from sql_alchemy.E3_metadata import user_table, address_table

insert_fake_data_to_db()

# TODO NOT FOR SQLLITE

update_stmt = (update(user_table).
               where(user_table.c.id == address_table.c.id).
               where(address_table.c.email_address == "Rex@animal.org").
               values(fullname="Rex"))

with engine.connect() as conn:
    conn.execute(update_stmt)
    result = conn.execute(user_table)
    print(result.all())
