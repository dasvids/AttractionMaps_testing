from aiogram.types import CallbackQuery, InputMediaPhoto

from encyclopedia_all_files.Encyclopedia_District.Soviet_region.photos import Sovet_photo, max_sov
from encyclopedia_all_files.Encyclopedia_District.Soviet_region.text import Sovet_text
from handlers.users.encyclopedia import get_page
from keyboards.inline.callback_datas import place_callback, pagination_call
from keyboards.inline.encyclopedia import get_page_keyboard, get_text
from loader import dp, photo_db

@dp.callback_query_handler(place_callback.filter(item_name="sov_r"))
async def sov_region_pag(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    text= get_page(Sovet_text)
    photo=get_page(Sovet_photo)
    await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=photo), 'rb'), reply_markup=get_page_keyboard(k="sov",max=max_sov))
    await call.message.answer(text=text, reply_markup=get_text(max=max_sov,k="sov_t"))


@dp.callback_query_handler(pagination_call.filter(key="sov"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    photo = get_page(array=Sovet_photo,page=current_page)
    media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo),'rb'))
    markup=get_page_keyboard(k="sov",max=max_sov,page=current_page)
    await call.message.edit_media(media= media, reply_markup=markup)

@dp.callback_query_handler(pagination_call.filter(key="sov_t"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    text=get_page(array=Sovet_text,page=current_page)
    await call.message.edit_text(text=text, reply_markup=get_text(k="sov_t",max=max_sov,page=current_page))
