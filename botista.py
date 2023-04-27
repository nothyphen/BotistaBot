#!/usr/bin/python3

import logging
import instaloader
from aiogram import Bot, Dispatcher, executor, types
import os, shutil

API_TOKEN = ''
INSTA_USER = ''
INSTA_PASS = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("سلام خیلی خوش اومدین به باتستا جایی که میتونین همه ی پروفایل هارو دانلود کنین :)")
    await message.answer("لطفا ایدی اینستاگرام اکانت مورد نظز رو بدون @ وارد کنین.")

@dp.message_handler(commands=['downpost'])
async def send_welcome(message: types.Message):
    await message.answer("لطفا ایدی اینستاگرام اکانت مورد نظز رو بدون @ وارد کنین.")

@dp.message_handler(content_types=['text'])
async def give(message: types.Message):
    TargetUser = message.text.lower().replace(' ', '')

    ig = instaloader.Instaloader(download_pictures=False, download_videos=False, download_video_thumbnails=False, download_geotags=False, download_comments=False)
    ig.login(INSTA_USER, INSTA_PASS)
    ig.download_profile(TargetUser, profile_pic_only=True)
    print("Done")
    ll = os.listdir(TargetUser)

    for item in ll:
        if ".jpg" in item:
            photo = item

    route = f"{TargetUser}/{photo}"
    await bot.send_photo(chat_id=message.chat.id, photo=open(route, "rb"))
    await message.animation("بفرمایین به همین خوش مزگی :))))")
    shutil.rmtree(TargetUser)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)