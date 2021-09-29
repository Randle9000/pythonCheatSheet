from sqlalchemy import create_engine
from sqlalchemy import text
from sql_alchemy.database import engine


"""
In the below example, the context manager provided for a database connection
and also framed the operation inside of a transaction.
ROLLBACK is emitted to end the transaction.
The transaction is not committed automatically;
when we want to commit data we normally need to call Connection.commit(
"""

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())


print("\n commit as You go \n")
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
     text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
     [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )

    conn.commit()


"""
There is also another style of committing data,
which is that we can declare our “connect” block to be a transaction block up front.
For this mode of operation, we use the Engine.begin() method to acquire the connection,
rather than the Engine.connect() method.
This method will both manage the scope of the Connection
and also enclose everything inside of a transaction with COMMIT at the end,
assuming a successful block, or ROLLBACK in case of exception raise.
This style may be referred towards as begin once:
"""
print("\n begin once \n")
with engine.begin() as conn:
    conn.execute(
     text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
     [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    )

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM some_table"))
#     for x, y in result:
#         print(x, y)

# for just one parameter
stmt = text("SELECT x, y FROM some_table WHERE y > :y").bindparams(y=8)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for x, y in result:
        print(x, y)



