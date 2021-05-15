from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from utils.misc import rate_limit


# лимит на раз в 5 сек
@rate_limit(limit=5)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}! 😎😉1️⃣'
                         f'\nДля получения списка доступных команд нажми /help')
    # await message.answer_document(types.InputFile("data/Rostov-na-donu.png"), caption="Вот ваша секретная покупка!")
    # если хотим обнулять рейтинг человека, расскомментировать нижестоящую строчку
    # db.update_rating(id=message.from_user.id, rating=0.0)

    # если Бд уже есть, печатаем ошибку
    try:
        db.add_user(id=message.from_user.id, name=message.from_user.full_name)

    except Exception as error:
        print(error)

    # Забираем 1-ое значение в базе
    count_users_db = db.count_users()[0]
    await message.answer(f'В базе сейчас <b><i>{count_users_db}</i></b> пользователей')
    # await state.set_state("locale_lat_lon_db")

# @dp.message_handler(content_types=types.ContentTypes.LOCATION,state="locale_lat_lon_db")
# async def locale_dp(message: types.Message,state: FSMContext):
#     location = message.location
#     latitude = location.latitude
#     longitude = location.longitude
#     db.update_lat(id=message.from_user.id, lat=latitude)
#     db.update_lon(id=message.from_user.id, lon=longitude)
#     print(db.select_all_users())
