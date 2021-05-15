from aiogram.types import CallbackQuery, InputMediaPhoto

from encyclopedia_all_files.Encyclopedia_District.MayDay_region.photos import MayDay_photo
from encyclopedia_all_files.Encyclopedia_District.MayDay_region.text import MayDay_text, max_perv
from handlers.users.encyclopedia import get_page
from keyboards.inline.callback_datas import place_callback, pagination_call
from keyboards.inline.encyclopedia import get_text, get_page_keyboard
from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="perv_r"))
async def perv_region_pag(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    text= get_page(MayDay_text)
    photo=get_page(MayDay_photo)
    await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=photo), 'rb'), reply_markup=get_page_keyboard(k="perv",max=max_perv))
    await call.message.answer(text=text, reply_markup=get_text(max=max_perv,k="perv_t"))


@dp.callback_query_handler(pagination_call.filter(key="perv"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    photo = get_page(array=MayDay_photo,page=current_page)
    media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo),'rb'))
    markup=get_page_keyboard(k="perv",max=max_perv,page=current_page)
    await call.message.edit_media(media= media, reply_markup=markup)

@dp.callback_query_handler(pagination_call.filter(key="perv_t"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    text=get_page(array=MayDay_text,page=current_page)
    await call.message.edit_text(text=text, reply_markup=get_text(k="perv_t",max=max_perv,page=current_page))
