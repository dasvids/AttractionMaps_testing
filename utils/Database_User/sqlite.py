import sqlite3


class Database:
    # Конструктор по пути
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    # Создаем подключение
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    # функция есть sql - запрос, где id - основной ключ
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection

        # поиск ошибков и просмотр действий бд
        connection.set_trace_callback(logger)
        # позволяет делать запросы к бд
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        # если изменяли то изменяем бд
        if commit:
            # изменение бд
            connection.commit()

        # если выгружали данные то изменяем бд
        if fetchone:
            # выгружаем один тьюпл
            data = cursor.fetchone()

        # если выгружали все данные то бд
        if fetchall:
            # выгружаем всех в  тьюпл
            data = cursor.fetchall()

        # закрываем конешкн после изменений
        connection.close()
        return data

    # Функция создания таблицы
    # по id можно выбирать пользователя
    def create_table_users(self):
        # Users - таблица пользователей
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id INT NOT NULL,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        lat DOUBLE,
        lon DOUBLE,
        rating_easy DOUBLE,
        rating_medium DOUBLE,
        rating_hard DOUBLE,
        PRIMARY KEY (id)
        );
        """
        # Закрепляем изменения
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str, email: str = None, lat: float = 0, lon: float = 0,
                 rating_easy: float = 0, rating_medium: float = 0, rating_hard: float = 0,):
        sql = "INSERT OR IGNORE INTO Users(id, name, email, lat, lon, rating_easy, rating_medium, rating_hard) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        self.execute(sql, (id, name, email, lat, lon, rating_easy, rating_medium, rating_hard), commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        # Выгружаем все данные из таблицы
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f" {item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        # формируем запрос sql и формируем параметры из тьюпла
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users", fetchone=True)

    def update_email(self, id: int, email: str):
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execute(sql, parameters=(email, id), commit=True)

    #def update_rating(self, id: int, rating: float):
    #    sql = "UPDATE Users SET rating=? WHERE id=?"
    #    return self.execute(sql, parameters=(rating, id), commit=True)

    def update_lat(self, id: int, lat: float):
        sql = "UPDATE Users SET lat=? WHERE id=?"
        return self.execute(sql, parameters=(lat, id), commit=True)

    def update_lon(self, id: int, lon: float):
        sql = "UPDATE Users SET lon=? WHERE id=?"
        return self.execute(sql, parameters=(lon, id), commit=True)

    def get_coordinates(self, id:int):
        x = self.select_user(id=id)
        lat = x[3]
        lon = x[4]
        return lat, lon

    def delete_all_users(self):
        # Удаляем всех
        self.execute("DELETE FROM Users WHERE True", commit=True)

    def delete_user_by_id(self, id: int):
        sql = "DELETE FROM Users WHERE id=?"
        return self.execute(sql, parameters=tuple([id]), commit=True)

    def get_rating_easy(self, id: int):
        # print((await self.select_user(id=id))[5])
        return (self.select_user(id=id))[5]

    def get_rating_medium(self, id: int):
        return (self.select_user(id=id))[6]

    def get_rating_hard(self, id: int):
        return (self.select_user(id=id))[7]

    def get_rating_total(self, id: int):
        return (self.get_rating_easy(id)) + (self.get_rating_medium(id)) + (self.get_rating_hard(id))

    def update_rating_easy(self, id: int, rating: float):
        sql = "UPDATE Users SET rating_easy=? WHERE id=?"
        return self.execute(sql, parameters=(rating, id), commit=True)

    def update_rating_medium(self, id: int, rating: float):
        sql = "UPDATE Users SET rating_medium=? WHERE id=?"
        return self.execute(sql, parameters=(rating, id), commit=True)

    def update_rating_hard(self, id: int, rating: float):
        sql = "UPDATE Users SET rating_hard=? WHERE id=?"
        return self.execute(sql, parameters=(rating, id), commit=True)

# логгирование результатов
def logger(statement):
    print(f"""
_____
Executing:
{statement}
-----
""")
