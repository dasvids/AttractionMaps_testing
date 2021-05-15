import asyncio
from utils.Database_User.postgresql import Database

db = Database(asyncio.get_event_loop())


async def test():
    await db.create_table_users()
    await db.delete_all_users()
    users = await db.select_all_users()
    print(f"До добавления: {users=}")
    await db.add_user(1, "Vasya")
    users = await db.select_all_users()
    print(f"После добавления: {users=}")
    user = await db.select_user(name="Vasya")
    print('rating vasya = ',user[-1])
    print(f"Найденный пользователь: {user=}")
    await db.update_email(1, "vasya@eu.ru")
    # await db.update_rating(1, 5.0)
    await db.update_lat(1, -10)
    await db.update_lon(1, 10)
    await db.update_rating_easy(1, 10)
    print('RATING vasya = ', (await db.get_rating_easy(1)))
    users = await db.select_all_users()
    print(f"После обновления: {users=}")
    await db.add_user(2, "Alice", "alice@gensokyo.jp", -50.1, 20.5, 10)
    users = await db.select_all_users()
    print(f"После добавления ещё одного пользователя: {users=}")
    await db.delete_user_by_id(1)
    users = await db.select_all_users()
    print(f"После удаления пользователя: {users=}")
    print(f"Попытка добавления того же пользователя:")
    await db.add_user(2, "Alice", "alice@gensokyo.usa", 31, 60.5, 20)
    users = await db.select_all_users()
    print(f"После попытки добавления пользователя: {users=}")
    x, y = await db.get_coordinates(2)
    print(f"Lat: {x} Lon: {y}")

asyncio.get_event_loop().run_until_complete(test())