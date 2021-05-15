from aiogram.types import CallbackQuery, InputMediaPhoto

from encyclopedia_all_files.Encyclopedia_District.Proletarian_region.photos import Proletarian_photo, max_prol
from encyclopedia_all_files.Encyclopedia_District.Proletarian_region.text import Proletarian_text
from handlers.users.encyclopedia import get_page
from keyboards.inline.callback_datas import place_callback, pagination_call
from keyboards.inline.encyclopedia import get_text, get_page_keyboard
from loader import dp, photo_db



@dp.callback_query_handler(place_callback.filter(item_name="prol_r"))
async def prol_region_pag(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    text= get_page(Proletarian_text)
    photo=get_page(Proletarian_photo)
    await call.message.answer_photo(photo=open(photo_db.get_one_file_name(name=photo), 'rb'), reply_markup=get_page_keyboard(k="prol",max=max_prol))
    await call.message.answer(text=text, reply_markup=get_text(max=max_prol,k="prol_t"))


@dp.callback_query_handler(pagination_call.filter(key="prol"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    photo = get_page(array=Proletarian_photo,page=current_page)
    media=InputMediaPhoto(media=open(photo_db.get_one_file_name(name=photo),'rb'))
    markup=get_page_keyboard(k="prol",max=max_prol,page=current_page)
    await call.message.edit_media(media= media, reply_markup=markup)

@dp.callback_query_handler(pagination_call.filter(key="prol_t"))
async def show_current_page(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=2)
    current_page=int(callback_data.get("page"))
    text=get_page(array=Proletarian_text,page=current_page)
    await call.message.edit_text(text=text, reply_markup=get_text(k="prol_t",max=max_prol,page=current_page))
