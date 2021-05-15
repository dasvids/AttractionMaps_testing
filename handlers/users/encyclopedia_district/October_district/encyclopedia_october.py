from aiogram.types import CallbackQuery, InputMediaPhoto

from encyclopedia_all_files.Encyclopedia_District.October_region.photos import October_photo, max_oct
from encyclopedia_all_files.Encyclopedia_District.October_region.text import October_text
from handlers.users.encyclopedia import  get_page
from keyboards.inline.callback_datas import place_callback, pagination_call
from keyboards.inline.encyclopedia import  get_text, get_page_keyboard
from loader import dp, photo_db

@dp.callback_query_handler(place_callback.filter(item_name="oct_r"))
async def oct_region_pag(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    text= get_page(October_text)
    photo=get_page(October_photo)
    await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=photo), 'rb'), reply_markup=get_page_keyboard(k="oct",max=max_oct))
    await call.message.answer(text=text, reply_markup=get_text(max=max_oct,k="oct_t"))


@dp.callback_query_handler(pagination_call.filter(key="oct"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    photo = get_page(array=October_photo,page=current_page)
    media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo),'rb'))
    markup=get_page_keyboard(k="oct",max=max_oct,page=current_page)
    await call.message.edit_media(media= media, reply_markup=markup)

@dp.callback_query_handler(pagination_call.filter(key="oct_t"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    text=get_page(array=October_text,page=current_page)
    await call.message.edit_text(text=text, reply_markup=get_text(k="oct_t",max=max_oct,page=current_page))
