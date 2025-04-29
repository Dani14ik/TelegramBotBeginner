import asyncio
from asyncpg_lite import DatabaseManager
from decouple import config

async def main():
    db_manager = DatabaseManager(dsn_flag=False, host=host, port=port, user=user,
                                 password=password, database=database, deletion_password=root_pass)
    async with db_manager as manager:
        columns = [
            "user_id INT8 PRIMARY KEY",
            "user_name VARCHAR(255)",
            "user_surname VARCHAR(255)",
            "user_age INT4"
        ]

        await manager.create_table(table_name="new_users", columns=columns)

asyncio.run(main())