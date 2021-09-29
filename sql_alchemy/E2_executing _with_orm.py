from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import MetaData
from sql_alchemy.database import engine


print("\n commit as You go \n")
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
     text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
     [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )

    conn.commit()

metadata_obj = MetaData()

stmt = text("SELECT x, y FROM some_table WHERE y > :y").bindparams(y=3)
with Session(engine) as session:
    result = session.execute(stmt)
    # for row in result:
    #     print(row.x, row.y)
    #
    # for x, y, in result:
    #     print(x,y)
    #
    # for row in result:
    #     x = row[0]

    for dict_row in result.mappings():
        x = dict_row['x']
        y = dict_row['y']
        print(x,y)