from utils.Database_User.sqlite import Database

db = Database("test.db")


def test():
    db.create_table_users()
    users = db.select_all_users()
    print(f"До добавления: {users=}")
    db.add_user(1, "Vasya")
    users = db.select_all_users()
    print(f"После добавления: {users=}")
    user = db.select_user(name="Vasya")
    print(f"Найденный пользователь: {user=}")
    db.update_email(1, "vasya@eu.ru")
    db.update_rating(1, 5.0)
    db.update_lat(1, -10)
    db.update_lon(1, 10)
    users = db.select_all_users()
    print(f"После обновления: {users=}")
    db.add_user(2, "Alice", "alice@gensokyo.jp", -50.1, 20.5, 10)
    users = db.select_all_users()
    print(f"После добавления ещё одного пользователя: {users=}")
    db.delete_user_by_id(1)
    users = db.select_all_users()
    print(f"После удаления пользователя: {users=}")
    print(f"Попытка добавления того же пользователя:")
    db.add_user(2, "Alice", "alice@gensokyo.usa", 31, 60.5, 20)
    users = db.select_all_users()
    print(f"После попытки добавления пользователя: {users=}")
    x, y = db.get_coordinates(2)
    print(f"Lat: {x} Lon: {y}")

test()
