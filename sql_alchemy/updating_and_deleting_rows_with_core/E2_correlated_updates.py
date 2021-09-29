from sql_alchemy.database import engine
from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import update, select, bindparam
from sql_alchemy.E3_metadata import user_table

insert_fake_data_to_db()

# TODO
