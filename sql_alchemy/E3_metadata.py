# CORE approach

from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, MetaData
from sql_alchemy.database import engine

metadata = MetaData()

user_table = Table(
    "user_account",
    metadata, # this table object will be added to proper metadata dict
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey("user_account.id"), nullable=False),
    Column('email_address', String, nullable=False)
)

# creates all tables which are in metadata object
metadata.create_all(engine)