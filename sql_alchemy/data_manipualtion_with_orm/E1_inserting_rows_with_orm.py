from sqlalchemy.orm import Session

from sql_alchemy.data_manipualtion_with_orm.tables import User, Address
from sql_alchemy.database import engine

# inserting rows
rex = User(name="Rex", fullname="Rex the dog")
pat = User(name="Pat", fullname="Pat the cat")  # these object are in state called transient not associated with any db
print(rex)

# create session
session = Session(engine) # just the learning purpose, normally we use the context manager (here we need to close it later!)

# objects added to the session
# it's pending state and object have not been inserted yet
session.add(rex)
session.add(pat)

# check the pending objects state in session
print(session.new)

"""
the Session makes use of a pattern known as unit of work.
This generally means it accumulates changes one at a time,
but does not actually communicate them to the database until needed
This allows it to make better decisions
about how SQL DML should be emitted in the transaction based on a given set of pending changes. 
When it does emit SQL to the database to push out the current set of changes, the process is known as a flush.
"""

# so it created a new transaction and emitted the appropriate INSERT statements for the two objects.
# !! The transaction now remains open
# until we call any of the Session.commit(), Session.rollback(), or Session.close() methods of Session.
session.flush()

# but it is usually unnecessary as the Session features a behavior known as autoflush,
# which we will illustrate later. It also flushes out changes whenever Session.commit() is called.

print(rex.id)
print(pat.id)

some_rex = session.get(User, 1)
print(some_rex)
session.commit()
session.close()