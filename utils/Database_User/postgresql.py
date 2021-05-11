import asyncio
import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.db_user,
                password=config.db_password,
                host='localhost'
            )
        )

    async def create_table_users(self):
        # Users - таблица пользователей
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        lat double precision,
        lon double precision,
        rating double precision,
        PRIMARY KEY (id)
        );
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f" {item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, id: int, name: str, email: str = None, lat: float = 0, lon: float = 0, rating: float = 0):
        sql = "INSERT INTO Users(id, name, email, lat, lon, rating) VALUES($1, $2, $3, $4, $5, $6) ON CONFLICT DO NOTHING"
        await self.pool.execute(sql, id, name, email, lat, lon, rating)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        # Выгружаем все данные из таблицы
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        # формируем запрос sql и формируем параметры из тьюпла
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")

    async def update_email(self, id: int, email: str):
        sql = "UPDATE Users SET email=$1 WHERE id=$2"
        return await self.pool.execute(sql, email, id)

    async def update_rating(self, id: int, rating: float):
        sql = "UPDATE Users SET rating=$1 WHERE id=$2"
        return await self.pool.execute(sql, rating, id)

    async def update_lat(self, id: int, lat: float):
        sql = "UPDATE Users SET lat=$1 WHERE id=$2"
        return await self.pool.execute(sql, lat, id)

    async def update_lon(self, id: int, lon: float):
        sql = "UPDATE Users SET lon=$1 WHERE id=$2"
        return await self.pool.execute(sql, lon, id)

    async def get_coordinates(self, id:int):
        x = await self.select_user(id=id)
        lat = x[3]
        lon = x[4]
        return lat, lon

    async def delete_all_users(self):
        await self.pool.execute("DELETE FROM Users WHERE True")

    async def delete_user_by_id(self, id: int):
        sql = "DELETE FROM Users WHERE id=$1"
        return await self.pool.execute(sql, id)
