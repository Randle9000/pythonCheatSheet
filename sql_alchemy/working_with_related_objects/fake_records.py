from sql_alchemy.working_with_related_objects.tables import User, Address, engine
from sqlalchemy.orm import Session

u1 = User(name="Pat", fullname="Pat the cat")
u2 = User(name="Pog", fullname="Pog the dog")

for user in [u1, u2]:
    a = Address(email_address=f"{user.fullname.replace(' ','')}@animal.org")
    user.addresses.append(a)

with Session(engine) as session:
    for user in [u1, u2]:
        session.add(user)
    session.commit()
