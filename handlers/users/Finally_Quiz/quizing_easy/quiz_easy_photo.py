from aiogram.types import CallbackQuery, InputMediaPhoto

from keyboards.inline.callback_datas import quiz_photo_callback
from keyboards.inline.quiz_keyboard import quiz_photo2, quiz_photo3, quiz_photo4, quiz_photo5, quiz_photo6, quiz_photo7, \
    quiz_photo8, quiz_photo9
from loader import dp, photo_db
from states import QuizEasy

photo_quiz=['easy_question_1','easy_question_2','easy_question_3','easy_question_4','easy_question_5','easy_question_6','easy_question_7',
            'easy_question_8','easy_question_9','easy_question_10']

@dp.callback_query_handler(quiz_photo_callback.filter(next="p1"),state=QuizEasy.Q1)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[1]), 'rb')),reply_markup=quiz_photo2)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p1"),state=QuizEasy.Q2)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[1]), 'rb')),reply_markup=quiz_photo2)
# 2
@dp.callback_query_handler(quiz_photo_callback.filter(next="p2"),state=QuizEasy.Q2)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[2]), 'rb')),reply_markup=quiz_photo3)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p2"),state=QuizEasy.Q3)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[2]), 'rb')),reply_markup=quiz_photo3)

# 3
@dp.callback_query_handler(quiz_photo_callback.filter(next="p3"),state=QuizEasy.Q3)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[3]), 'rb')),reply_markup=quiz_photo4)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p3"),state=QuizEasy.Q4)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[3]), 'rb')),reply_markup=quiz_photo4)

# 4
@dp.callback_query_handler(quiz_photo_callback.filter(next="p4"),state=QuizEasy.Q4)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[4]), 'rb')),reply_markup=quiz_photo5)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p4"),state=QuizEasy.Q5)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[4]), 'rb')),reply_markup=quiz_photo5)

# 5
@dp.callback_query_handler(quiz_photo_callback.filter(next="p5"),state=QuizEasy.Q5)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[5]), 'rb')),reply_markup=quiz_photo6)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p5"),state=QuizEasy.Q6)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[5]), 'rb')),reply_markup=quiz_photo6)

# 6
@dp.callback_query_handler(quiz_photo_callback.filter(next="p6"),state=QuizEasy.Q6)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[6]), 'rb')),reply_markup=quiz_photo7)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p6"),state=QuizEasy.Q7)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[6]), 'rb')),reply_markup=quiz_photo7)

# 7
@dp.callback_query_handler(quiz_photo_callback.filter(next="p7"),state=QuizEasy.Q7)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[7]), 'rb')),reply_markup=quiz_photo8)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p7"),state=QuizEasy.Q8)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[7]), 'rb')),reply_markup=quiz_photo8)

# 8
@dp.callback_query_handler(quiz_photo_callback.filter(next="p8"),state=QuizEasy.Q8)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[8]), 'rb')),reply_markup=quiz_photo9)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p8"),state=QuizEasy.Q9)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[8]), 'rb')),reply_markup=quiz_photo9)

# 9
@dp.callback_query_handler(quiz_photo_callback.filter(next="p9"),state=QuizEasy.Q9)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[9]), 'rb')))
    await call.message.edit_reply_markup(reply_markup=None)

@dp.callback_query_handler(quiz_photo_callback.filter(next="p9"),state=QuizEasy.Q10)
async def question_1(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.edit_media(media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo_quiz[9]), 'rb')))
    await call.message.edit_reply_markup(reply_markup=None)