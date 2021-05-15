from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("get_my_rating"))
async def get_my_rating(message: types.Message):
    rate = db.get_rating_total(message.from_user.id)
    await message.answer("Ваш рейтинг: " + str(rate))


@dp.message_handler(Command("get_rating"))
async def view_rating_user(message: types.Message):
    users = db.select_all_users()
    print(len(users))
    tmp_user_rating = {}
    for i in users:
        tmp_user_rating[i[1]] = i[-1]
    sorted_user_rating = {}
    sorted_users = sorted(tmp_user_rating, key=tmp_user_rating.get, reverse=True)
    for w in sorted_users:
        sorted_user_rating[w] = tmp_user_rating[w]

    output_string = ""
    for user in sorted_user_rating:
        output_string += "Рейтинг пользователя " + user + ": " + str(sorted_user_rating[user]) + str("\n")
    await message.answer(output_string)

