import telebot
from config.env import env
from decimal import Decimal

BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN = env.int("ADMIN")

bot = telebot.TeleBot(token=BOT_TOKEN)


def order_caption(**kwargs):
    caption = ""
    caption += "🧾 <b>To‘lov Tafsilotlari</b>\n\n"
    
    caption += f"🆔 <b>Buyurtma raqami:</b> {kwargs['order_id']}\n"
    caption += f"💰 <b>To‘lov summasi:</b> {Decimal(kwargs['total']):,} so'm\n"
    caption += f"⏰ <b>Buyurtma vaqti:</b> {kwargs['date']}\n"

    return caption


def send_payment(order, perform_time):
    caption = order_caption(
        order_id=order.id,
        total=order.total,
        date=perform_time.strftime("%Y-%m-%d %H:%M")
    )
    
    bot.send_message(
        chat_id=ADMIN,
        text=caption,
        parse_mode="HTML"
    )
