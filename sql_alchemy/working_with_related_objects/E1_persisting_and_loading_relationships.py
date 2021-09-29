from sql_alchemy.working_with_related_objects.tables import User, Address
from sqlalchemy.orm import Session
from sql_alchemy.database import engine

u1 = User(name="Rychu", fullname="Peja")
print(u1.addresses)
# relationship does to instances of objects. user obj. has python list when access the .addresses element
a1 = Address(email_address="Rychu@raper@lwwl.org")
u1.addresses.append(a1)

# This synchronization occurred as a result of
# our use of the relationship back_populates parameter between the two relationship() objects

print(u1.addresses)
print(a1.user)

a2 = Address(email_address="pearl@aol.com", user=u1)
print(u1.addresses)


# till now the a1,a2,u1 are in transient state
session = Session(engine)
session.add(u1)

# cascading object into the session only u1 is added to session but because of relationship
# the a1, a2 are added by definition
print(u1 in session)
print(a1 in session)
print(a2 in session)

# now the a1,a2,u1 are in pending state this means they are ready to be the subject of an INSERT operation
# but this has not yet proceeded;
print(u1.id) # no id because it has not been added yet to db
session.commit()

print(u1.id) # added to db (thanks to commit()) so now the id exists
print(u1.addresses)
print(a1)
"""
Collections and related attributes in the SQLAlchemy ORM are persistent in memory; 
once the collection or attribute is populated, SQL is no longer emitted until that collection or attribute is expired.
We may access u1.addresses again as well as add or remove items and this will not incur any new SQL calls:
"""




