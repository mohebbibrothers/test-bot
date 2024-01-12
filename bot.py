from pyrogram import Client, filters
from pyrogram.types import Message

# API اطلاعات ربات تلگرام خود را در اینجا قرار دهید
api_id = "12648220"
api_hash = "23efa24ab816730374a508bcca01fdf9"
bot_token = "6740060058:AAF8Fcru8GZLpZ6s9IyYLrI8sXcBec0cooQ"

# ایجاد نمونه از ربات
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# تابع برای پردازش پیام‌های دریافتی
@bot.on_message()
async def get_info(client, message):

    await bot.send_message("me", message.text)

# شروع اجرای ربات
bot.run()
