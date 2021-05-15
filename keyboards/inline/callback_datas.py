from aiogram.utils.callback_data import CallbackData

# колл бекл для покупки,
# действие, название, масштаб
buy_callback = CallbackData("buy", "item_name", "scale")

place_callback = CallbackData("show", "item_name")

pagination_call=CallbackData("pagionator","key","page")

quiz_callback = CallbackData("quiz","next","answer")

quiz_photo_callback= CallbackData("photo","next")