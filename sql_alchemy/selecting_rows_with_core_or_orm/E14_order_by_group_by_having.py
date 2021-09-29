from sql_alchemy.utils import insert_fake_data_to_db
from sqlalchemy import select, func, desc
from sql_alchemy.E3_metadata import user_table
from sql_alchemy.E4_declaring_tables_orm_approach import User, Address
from sql_alchemy.database import engine


check_order = True
aggregate_functions = True
ordering_or_grouping_by_label = True
insert_fake_data_to_db()

if check_order:
    # order_by CORE
    stmt_order_CORE = select(user_table).order_by(user_table.c.name)
    print(stmt_order_CORE)

    # order_by ORM
    stmt_order_ORM = select(User).order_by(User.fullname.desc())
    print(stmt_order_ORM)

    with engine.begin() as conn:
        result = conn.execute(stmt_order_CORE).all()
        print(result)
        result = conn.execute(stmt_order_ORM).all()
        print(result)


#Aggregate functions
if aggregate_functions:
    """
    aggregate functions allow column expressions across multiple rows
    to be aggregated together to produce a single result
    Examples include counting, computing averages,
    as well as locating the maximum or minimum value in a set of values.
    SQL functions are described in more detail later in this tutorial at Working with SQL Functions.
    https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#tutorial-functions
    """

    count_fn = func.count(User.id)
    print(count_fn)

    stmt = select(User.name, func.count(User.name).label("count"))\
        .join(Address)\
        .group_by(User.name)\
        .having(func.count(User.name) > 1)
    print(stmt)

    with engine.connect() as conn:
        result = conn.execute(stmt)
        print(result.all())

if ordering_or_grouping_by_label:
    stmt = not select(
        Address.user_id,
        func.count(Address).label("num_addresse")).\
        group_by("user_id").order_by("user_id", desc("num_addresses"))

print(stmt)




