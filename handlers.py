from loader import dp, bot
from aiogram import types
import game as gm
from aiogram.types import ContentType, Message


@dp.message_handler(commands=['start', 'help'])
async def mes_start(message: types.Message):
    gm.activate_game(message.from_user.id)
    await message.answer(f'Приветствую. На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
    await message.answer(f'Команды: \n /game - начать игру \n /set xxx - задать количество конфет (по умолчанию 150), указать не менее 29, не более 1000 \n /end - остановить игру \n /score - счет побед')


@dp.message_handler(commands=['game'])
async def mes_game(message: types.Message):
    if gm.is_game_running(message.from_user.id):
        remainder = gm.get_remainder(message.from_user.id)
        await message.answer(f'Игра уже идет, осталось {remainder} конфет')
    else:
        gm.game_start(message.from_user.id)
        await message.answer(f'Игра началась')

        if gm.first_move() == 2:
            countForDelete = gm.move(message.from_user.id)
            remainder = gm.get_remainder(message.from_user.id)
            await message.answer(f'Первый ход бота, забрал {countForDelete} конфет, осталось {remainder} конфет')
        else:
            remainder = gm.get_remainder(message.from_user.id)
            await message.answer(f'Первый ход пользователя, осталось {remainder} конфет')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    if gm.is_game_running(message.from_user.id):
        await message.answer(f'Игра уже идет')
    else:
        try:
            count = message.text.split()[1]
            total = int(count)
        except:
            await message.answer(f'Количество указано не верно.')
        else:
            if total < 29 or total > 1000:
                await message.answer(f'Количество указано не верно.')
            else:
                gm.set_candies(message.from_user.id, total)
                await message.answer(f'Установили кол-во конфет в размере {total}')


@dp.message_handler(commands=['score'])
async def mes_score(message: types.Message):
    win_loss = gm.get_win_loss(message.from_user.id)
    await message.answer(f'Победы - {win_loss[0]}, поражения - {win_loss[1]}')


@dp.message_handler(commands=['end'])
async def mes_end(message: types.Message):
    gm.game_end(message.from_user.id)
    await message.answer('Игра остановлена.')


@dp.message_handler()
async def mes_all(message: types.Message):
    if message.text.isdigit():
        count = int(message.text)
        remainder = gm.get_remainder(message.from_user.id)
        if count > 28 or count < 1 or count > remainder:
            await bot.send_message(message.from_user.id, f'Столько взять конфет нельзя, конфет осталось {remainder}')
        else:
            gm.move_player(message.from_user.id, count)
            if gm.check_winner(message.from_user.id) != False:
                gm.win_loss_counter(message.from_user.id)

                if gm.check_winner(message.from_user.id) == 1:
                    await bot.send_message(message.from_user.id, f'Победил пользователь. Игра окончена.')
                else:
                    await bot.send_message(message.from_user.id, f'Победил бот. Игра окончена.')
                gm.game_end(message.from_user.id)
            else:
                countForDelete = gm.move(message.from_user.id)
                remainder = gm.get_remainder(message.from_user.id)
                await bot.send_message(message.from_user.id, f'Бот забрал {countForDelete} конфет. Осталось {remainder}')

                if gm.check_winner(message.from_user.id) != False:
                    gm.win_loss_counter(message.from_user.id)

                    if gm.check_winner(message.from_user.id) == 1:
                        await bot.send_message(message.from_user.id, f'Победил пользователь. Игра окончена.')
                    else:
                        await bot.send_message(message.from_user.id, f'Победил бот. Игра окончена.')
                    gm.game_end(message.from_user.id)
    else:
        await bot.send_message(message.from_user.id, f'Не число')
    # await message.answer(f'Гляди, че поймал - {message.text}')
