from sql_alchemy.utils import insert_fake_data_to_db
from sql_alchemy.E4_declaring_tables_orm_approach import User, Address
from sql_alchemy.E3_metadata import user_table
from sqlalchemy import select
from sqlalchemy.orm import Session
from sql_alchemy.database import engine

insert_fake_data_to_db()

engine.echo = False
print(select(User))
print(select(user_table))
print(select(User.name, User.fullname))

with Session(engine) as session:
    row = session.execute(select(User)).first()
    print(row)
    print(row[0])
    print('\n')
    row = session.execute(select(User.name, User.fullname)).first()
    print(row, '\n')

    result = session.execute(
        select(User.name, Address).
        where(User.id == Address.user_id).
        order_by(Address.id))\
        .all()
    print(result)

