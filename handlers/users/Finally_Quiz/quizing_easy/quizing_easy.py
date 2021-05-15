from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold, hitalic

from handlers.users.Finally_Quiz.quizing_easy.quiz_easy_photo import photo_quiz
from keyboards.inline.callback_datas import quiz_callback
from keyboards.inline.quiz_keyboard import quiz_keyboard1, quiz_keyboard2, quiz_keyboard3, quiz_keyboard4, \
    quiz_keyboard5, quiz_keyboard6, quiz_keyboard7, quiz_keyboard8, quiz_keyboard9, quiz_keyboard10, quiz_photo1
from quiz_all_files.Quiz_Questions.questions_quiz import Easy_Array_Questions

from loader import dp, photo_db, db
from aiogram import types

from states.MachineStates_For_Quiz import QuizEasy


@dp.message_handler(Command("quiz_easy"), state=None)
async def enter_easy_test(message: types.Message):

    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name=photo_quiz[0]), 'rb'),
                               reply_markup=quiz_photo1)
    await message.answer(text=hitalic("Вопрос 1:\n") + Easy_Array_Questions[0], reply_markup=quiz_keyboard1)
    await QuizEasy.Q1.set()

    # @dp.callback_query_handler(quiz_photo_callback.filter(next="p1"),state=QuizEasy.Q1)
    # async def question_1(call: CallbackQuery):
    #     await call.answer(cache_time=60)
    #     await call.message.edit_reply_markup(reply_markup=quiz_photo2)


@dp.callback_query_handler(quiz_callback.filter(next="2"), state=QuizEasy.Q1)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)

    answer1 = callback_data.get('answer')
    await state.update_data(answer1=answer1)
    await call.message.edit_text(text="Вопрос 2:\n" + Easy_Array_Questions[1], reply_markup=quiz_keyboard2)
    # await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name='easy_question_1'), 'rb'))
    await QuizEasy.Q2.set()


@dp.callback_query_handler(quiz_callback.filter(next="3"), state=QuizEasy.Q2)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer2 = callback_data.get('answer')
    await state.update_data(answer2=answer2)
    await call.message.edit_text(text="Вопрос 3:\n" + Easy_Array_Questions[2], reply_markup=quiz_keyboard3)
    await QuizEasy.Q3.set()


@dp.callback_query_handler(quiz_callback.filter(next="4"), state=QuizEasy.Q3)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer3 = callback_data.get('answer')
    await state.update_data(answer3=answer3)
    await call.message.edit_text(text="Вопрос 4:\n" + Easy_Array_Questions[3], reply_markup=quiz_keyboard4)
    await QuizEasy.Q4.set()


@dp.callback_query_handler(quiz_callback.filter(next="5"), state=QuizEasy.Q4)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer4 = callback_data.get('answer')
    await state.update_data(answer4=answer4)
    await call.message.edit_text(text="Вопрос 5:\n" + Easy_Array_Questions[4], reply_markup=quiz_keyboard5)
    await QuizEasy.Q5.set()


@dp.callback_query_handler(quiz_callback.filter(next="6"), state=QuizEasy.Q5)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer5 = callback_data.get('answer')
    await state.update_data(answer5=answer5)
    await call.message.edit_text(text="Вопрос 6:\n" + Easy_Array_Questions[5], reply_markup=quiz_keyboard6)
    await QuizEasy.Q6.set()


@dp.callback_query_handler(quiz_callback.filter(next="7"), state=QuizEasy.Q6)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer6 = callback_data.get('answer')
    await state.update_data(answer6=answer6)
    await call.message.edit_text(text="Вопрос 7:\n" + Easy_Array_Questions[6], reply_markup=quiz_keyboard7)
    await QuizEasy.Q7.set()


@dp.callback_query_handler(quiz_callback.filter(next="8"), state=QuizEasy.Q7)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer7 = callback_data.get('answer')
    await state.update_data(answer7=answer7)
    await call.message.edit_text(text="Вопрос 8:\n" + Easy_Array_Questions[7], reply_markup=quiz_keyboard8)
    await QuizEasy.Q8.set()


@dp.callback_query_handler(quiz_callback.filter(next="9"), state=QuizEasy.Q8)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer8 = callback_data.get('answer')
    await state.update_data(answer8=answer8)
    await call.message.edit_text(text="Вопрос 9:\n" + Easy_Array_Questions[8], reply_markup=quiz_keyboard9)
    await QuizEasy.Q9.set()


@dp.callback_query_handler(quiz_callback.filter(next="10"), state=QuizEasy.Q9)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer9 = callback_data.get('answer')
    await state.update_data(answer9=answer9)
    await call.message.edit_text(text="Вопрос 10:\n" + Easy_Array_Questions[9], reply_markup=quiz_keyboard10)
    await QuizEasy.Q10.set()


@dp.callback_query_handler(quiz_callback.filter(next="11"), state=QuizEasy.Q10)
async def question_1(call: CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer(cache_time=60)
    answer10 = callback_data.get('answer')
    await state.update_data(answer10=answer10)
    await call.message.edit_text(text="Спасибо за ваши ответы\n Чтобы закончить викторину нажмите /finish",
                                 reply_markup=None)
    await QuizEasy.Q11.set()


# Выход из викторины
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q1)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q2)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q3)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q4)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q5)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q6)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q7)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q8)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q9)
@dp.callback_query_handler(quiz_callback.filter(answer="End"), state=QuizEasy.Q10)
async def cancel_quiz(call: CallbackQuery):
    await call.message.edit_text(text="Спасибо за ваши ответы\n Чтобы закончить викторину нажмите /finish")
    # Отправляем пустую клавиатуру, т.е. выходит из клавиатуры
    await QuizEasy.Q11.set()
    await call.message.edit_reply_markup(reply_markup=None)


Right_Answer_List_Question_Easy = [
    "Георгия Победоносца",
    "КСА - Союз ТМА-10",
    "Великой Отечественной войне",
    "Бульвар Дружбы",
    "Тихий Дон",
    "Бронзовый век",
    "был владельцем сз",
    "Старообрядчество",
    "2018г",
    "Библиотека ЮФУ(РГУ)"
]


@dp.message_handler(Command("finish"), state=QuizEasy.Q11)
async def finish_test(message: types.Message, state: FSMContext):
    # # получаем все данные
    data = await state.get_data()

    # пишем их в переменные
    answer_first = data.get("answer1")
    answer_second = data.get("answer2")
    answer_third = data.get("answer3")
    answer_fourth = data.get("answer4")
    answer_5th = data.get("answer5")
    answer_6th = data.get("answer6")
    answer_7th = data.get("answer7")
    answer_8th = data.get("answer8")
    answer_9th = data.get("answer9")
    answer_10th = data.get("answer10")

    await message.answer("Ваши ответы:")

    Answer_List_Question_Easy = [answer_first, answer_second, answer_third, answer_fourth, answer_5th, answer_6th,
                                 answer_7th, answer_8th, answer_9th, answer_10th]

    # Обнуляем рейтинг
    db.update_rating_easy(message.from_user.id, 0);

    for index in range(0, 10):
        if (Answer_List_Question_Easy[index] == Right_Answer_List_Question_Easy[index]):
            await message.answer(text=f'Вопрос {index + 1}:Правильный ответ!')
            rate = db.get_rating_easy(message.from_user.id)
            db.update_rating_easy(id=message.from_user.id, rating=rate + 1.0)
        else:
            await message.answer(text=f'Вопрос {index + 1}:Неправильный ответ!')
    await message.answer("Чтобы увидеть свой рейтинг, после прохождения викторины нажмите /get_my_rating")

    await state.finish()
