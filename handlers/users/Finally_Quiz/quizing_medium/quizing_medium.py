from typing import List, Any, Coroutine

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.checking_answers_medium_level import check_answer_medium_1, check_answer_medium_2, check_answer_medium_3, \
    check_answer_medium_4, check_answer_medium_5, check_answer_medium_6, check_answer_medium_7, check_answer_medium_8, \
    check_answer_medium_9, check_answer_medium_10, check_answer_medium_11, check_answer_medium_12, \
    check_answer_medium_13, check_answer_medium
from quiz_all_files.Quiz_Questions.questions_quiz import Medium_Array_Questions
from loader import dp, photo_db
from aiogram import types

from states.MachineStates_For_Quiz import QuizMedium

answer = []


@dp.message_handler(Command("quiz_medium"), state=None)
async def enter_easy_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_1'), 'rb'))
    await message.answer("Вопрос 1:\n" + Medium_Array_Questions[0])
    await QuizMedium.Q1.set()


@dp.message_handler(state=QuizMedium.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer.append(message.text)
    await state.update_data(answer1=answer[0])

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_2'), 'rb'))
    await message.answer("Вопрос 2:\n" + Medium_Array_Questions[1])

    await QuizMedium.Q2.set()


@dp.message_handler(state=QuizMedium.Q2)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_second_medium = message.text
    await state.update_data(answer2=answer_second_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_3'), 'rb'))
    await message.answer("Вопрос 3:\n" + Medium_Array_Questions[2])

    await QuizMedium.Q3.set()


@dp.message_handler(state=QuizMedium.Q3)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_third_medium = message.text
    await state.update_data(answer3=answer_third_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_4'), 'rb'))
    await message.answer("Вопрос 4:\n" + Medium_Array_Questions[3])

    await QuizMedium.Q4.set()


@dp.message_handler(state=QuizMedium.Q4)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_4th_medium = message.text
    await state.update_data(answer4=answer_4th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_5'), 'rb'))
    await message.answer("Вопрос 5:\n" + Medium_Array_Questions[4])

    await QuizMedium.Q5.set()


@dp.message_handler(state=QuizMedium.Q5)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_5th_medium = message.text
    await state.update_data(answer5=answer_5th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_6'), 'rb'))
    await message.answer("Вопрос 6:\n" + Medium_Array_Questions[5])

    await QuizMedium.Q6.set()


@dp.message_handler(state=QuizMedium.Q6)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_6th_medium = message.text
    await state.update_data(answer6=answer_6th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_7'), 'rb'))
    await message.answer("Вопрос 7:\n" + Medium_Array_Questions[6])

    await QuizMedium.Q7.set()


@dp.message_handler(state=QuizMedium.Q7)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_7th_medium = message.text
    await state.update_data(answer7=answer_7th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_8'), 'rb'))
    await message.answer("Вопрос 8:\n" + Medium_Array_Questions[7])

    await QuizMedium.Q8.set()


@dp.message_handler(state=QuizMedium.Q8)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_8th_medium = message.text
    await state.update_data(answer8=answer_8th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_9'), 'rb'))
    await message.answer("Вопрос 9:\n" + Medium_Array_Questions[8])

    await QuizMedium.Q9.set()


@dp.message_handler(state=QuizMedium.Q9)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_9th_medium = message.text
    await state.update_data(answer9=answer_9th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_10'), 'rb'))
    await message.answer("Вопрос 10:\n" + Medium_Array_Questions[9])

    await QuizMedium.Q10.set()


@dp.message_handler(state=QuizMedium.Q10)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_10th_medium = message.text
    await state.update_data(answer10=answer_10th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_11'), 'rb'))
    await message.answer("Вопрос 11:\n" + Medium_Array_Questions[10])

    await QuizMedium.Q11.set()


@dp.message_handler(state=QuizMedium.Q11)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_medium = message.text
    await state.update_data(answer9=answer_11th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_12'), 'rb'))
    await message.answer("Вопрос 12:\n" + Medium_Array_Questions[11])

    await QuizMedium.Q12.set()


@dp.message_handler(state=QuizMedium.Q12)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_12th_medium = message.text
    await state.update_data(answer12=answer_12th_medium)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='medium_question_13'), 'rb'))
    await message.answer("Вопрос 13:\n" + Medium_Array_Questions[12])

    await QuizMedium.Q13.set()


@dp.message_handler(state=QuizMedium.Q13)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем последний ответ
    await state.update_data(answer13=message.text)
    # сохраняем и пишем данные
    data = await state.get_data()

    checked = []

    for i in range(len(data)+1):
        checked.append(await check_answer_medium(message, data.get("answer" + str(i+1)), i+1))

    # checked.append(await check_answer_medium_1(message, data.get("answer1")))
    # checked.append(await check_answer_medium_2(message, data.get("answer2")))
    # checked.append(await check_answer_medium_3(message, data.get("answer3")))
    # checked.append(await check_answer_medium_4(message, data.get("answer4")))
    # checked.append(await check_answer_medium_5(message, data.get("answer5")))
    # checked.append(await check_answer_medium_6(message, data.get("answer6")))
    # checked.append(await check_answer_medium_7(message, data.get("answer7")))
    # checked.append(await check_answer_medium_8(message, data.get("answer8")))
    # checked.append(await check_answer_medium_9(message, data.get("answer9")))
    # checked.append(await check_answer_medium_10(message, data.get("answer10")))
    # checked.append(await check_answer_medium_11(message, data.get("answer11")))
    # checked.append(await check_answer_medium_12(message, data.get("answer12")))
    # checked.append(await check_answer_medium_13(message, message.text))

    await message.answer('\n'.join(checked))
    await state.finish()
