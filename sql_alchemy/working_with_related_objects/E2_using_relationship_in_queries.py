from sql_alchemy.working_with_related_objects.tables import User,Address, engine
from sql_alchemy.working_with_related_objects import fake_records
from sqlalchemy import select
from sqlalchemy.orm import Session

stmt = select(Address.email_address)\
      .select_from(Address)\
      .join(User.addresses)

print(stmt)

"""
The presence of an ORM relationship() on a mapping is not used by Select.join() or Select.join_from()
if we don’t specify it; it is not used for ON clause inference.
This means, if we join from User to Address without an ON clause,
it works because of the ForeignKeyConstraint between the two mapped Table objects,
not because of the relationship() objects on the User and Address classes:
"""
stmt_2 = select(Address.email_address).\
      join_from(User, Address)

print(stmt_2)

with Session(engine) as session:
    result = session.execute(stmt)
    print(result.all())  # ON is chosen automatically by checking the ForeignKeyConstraint between Address and User classes


