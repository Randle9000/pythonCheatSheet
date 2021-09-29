from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

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
    rex = session.get(User, 1) # short way to load up user object from db
    print(rex)
    # delete
    print(f"rex in session {rex in session}")
    session.delete(rex)  # here the object rex is marked for deletion, nothing happened until flush proceeds
    session.execute(select(User).where(User.name == "Rex")).first()  # rex stays in the session until the flush proceeds
    print(f"rex in session {rex in session}")  # but rex is no longer considered to be persistent withing the session

# ORM-enalbed delete statement
print(f'\norm enabled delete\n')
with Session(engine) as session:
    rex = session.get(User, 1)
    session.execute(delete(User).where(User.name == "Rex"))
    print(f"rex in session {rex in session}")

