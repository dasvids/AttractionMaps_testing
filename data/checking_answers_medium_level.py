import re

from aiogram import types
from aiogram.utils.markdown import hbold

from loader import db

ListPatternsRegexMediumLevel = [
    "^((1)|([оО]дну( звезду)?)|([оО]дин))$",
    "^([Пп][её]тр\s([Аа]лексеевич|2|[iI]{2}|[Вв]торой))$",
    "^(([Пп]ятнадцатый\s)?([Аа]рбитражный\s)?([Аа]пелляционный\s)?[Сс]уд)$",
    "^(['']?(12|[Дд]венадцать)\sстульев['']?)$",
    "^(([Гг]ородская\s[Дд]ума)|[Дд]ума)$",
    "^(([Вв]\s)?1941(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот сорок первом(\s?г((\.)|(оду))?)?)$",
    "^(([Пп][её]тр\s)?[Вв]рангель)$",
    "^(([Фф]рейд(\s*,*\s*|\.|\sи\s)[Юю]нг)|([Юю]нг(\s*,*\s*|\.|\sи\s)[Фф]рейд))$",
    "^(\s*[Аа]мерикански(м|й)\s*(\s[Мм]ост(ом)?)?\s?)$",
    "^(([Вв]\s)?1911(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот одиннадцатом(\s?г((\.)|(оду))?)?)$",
    "^(\s*[Нн]еобарокко\s*)$",
    "^(([Вв]\s)?1901(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот первом(\s?г((\.)|(оду))?)?)$",
    "^(([Вв]\s)?1914(\s?[Гг]((\.)|(од[у]?))?)?)|(([Вв]\s)?[Тт]ысяча девятьсот четырнадцатом(\s?г((\.)|(оду))?)?)$"
]


async def check_answer_medium(message: types.Message, answers):
    # Обнуляем рейтинг
    db.update_rating_medium(message.from_user.id, 0);
    # assert (len(answers) == len(ListPatternsRegexHardLevel))
    res = ""
    for i in range(0, len(answers)):
        if re.search(ListPatternsRegexMediumLevel[i], answers[i], re.IGNORECASE) is not None:
            res += hbold(f"Правильный ответ : {int(i) + 1}\n")
            rate = db.get_rating_medium(message.from_user.id)
            db.update_rating_medium(id=message.from_user.id, rating=rate + 3.0)
        else:
            res += f"Неправильный ответ : {int(i) + 1}\n"
    return res
    # result = re.search(str(ListPatternsRegex[num - 1]), str(str_ans), re.IGNORECASE)
    # if result is not None:
    #     RATE = db.select_user(id=message.from_user.id)[-1]
    #     db.update_rating(id=message.from_user.id, rating=RATE + 3.0)
    #     return "Вопрос " + str(num) + ": Правильный ответ!"
    # else:
    #     return "Вопрос " + str(num) + ": Неправильный ответ!"
