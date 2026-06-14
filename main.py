import os
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset di Railway Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

AKSES_LAYANAN = "https://cutt.ly/KtTxXam4"
LIVE_SUPPORT = "https://static.zdassets.com/web_widget/latest/liveChat.html?v=10#key=fifa777.zendesk.com&settings=JTdCJTIyd2ViV2lkZ2V0JTIyJTNBJTdCJTIyY2hhdCUyMiUzQSU3QiUyMnRpdGxlJTIyJTNBbnVsbCUyQyUyMm1lbnVPcHRpb25zJTIyJTNBJTdCJTIyZW1haWxUcmFuc2NyaXB0JTIyJTNBdHJ1ZSU3RCUyQyUyMmRlcGFydG1lbnRzJTIyJTNBJTdCJTdEJTJDJTIycHJlY2hhdEZvcm0lMjIlM0ElN0IlMjJkZXBhcnRtZW50TGFiZWwlMjIlM0FudWxsJTJDJTIyZ3JlZXRpbmclMjIlM0FudWxsJTdEJTJDJTIyb2ZmbGluZUZvcm0lMjIlM0ElN0IlMjJncmVldGluZyUyMiUzQW51bGwlN0QlMkMlMjJjb25jaWVyZ2UlMjIlM0ElN0IlMjJhdmF0YXJQYXRoJTIyJTNBbnVsbCUyQyUyMm5hbWUlMjIlM0FudWxsJTJDJTIydGl0bGUlMjIlM0FudWxsJTdEJTdEJTJDJTIyY29sb3IlMjIlM0ElN0IlMjJhcnRpY2xlTGlua3MlMjIlM0ElMjIlMjIlMkMlMjJidXR0b24lMjIlM0ElMjIlMjIlMkMlMjJoZWFkZXIlMjIlM0ElMjIlMjIlMkMlMjJsYXVuY2hlciUyMiUzQSUyMiUyMiUyQyUyMmxhdW5jaGVyVGV4dCUyMiUzQSUyMiUyMiUyQyUyMnJlc3VsdExpc3RzJTIyJTNBJTIyJTIyJTJDJTIydGhlbWUlMjIlM0FudWxsJTdEJTdEJTdE&&locale=en-us&title=Web%20Widget%20Live%20Chat"

WELCOME_TEXT = """FIFA777 OFFICIAL

Selamat datang di layanan resmi Fifa777

Transaksi deposit QRIS proses hanya 1 detik
Penarikan berapapun dibayar tuntas tanpa ribet

Kami hadir dengan sistem cepat, stabil & pelayanan terbaik untuk
Anda."""


def menu_buttons():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Akses Layanan", url=AKSES_LAYANAN),
        InlineKeyboardButton("Live Support", url=LIVE_SUPPORT),
    )
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=menu_buttons(),
        disable_web_page_preview=True,
    )


@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=menu_buttons(),
        disable_web_page_preview=True,
    )


if __name__ == "__main__":
    logging.info("Bot Fifa777 berjalan...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)
