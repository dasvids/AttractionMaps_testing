from aiogram.types import CallbackQuery, InputMediaPhoto

from encyclopedia_all_files.Encyclopedia_District.Kirovsky_region.photos import Kirovsky_photo, max_kir_photo
from encyclopedia_all_files.Encyclopedia_District.Kirovsky_region.text import Kirovsky_text, max_kir
from handlers.users.encyclopedia import get_page

from keyboards.inline.callback_datas import place_callback
from keyboards.inline.encyclopedia import get_page_keyboard, pagination_call, get_text

from loader import dp, photo_db


@dp.callback_query_handler(place_callback.filter(item_name="kir_r"))
async def kir_region_pag(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    text = get_page(Kirovsky_text)
    photo = get_page(Kirovsky_photo)
    await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=photo), 'rb'),
                                    reply_markup=get_page_keyboard(k="kir", max=max_kir_photo))
    await call.message.answer(text=text, reply_markup=get_text(max=max_kir, k="kir_t"))


@dp.callback_query_handler(pagination_call.filter(key="kir"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page = int(callback_data.get("page"))
    photo = get_page(array=Kirovsky_photo, page=current_page)
    media = InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo), 'rb'))
    markup = get_page_keyboard(k="kir", max=max_kir_photo, page=current_page)
    await call.message.edit_media(media=media, reply_markup=markup)


@dp.callback_query_handler(pagination_call.filter(key="kir_t"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page = int(callback_data.get("page"))
    text = get_page(array=Kirovsky_text, page=current_page)
    await call.message.edit_text(text=text, reply_markup=get_text(k="kir_t", max=max_kir, page=current_page))
