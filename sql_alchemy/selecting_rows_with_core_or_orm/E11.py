from sql_alchemy.utils import insert_fake_data_to_db
from sql_alchemy.E3_metadata import user_table
from sqlalchemy import select, text
from sql_alchemy.database import engine

insert_fake_data_to_db()

## Selecting from Labeled SQL Expressions

stmt = select(("Username: " + user_table.c.name).label("username")).order_by(user_table.c.name)

with engine.begin() as conn:
    for row in conn.execute(stmt):
        print(f'{row.username}')
        print(f'{row}')

print('\n')
# Selecting with Textual Column Expressions¶
stmt = (
    select(
        text("'some phrase'"), user_table.c.name
    ).order_by(user_table.c.name)
)
with engine.begin() as conn:
    for row in conn.execute(stmt):
        print(f'{row}')