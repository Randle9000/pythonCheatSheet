from sql_alchemy.database import engine
from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import update, select, bindparam, delete
from sql_alchemy.E3_metadata import user_table, address_table

insert_fake_data_to_db()

update_stmt = (
    update(user_table).where(user_table.c.name == 'Rex').
    values(fullname='Rex the Star').
    returning(user_table.c.id, user_table.c.name)
)

with engine.connect() as conn:
    result = conn.execute(update_stmt)
    print(result)