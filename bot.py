from pyrogram import Client, filters
from pyrogram.types import Message

# API اطلاعات ربات تلگرام خود را در اینجا قرار دهید
api_id = "12648220"
api_hash = "23efa24ab816730374a508bcca01fdf9"
bot_token = "6740060058:AAF8Fcru8GZLpZ6s9IyYLrI8sXcBec0cooQ"

# ایجاد نمونه از ربات
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# تابع برای پردازش پیام‌های دریافتی
@app.on_message(filters.private & filters.text)
async def handle_messages(client: Client, message: Message):
    # دریافت متن پیام (نام ارسال شده)
    name = message.text

    # ارسال نام به تلگرام شما
    await client.send_message("self", f"Name received: {name}")

# شروع اجرای ربات
app.run()
