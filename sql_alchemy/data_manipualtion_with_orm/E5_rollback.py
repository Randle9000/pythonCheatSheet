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


# rollback
"""
session.rollback() - will not only roll back the transaction,
but also expire all objects currently associated with this Session
which will have the effect that they will refresh themselves 
when next accessed using a process known as lazy loading:
"""
engine.echo = False
with Session(engine) as session:
    pat = session.execute(select(User).filter_by(name="Pat")).scalar_one()
    session.execute(
        update(User).where(User.name == "Pat").
        values(fullname="Pat the Mega cat")
    )
    print(pat.fullname)
    print(pat.__dict__)
    session.rollback()
    """
    this (below) is the expired state, 
    accessing the attribute again will autobegin a new transaction
    and refresh sandy with the current database row:
    """
    print(f"pat in session {pat in session}")
    print(pat.__dict__)
    print(pat.fullname)
    """
    We may now observe that the full database row was also populated into the __dict__ of the sandy object:
    lazy loading !
    """
    print(pat.__dict__)
    print(f"pat in session {pat in session}")
    print(session.execute(select(User).where(User.name == 'Pat')).scalar_one() is pat)