from sqlalchemy.orm import Session
from sqlalchemy import select

from sql_alchemy.data_manipualtion_with_orm.tables import User, Address
from sql_alchemy.database import engine

# inserting rows
rex = User(name="Rex", fullname="Rex the dog")
pat = User(name="Pat", fullname="Pat the cat")  # these object are in state called transient not associated with any db

with Session(engine) as session:
    session.add(rex)
    session.add(pat)
    session.commit()

with Session(engine) as session:
    rex = session.execute(select(User).filter_by(name="Rex")).scalar_one() # it works as a proxy
    # to specific row in db. In terms of current transaction
    print(rex)
    print(f' is object dirty? {rex in session.dirty}')
    rex.name = "Bax"
    print('Rex name change to Bax')
    print(f' is object dirty? {rex in session.dirty}')
    session.commit()
    result = session.execute(select(User))
    print(result.all())