import os
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset di Railway Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

AKSES_LAYANAN = "https://cutt.ly/LytNXbTV"
LIVE_SUPPORT = (
    "https://static.zdassets.com/web_widget/latest/liveChat.html?v=10"
    "#key=fifa777.zendesk.com&settings=JTdCJTIyd2ViV2lkZ2V0JTIyJTNBJTdCJTIy"
    "Y2hhdCUyMiUzQSU3QiUyMnRpdGxlJTIyJTNBbnVsbCUyQyUyMm1lbnVPcHRpb25zJTIy"
    "JTNBJTdCJTIyZW1haWxUcmFuc2NyaXB0JTIyJTNBdHJ1ZSU3RCUyQyUyMmRlcGFydG1l"
    "bnRzJTIyJTNBJTdCJTdEJTJDJTIycHJlY2hhdEZvcm0lMjIlM0ElN0IlMjJkZXBhcnRt"
    "ZW50TGFiZWwlMjIlM0FudWxsJTJDJTIyZ3JlZXRpbmclMjIlM0FudWxsJTdEJTJDJTIy"
    "b2ZmbGluZUZvcm0lMjIlM0ElN0IlMjJncmVldGluZyUyMiUzQW51bGwlN0QlMkMlMjJj"
    "b25jaWVyZ2UlMjIlM0ElN0IlMjJhdmF0YXJQYXRoJTIyJTNBbnVsbCUyQyUyMm5hbWUl"
    "MjIlM0FudWxsJTJDJTIydGl0bGUlMjIlM0FudWxsJTdEJTdEJTJDJTIyY29sb3IlMjIl"
    "M0ElN0IlMjJhcnRpY2xlTGlua3MlMjIlM0ElMjIlMjIlMkMlMjJidXR0b24lMjIlM0El"
    "MjIlMjIlMkMlMjJoZWFkZXIlMjIlM0ElMjIlMjIlMkMlMjJsYXVuY2hlciUyMiUzQSUy"
    "MiUyMiUyQyUyMmxhdW5jaGVyVGV4dCUyMiUzQSUyMiUyMiUyQyUyMnJlc3VsdExpc3Rz"
    "JTIyJTNBJTIyJTIyJTJDJTIydGhlbWUlMjIlM0FudWxsJTdEJTdEJTdE"
    "&&locale=en-us&title=Web%20Widget%20Live%20Chat"
)

BANNER_PATH = os.path.join("assets", "fifa777-banner.jpg")

WELCOME_TEXT = """🔥 <b>FIFA777 OFFICIAL</b> 🔥

Selamat datang di layanan resmi Fifa777 ⚽

💸 Transaksi deposit QRIS proses hanya 1 detik
🏧 Penarikan berapapun dibayar tuntas tanpa ribet

Kami hadir dengan sistem cepat, stabil & pelayanan terbaik untuk Anda."""


def menu_buttons():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🌐 LINK RESMI FIFA777", url=AKSES_LAYANAN),
        InlineKeyboardButton("💬 LIVE CHAT SUPPORT", url=LIVE_SUPPORT),
    )
    return markup


def send_welcome(chat_id):
    if os.path.isfile(BANNER_PATH):
        with open(BANNER_PATH, "rb") as banner:
            bot.send_photo(
                chat_id,
                banner,
                caption=WELCOME_TEXT,
                reply_markup=menu_buttons(),
            )
    else:
        logging.warning("Banner tidak ditemukan: %s", BANNER_PATH)
        bot.send_message(
            chat_id,
            WELCOME_TEXT,
            reply_markup=menu_buttons(),
            disable_web_page_preview=True,
        )


@bot.message_handler(commands=["start"])
def start(message):
    send_welcome(message.chat.id)


@bot.message_handler(func=lambda message: True)
def reply_all(message):
    send_welcome(message.chat.id)


if __name__ == "__main__":
    logging.info("Bot Fifa777 berjalan...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)
