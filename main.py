from aiogram import Bot, Dispatcher, executor, types
from config import token
from questions import *
start_text = '''<em>Приветствую тебя в тесте
на знание языка программирования <b>Python</b>😁

Ты сможешь оценить свои знания и возможно расширить их</em>🎓'''

balls = 0

bot = Bot(token)
dp = Dispatcher(bot)

start_markup = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Начать тест' , callback_data='старт')
start_markup.add(button1)

q1_markup = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Да' , callback_data='1-Да')
button2 = types.InlineKeyboardButton('Нет' , callback_data='1-Нет')
button3 = types.InlineKeyboardButton('Ошибку' , callback_data='1-Err')
q1_markup.add(button1,button2,button3)

q2_markup = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('5' , callback_data='2-5')
button2 = types.InlineKeyboardButton('10' , callback_data='2-10')
button3 = types.InlineKeyboardButton('Ошибку' , callback_data='2-Err')
q2_markup.add(button1,button2,button3)

q3_markup = types.InlineKeyboardMarkup()
button0 = types.InlineKeyboardButton('True' , callback_data='3-f')
button1 = types.InlineKeyboardButton('34' , callback_data='3-f')
button2 = types.InlineKeyboardButton('45' , callback_data='3-t')
button3 = types.InlineKeyboardButton('весь список' , callback_data='3-f')
q3_markup.add(button0,button1)
q3_markup.add(button2,button3)

q4_markup = types.InlineKeyboardMarkup()
button0 = types.InlineKeyboardButton('ошибка' , callback_data='4-f')
button1 = types.InlineKeyboardButton('2' , callback_data='4-t')
button2 = types.InlineKeyboardButton('True' , callback_data='4-f')
button3 = types.InlineKeyboardButton('False' , callback_data='4-f')
q4_markup.add(button0,button1)
q4_markup.add(button2,button3)

q5_markup = types.InlineKeyboardMarkup()
button0 = types.InlineKeyboardButton('начнется вечный цикл', callback_data='5-t')
button1 = types.InlineKeyboardButton('4', callback_data='5-f')
button2 = types.InlineKeyboardButton('5', callback_data='5-f')
button3 = types.InlineKeyboardButton('3', callback_data='5-f')
q5_markup.add(button0)
q5_markup.add(button1,button2,button3)

finish_markup = types.InlineKeyboardMarkup()
button0 = types.InlineKeyboardButton('Начать заново', callback_data='гг')
finish_markup.add(button0)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, start_text ,parse_mode='HTML', reply_markup=start_markup)




@dp.callback_query_handler()
async def callback(callback:types.CallbackQuery):
    global balls
    if callback.data == 'старт':
        await callback.answer('START')
        await callback.bot.send_message(callback.message.chat.id , question1 , reply_markup=q1_markup, parse_mode='HTML')
    elif callback.data[0] == '1':
        if callback.data == '1-Да':
            await callback.answer('+ балл 🔥')
            balls+=1
        else:
            await callback.answer('Ответ не правильный🫤')
        await callback.bot.send_message(callback.message.chat.id, question2, reply_markup=q2_markup, parse_mode='HTML')
    elif callback.data[0] == '2':
        if callback.data == '2-10':
            await callback.answer('+ балл 🔥')
            balls+=1
        else:
            await callback.answer('Ответ не правильный🫤')
        await callback.bot.send_message(callback.message.chat.id, question3, reply_markup=q3_markup, parse_mode='HTML')
    elif callback.data[0] == '3':
        if callback.data[2] == 't':
            await callback.answer('+ балл 🔥')
            balls+=1
        else:
            await callback.answer('Ответ не правильный🫤')
        await callback.bot.send_message(callback.message.chat.id, question4, reply_markup=q4_markup, parse_mode='HTML')
    elif callback.data[0] == '4':
        if callback.data[2] == 't':
            await callback.answer('+ балл 🔥')
            balls += 1
        else:
            await callback.answer('Ответ не правильный🫤')
        await callback.bot.send_message(callback.message.chat.id, question5, reply_markup=q5_markup, parse_mode='HTML')
    elif callback.data[0] == '5':
        if callback.data[2] == 't':
            await callback.answer('+ балл 🔥')
            balls += 1
        else:
            await callback.answer('Ответ не правильный🫤')
        await callback.bot.send_message(callback.message.chat.id, f'ОГО, ты набрал целых <b>{balls} баллов</b>🤩\n Продолжай заниматься и тогда ты станешь отличным программистом👨‍🏫' ,
                                        parse_mode='HTML',
                                        reply_markup=finish_markup)
        balls = 0
    elif callback.data == 'гг':
        await callback.answer('START')
        await callback.bot.send_message(callback.message.chat.id, question1, reply_markup=q1_markup, parse_mode='HTML')
executor.start_polling(dp)
