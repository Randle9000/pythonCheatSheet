from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import select, func
from sql_alchemy.E3_metadata import user_table, address_table
from sql_alchemy.database import engine


insert_fake_data_to_db()

subq = select(func.count(address_table.c.id).label("count"), address_table.c.user_id
              ).group_by(address_table.c.user_id).subquery()
print(subq)

with engine.connect() as conn:
    result = conn.execute(subq)
    print(result.all())

# with engine.connect() as conn:
#     result = conn.execute(select(subq.c.user_id, subq.c.count))
#     print(result.all())


stmt = select(
    user_table.c.name,
    user_table.c.fullname,
    subq.c.count
).join_from(user_table, subq)

print("\n", stmt, "\n")

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())