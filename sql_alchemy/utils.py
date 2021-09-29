
from sqlalchemy import select, insert
from sql_alchemy.E3_metadata import user_table, address_table
from sql_alchemy.database import engine
from sql_alchemy.E4_declaring_tables_orm_approach import User, Address


def insert_fake_data_to_db():
    with engine.connect() as conn:
        resource = conn.execute(
            insert(user_table),
            [
                {"name": "Pat", "fullname": "Pat the cat"},
                {"name": "Rex", "fullname": "Rex the dog"},
                {"name": "Thumb", "fullname": "Thumb the Whale"},
                {"name": "Marc", "fullname": "Marc the Giraffe"},
                {"name": "Marc", "fullname": "Marc the Giraffe"},
            ]
        )
        conn.commit()

    select_stmt = select(User.id, User.fullname + "@animal.org")
    insert_stmt = insert(address_table).from_select(
        ["user_id", "email_address"], select_stmt
    )
    with engine.begin() as conn:
        conn.execute(insert_stmt)