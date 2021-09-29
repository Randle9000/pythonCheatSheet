from sqlalchemy.orm import Session
from sqlalchemy import select, update

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
    pat = session.execute(select(User).filter_by(name="Pat")).scalar_one()
    session.execute(
        update(User).where(User.name == "Pat").
        values(fullname="Pat the Mega cat")
    )
    print(pat.fullname)

