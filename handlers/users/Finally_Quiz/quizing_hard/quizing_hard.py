from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.checking_answers_hard_level import check_answer_hard

from quiz_all_files.Quiz_Questions.questions_quiz import Hard_Array_Questions
from loader import dp, photo_db
from aiogram import types

from states.MachineStates_For_Quiz import QuizHard

user_answers = []


@dp.message_handler(Command("quiz_hard"), state=None)
async def enter_hard_test(message: types.Message):
    # присылаем фотку и клаву
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_1'), 'rb'))
    await message.answer("Вопрос 1:\n" + Hard_Array_Questions[0])
    await QuizHard.Q1.set()


@dp.message_handler(state=QuizHard.Q1)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_first_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer1=answer_first_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_2'), 'rb'))
    await message.answer("Вопрос 2:\n" + Hard_Array_Questions[1])
    await QuizHard.Q15.set()


@dp.message_handler(state=QuizHard.Q2)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_2nd_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer2=answer_2nd_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_3'), 'rb'))
    await message.answer("Вопрос 3:\n" + Hard_Array_Questions[2])
    await QuizHard.Q3.set()


@dp.message_handler(state=QuizHard.Q3)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_3rd_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer3=answer_3rd_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_4'), 'rb'))
    await message.answer("Вопрос 4:\n" + Hard_Array_Questions[3])
    await QuizHard.Q4.set()


@dp.message_handler(state=QuizHard.Q4)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_4th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer4=answer_4th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_5'), 'rb'))
    await message.answer("Вопрос 5:\n" + Hard_Array_Questions[4])
    await QuizHard.Q5.set()


@dp.message_handler(state=QuizHard.Q5)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_5th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer5=answer_5th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_6'), 'rb'))
    await message.answer("Вопрос 6:\n" + Hard_Array_Questions[5])
    await QuizHard.Q6.set()


@dp.message_handler(state=QuizHard.Q6)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_6th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer6=answer_6th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_7'), 'rb'))
    await message.answer("Вопрос 7:\n" + Hard_Array_Questions[6])
    await QuizHard.Q7.set()


@dp.message_handler(state=QuizHard.Q7)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_7th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer7=answer_7th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_8'), 'rb'))
    await message.answer("Вопрос 8:\n" + Hard_Array_Questions[7])
    await QuizHard.Q8.set()


@dp.message_handler(state=QuizHard.Q8)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_8th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer8=answer_8th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_9'), 'rb'))
    await message.answer("Вопрос 9:\n" + Hard_Array_Questions[8])
    await QuizHard.Q9.set()


@dp.message_handler(state=QuizHard.Q9)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_9th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer9=answer_9th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_10'), 'rb'))
    await message.answer("Вопрос 10:\n" + Hard_Array_Questions[9])
    await QuizHard.Q10.set()


@dp.message_handler(state=QuizHard.Q10)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_10th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer10=answer_10th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_11'), 'rb'))
    await message.answer("Вопрос 11:\n" + Hard_Array_Questions[10])
    await QuizHard.Q11.set()


@dp.message_handler(state=QuizHard.Q11)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer11=answer_11th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_12'), 'rb'))
    await message.answer("Вопрос 12:\n" + Hard_Array_Questions[11])
    await QuizHard.Q12.set()


@dp.message_handler(state=QuizHard.Q12)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_12th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer12=answer_12th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_13'), 'rb'))
    await message.answer("Вопрос 13:\n" + Hard_Array_Questions[12])
    await QuizHard.Q13.set()


@dp.message_handler(state=QuizHard.Q13)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer13=answer_11th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_14'), 'rb'))
    await message.answer("Вопрос 14:\n" + Hard_Array_Questions[13])
    await QuizHard.Q14.set()


@dp.message_handler(state=QuizHard.Q14)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем и пишем данные
    answer_11th_hard = message.text
    user_answers.append(message.text)
    await state.update_data(answer14=answer_11th_hard)

    # отправляем новую фотку + вопрос
    await message.answer_photo(photo=open(photo_db.get_one_file_name(name='hard_question_15'), 'rb'))
    await message.answer("Вопрос 15:\n" + Hard_Array_Questions[14])
    await QuizHard.Q15.set()


@dp.message_handler(state=QuizHard.Q15)
async def answer_test_1(message: types.Message, state: FSMContext):
    # сохраняем последний ответ
    user_answers.append(message.text)
    await state.update_data(answer15=message.text)
    total_answers = await check_answer_hard(message, user_answers)
    await message.answer(total_answers)
    await state.finish()
