# from sqlalchemy.orm import registry
#
# mapper_registry = registry()  # it includes Metadata
# Base = mapper_registry.generate_base()

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sql_alchemy.database import engine


Base = declarative_base()

# explain of relationship
"""
 The relationship() construct will be used to inspect the table relationships between 
 the Table objects that are mapped to the User and Address classes. 
 As the Table object representing the address table has a ForeignKeyConstraint which refers to the user_account table, 
 the relationship() can determine unambiguously that there is a one to many relationship from User.
 addresses to User; one particular row in the user_account table may be referred towards by many rows in the address table.
"""

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")  # TODO check how it works

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id")) # it assures that there is one to many relationship
                                                             # one email_address cannot be assigned to two users

    user = relationship("User", back_populates="addresses")
    """
    back_populate:
    these two relationship() constructs should be considered to be complimentary to each other;
     we will see how this plays out in the next section.
    """

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r}, user_id={self.user_id!r})"


Base.metadata.create_all(engine)
