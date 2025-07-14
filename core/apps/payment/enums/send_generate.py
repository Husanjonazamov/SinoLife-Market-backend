import telebot
from config.env import env
from payme import Payme
from click_up import ClickUp
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

PAYME_ID = env.str("PAYME_ID")
PAYME_KEY = env.str("PAYME_KEY")

CLICK_SERVICE_ID = env.int("CLICK_SERVICE_ID")
CLICK_MERCHANT_ID = env.int("CLICK_MERCHANT_ID")


BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN = env.int("ADMIN")

bot = telebot.TeleBot(token=BOT_TOKEN)

payme = Payme(
    payme_id=PAYME_ID,
    payme_key=PAYME_KEY
)



click_up = ClickUp(
    service_id=CLICK_SERVICE_ID,
    merchant_id=CLICK_MERCHANT_ID
)

def send_generate_payment(order):
    user_id = order.user.tg_id
    payment_type = order.payment_type
    order_id = order.id
    total = order.total
    amount = total * 100

    if payment_type == "payme":
        pay_link = payme.initializer.generate_pay_link(
            id=int(order_id),
            amount=amount,
            return_url="https://t.me/sinolifemarket_bot"
        )
    else:
        pay_link = click_up.initializer.generate_pay_link(
            id=user_id,
            amount=amount,
            return_url="https://t.me/sinolifemarket_bot"
        )
        
        
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="💳 To'lov qilish", url=pay_link)
    keyboard.add(button)

    bot.send_message(
        chat_id=user_id,
        text=f"💸 Hurmatli foydalanuvchi!\nBuyurtmangiz uchun to'lovni amalga oshiring 👇",
        reply_markup=keyboard
    )