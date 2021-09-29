from sql_alchemy import E3_metadata
from sql_alchemy.E3_metadata import user_table
from sql_alchemy.database import engine
from sqlalchemy import insert

# it just create insert not execute to execute you need engine, connection or session
stmt = insert(user_table).values(name="Moris", fullname="Moris the cat")
print(stmt)
compiled = stmt.compile()
print(compiled.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
    print(result.inserted_primary_key)

## more advanced
