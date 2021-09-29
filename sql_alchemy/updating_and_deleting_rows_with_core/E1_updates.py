from sql_alchemy.database import engine
from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import update, select, bindparam
from sql_alchemy.E3_metadata import user_table

insert_fake_data_to_db()

# update
stmt = (update(user_table).where(user_table.c.name == 'Rex').values(fullname="Rex the wolf"))

with engine.connect() as conn:
    result = conn.execute(stmt)
    print()

    result = conn.execute(select(user_table))
    print(result.all())

#
stmt = (update(user_table).
        where(user_table.c.name == bindparam('oldname')).
        values(name=bindparam("newname")))

with engine.connect() as conn:
    conn.execute(
        stmt,
        [
            {'oldname': "Pat", "newname": "Moris"},
            {'oldname': "Rex", "newname": "Hex"}
        ]
    )
    result = conn.execute(select(user_table))
    print(result.all())