from sqlalchemy.orm import registry, relationship
from sqlalchemy import Column, ForeignKey, Integer, Text, String, create_engine
from sql_alchemy.database import engine

mapper_registry = registry()
Base = mapper_registry.generate_base()

# the two steps above can be shortened to:
# from sqlalchemy.orm import declarative_base
# Base = declarative_base()

# declaring mapped classes


class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(Text(30))
    fullname = Column(Text)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, )
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# or Combining Core Table Declarations with ORM Declarative
"""
class User(Base):
    __table__ = user_table

     addresses = relationship("Address", back_populates="user")

     def __repr__(self):
        return f"User({self.name!r}, {self.fullname!r})"
"""



mapper_registry.metadata.create_all(engine)
"""
or:
# the identical MetaData object is also present on the
# declarative base
Base.metadata.create_all(engine)
"""