from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [
                                     KeyboardButton(text="Namoz vaqtlari"), KeyboardButton(text="Ismlar ma'nosi")
                                 ], [
                                     KeyboardButton(text="Talab va Takliflar")
                                 ],
                             ]
                             )