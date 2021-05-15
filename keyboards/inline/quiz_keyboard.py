from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import  quiz_callback, quiz_photo_callback


quiz_keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Виктора Дамасский",
                callback_data=quiz_callback.new(next="2",answer="Виктора Дамасский")),
],[InlineKeyboardButton(
                text="Георгия Победоносца",
                callback_data=quiz_callback.new(next="2",answer="Георгия Победоносца")),
],[InlineKeyboardButton(
                text="Иоанна Сочавского",
                callback_data=quiz_callback.new(next="2",answer="Иоанна Сочавского")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard2= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="продукты питания пилотов",
                callback_data=quiz_callback.new(next="3",answer="продукты питания пилотов")),
],[InlineKeyboardButton(
                text="космический спускаемый аппарат - Союз ТМА-10",
                callback_data=quiz_callback.new(next="3",answer="КСА - Союз ТМА-10")),
],[InlineKeyboardButton(
                text="баллистическая капсула",
                callback_data=quiz_callback.new(next="3",answer="баллистическая капсула")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard3= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Великой Отечественной войне",
                callback_data=quiz_callback.new(next="4",answer="Великой Отечественной войне")),
],[InlineKeyboardButton(
                text="в Первой мировой войне",
                callback_data=quiz_callback.new(next="4",answer="в Первой мировой войне")),
],[InlineKeyboardButton(
                text="в Отечественной войне 1812 г",
                callback_data=quiz_callback.new(next="4",answer="в Отечественной войне 1812 г")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard4= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Бульвар Дружбы",
                callback_data=quiz_callback.new(next="5",answer="Бульвар Дружбы")),
],[InlineKeyboardButton(
                text="Красная долина",
                callback_data=quiz_callback.new(next="5",answer="Красная долина")),
],[InlineKeyboardButton(
                text="Аллея любви",
                callback_data=quiz_callback.new(next="5",answer="Аллея любви")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard5= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Вишневый сад",
                callback_data=quiz_callback.new(next="6",answer="Вишневый сад")),
],[InlineKeyboardButton(
                text="Война и мир",
                callback_data=quiz_callback.new(next="6",answer="Война и мир")),
],[InlineKeyboardButton(
                text="Тихий Дон",
                callback_data=quiz_callback.new(next="6",answer="Тихий Дон")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard6= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Железный век",
                callback_data=quiz_callback.new(next="7",answer="Железный век")),
],[InlineKeyboardButton(
                text="Бронзовый век",
                callback_data=quiz_callback.new(next="7",answer="Бронзовый век")),
],[InlineKeyboardButton(
                text="Медный век",
                callback_data=quiz_callback.new(next="7",answer="Медный век")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard7= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="был известным врачом",
                callback_data=quiz_callback.new(next="8",answer="был известным врачом")),
],[InlineKeyboardButton(
                text="был управляющим города",
                callback_data=quiz_callback.new(next="8",answer="был управляющим города")),
],[InlineKeyboardButton(
                text="был владельцем спиртоводочного завода",
                callback_data=quiz_callback.new(next="8",answer="был владельцем сз")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)

quiz_keyboard8= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Истинное православие",
                callback_data=quiz_callback.new(next="9",answer="Истинное православие")),
],[InlineKeyboardButton(
                text="Старообрядчество",
                callback_data=quiz_callback.new(next="9",answer="Старообрядчество")),
],[InlineKeyboardButton(
                text="Протестантство",
                callback_data=quiz_callback.new(next="9",answer="Протестантство")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="9", answer="End"))
        ]]
)
quiz_keyboard9= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="2013г",
                callback_data=quiz_callback.new(next="10",answer="2013г")),
],[InlineKeyboardButton(
                text="2018г",
                callback_data=quiz_callback.new(next="10",answer="2018г")),
],[InlineKeyboardButton(
                text="2016г",
                callback_data=quiz_callback.new(next="10",answer="2016г")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)
quiz_keyboard10= InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(
                text="Библиотека ЮФУ(РГУ)",
                callback_data=quiz_callback.new(next="11",answer="Библиотека ЮФУ(РГУ)")),
],[InlineKeyboardButton(
                text="Ростовский областной музей изобразительных искусств",
                callback_data=quiz_callback.new(next="11",answer="РО МИИ")),
],[InlineKeyboardButton(
                text="Музей Восковых Фигур",
                callback_data=quiz_callback.new(next="11",answer="Музей Восковых Фигур")),
],[InlineKeyboardButton
                (
                text="Выйти из викторины",
                callback_data=quiz_callback.new(next="0", answer="End"))
        ]]
)

# фото

quiz_photo1= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 2 вопроса",callback_data=quiz_photo_callback.new(next="p1"))]])
quiz_photo2= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 3 вопроса",callback_data=quiz_photo_callback.new(next="p2"))]])
quiz_photo3= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 4 вопроса",callback_data=quiz_photo_callback.new(next="p3"))]])
quiz_photo4= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 5 вопроса",callback_data=quiz_photo_callback.new(next="p4"))]])
quiz_photo5= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 6 вопроса",callback_data=quiz_photo_callback.new(next="p5"))]])
quiz_photo6= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 7 вопроса",callback_data=quiz_photo_callback.new(next="p6"))]])
quiz_photo7= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 8 вопроса",callback_data=quiz_photo_callback.new(next="p7"))]])
quiz_photo8= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 9 вопроса",callback_data=quiz_photo_callback.new(next="p8"))]])
quiz_photo9= InlineKeyboardMarkup( inline_keyboard=[[InlineKeyboardButton(text="Перейти к фото 10 вопроса",callback_data=quiz_photo_callback.new(next="p9"))]])