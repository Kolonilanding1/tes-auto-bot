from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import logging
import asyncio
import pytz
from datetime import datetime



auto_task = None

API_TOKEN = '8110875332:AAG33TTd_CnmC_eFi58VhbNCSHL8A_EwfXA'
GROUP_USERNAME = '@InfoFreebet4D','@SITUSLINKGACOR4D'
CHANNEL_USERNAME = '@koloni4d_official1'
TARGET_CHAT_ID = -1002658447462  # Ganti ini ke chat ID grup/channel tujuan untuk auto-text

# Logger
logging.basicConfig(level=logging.INFO)

# Daftar pesan dan gambar
messages = [
    {
       "text": """<b>🔥🔥SLOT GACOR HARI INI🔥🔥</b>

🔥 Mau link slot gacor update tiap hari?  
🔥 RTP real time, info bocoran jam gacor langsung masuk grup!  

Gabung sekarang sebelum penuh:  
👉 https://heylink.me/LinkAlternatifKoloni4D/

Siapa cepat dia dapat! 🚀
🎲 <b>Rekomendasi Situs Gacor Terpercaya Hari Ini!</b>
💎 Jangan lewatkan info jackpot eksklusif hanya di @Situslinktergacor_Bot 
🔥 Update real-time & tips gacor setiap hari!  
🎯 Yuk, buktikan keberuntunganmu sekarang juga!""",
        "image": "https://i.postimg.cc/qvXqnkfv/KOLONI4-D-42.png"
    },
    {
        "text": """<b>🔥🔥BUKTI KEMENANGAN🔥🔥</b>

⚡️ 90% Member Sudah WD Hari Ini!  
Mau tau link gacor + bocoran jam hoki?

Buruan join! (FREE, No bayar!)  
👉 https://heylink.me/LinkAlternatifKoloni4D/

[Auto JP kalau paham timingnya 😎]
🎲 <b>Rekomendasi Situs Gacor Terpercaya Hari Ini!</b>
💎 Jangan lewatkan info jackpot eksklusif hanya di @Situslinktergacor_Bot  
🔥 Update real-time & tips gacor setiap hari!  
🎯 Yuk, buktikan keberuntunganmu sekarang juga!""",
        "image": "https://i.postimg.cc/nVC2nhg7/BTG-6.png"
    }, 
    {
        "text": """<b>🔥🔥BONUS DAN EVENT TERBARU🔥🔥</b>

🎁 Event Spesial Member Baru 🎁  
Join grup Telegram kita hari ini dan dapatkan bocoran link slot RTP 98%++!

🎰 Bonus rahasia buat 50 member pertama!

Gas join di sini:  
👉 https://heylink.me/LinkAlternatifKoloni4D/

Main makin hoki bareng komunitas! 🎯
🎲 <b>Rekomendasi Situs Gacor Terpercaya Hari Ini!</b>
💎 Jangan lewatkan info jackpot eksklusif hanya di @Situslinktergacor_Bot  
🔥 Update real-time & tips gacor setiap hari!  
🎯 Yuk, buktikan keberuntunganmu sekarang juga!""",
        "image": "https://i.postimg.cc/1zm02mD8/BATAGOR-1.png"
    },
    {
        "text": """<b>🔥🔥KONTEN EKSCLUSIVE🔥🔥</b>

🔥 Link Bokep + Link Slot Gacor Komplit Disini 🔥

✅ Update Link Bokep Setiap Hari  
✅ Slot Gacor + RTP Real Time  
✅ Member Aktif, Seru, Tanpa Hoax

Buruan masuk grup:  
👉 @Idaman_warga62_bot
👉 https://heylink.me/LinkAlternatifKoloni4D/

Satu tempat buat semua hiburan! 😈
🎲 <b>Rekomendasi Situs Gacor Terpercaya Hari Ini!</b>
💎 Jangan lewatkan info jackpot eksklusif hanya di @Situslinktergacor_Bot
🔥 Update real-time & tips gacor setiap hari!  
🎯 Yuk, buktikan keberuntunganmu sekarang juga!""",
        "image": "https://i.postimg.cc/nL3Kty10/image.png"
    }
]

# Fungsi /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎁 Klaim Freebet", callback_data='claim_freebet'),
            InlineKeyboardButton("📺 Konten Gratis", callback_data='konten_gratis'),
        ],
        [
            InlineKeyboardButton("🔒 Konten VIP", callback_data='konten_vip'),
        ],
        [
            InlineKeyboardButton("🔗 Link Gacor", url="https://heylink.me/LinkAlternatifKoloni4D/"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "<b>Selamat datang!</b>\n\n"
        "Silakan pilih menu di bawah ini untuk akses cepat:",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

# Fungsi untuk mengirim ulang pesan jika verifikasi gagal
async def send_welcome_message(query, context):
    keyboard = [
        [ InlineKeyboardButton("🎁 Klaim Freebet", callback_data='claim_freebet'),
        InlineKeyboardButton("📺 Konten Gratis", callback_data='konten_gratis'), ],
        [ InlineKeyboardButton("🔒 Konten VIP", callback_data='konten_vip'),],
        [ InlineKeyboardButton("🔒 Link Gacor", url="https://heylink.me/LinkAlternatifKoloni4D/"),],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text="👋 Silakan pilih salah satu menu berikut:",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

# Fungsi untuk menangani tombol yang dipilih
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'claim_freebet':
        text = (
            "<b>🎁 KLAIM FREEBET HARI INI!</b>\n\n"
            "Buruan klaim freebet khusus untuk member baru!\n"
            "✅ Tanpa deposit\n"
            "✅ Proses cepat\n"
            "✅ Langsung main slot gacor\n\n"
            "Gabung & klaim sekarang!\n\n"
            "👉 <a href='https://t.me/InfoFreebet4D'>Grup Freebet</a>\n"
            "👉 <a href='https://t.me/SITUSLINKGACOR4D'>Grup Siuts Link Gacor</a>\n"
            "👉 <a href='https://t.me/koloni4d_official1'>Channel Official</a>\n\n" 
            "Klik 'Lanjut' setelah bergabung di grup dan channel untuk klaim."
        )
        keyboard = [
            [InlineKeyboardButton("Grup Freebet", url='https://t.me/InfoFreebet4D')],
            [InlineKeyboardButton("Grup Situs Link Gacor", url='https://t.me/SITUSLINKGACOR4D')],
            [InlineKeyboardButton("Channel Official", url='https://t.me/koloni4d_official1')],
            [InlineKeyboardButton("Lanjut", callback_data='verify_claim_freebet')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)

    elif query.data == 'konten_gratis':
        text = (
            "<b>📺 KONTEN GRATIS UNTUK KAMU!</b>\n\n"
            "📺 Konten Gratis update 1x dalam hari\n"
            "🧠 vidio gratis update setiap hari\n\n"
            "Gabung GRATIS sekarang dan selamat menikmati!\n\n"
            "👉 <a href='https://t.me/InfoFreebet4D'>Grup Freebet</a>\n"
            "👉 <a href='https://t.me/SITUSLINKGACOR4D'>Grup Siuts Link Gacor</a>\n"
            "👉 <a href='https://t.me/koloni4d_official1'>Channel Official</a>\n\n" 
            "Klik 'Lanjut' setelah bergabung di grup dan channel untuk akses."
        )
        keyboard = [
            [InlineKeyboardButton("Grup Freebet", url='https://t.me/InfoFreebet4D')],
            [InlineKeyboardButton("Grup Situs Link Gacor", url='https://t.me/SITUSLINKGACOR4D')],
            [InlineKeyboardButton("Channel Official", url='https://t.me/koloni4d_official1')],
            [InlineKeyboardButton("Lanjut", callback_data='verify_konten_gratis')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)
        
    elif query.data == 'konten_vip':
        text = (
            "<b>🔒 KONTEN VIP EKSKLUSIF</b>\n\n"
            "🔥 Dapatkan akses ke:\n"
            "⭐️ Link slot RTP 98%++\n"
            "⭐️ Prediksi bocoran admin dalam\n"
            "⭐️ Bonus khusus dan trick anti zonk!\n\n"
            "⭐️ Vidio VIP tidak terbatas !!\n\n"
            "Mau gabung VIP? Hubungi admin:\n\n"
            "Gabung & Nikmati sekarang!\n\n"

            "👉 <a href='https://t.me/InfoFreebet4D'>Grup Freebet</a>\n"
            "👉 <a href='https://t.me/SITUSLINKGACOR4D'>Grup Siuts Link Gacor</a>\n"
            "👉 <a href='https://t.me/koloni4d_official1'>Channel Official</a>\n\n" 

            "Klik 'Lanjut' setelah bergabung di grup dan channel untuk VIP access."
        )
        keyboard = [
            [InlineKeyboardButton("Grup Freebet", url='https://t.me/InfoFreebet4D'),],
            [InlineKeyboardButton("Grup Situs Link Gacor", url='https://t.me/SITUSLINKGACOR4D')],
            [InlineKeyboardButton("Channel Official", url='https://t.me/koloni4d_official1'),],
            [InlineKeyboardButton("Lanjut", callback_data='verify_konten_vip')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=reply_markup)

    else:
        text = "❓ Pilihan tidak dikenal."
        await query.edit_message_text(text=text, parse_mode='HTML')

async def verify_membership(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    callback_data = query.data  # Ambil data dari callback

    try:
        # Verifikasi jika pengguna sudah gabung grup dan channel
        group_status = await context.bot.get_chat_member('@InfoFreebet4D', user_id)
        group_status = await context.bot.get_chat_member('@SITUSLINKGACOR4D', user_id)
        channel_status = await context.bot.get_chat_member('@koloni4d_official1', user_id)

        logging.info(f"Group status: {group_status.status}")  # Status pengguna di grup
        logging.info(f"Channel status: {channel_status.status}")  # Status pengguna di channel
        if group_status.status not in ['member', 'administrator', 'creator']:
            logging.warning(f"User {user_id} is not a member of the group! Status: {group_status.status}")
        if channel_status.status not in ['member', 'administrator', 'creator']:
            logging.warning(f"User {user_id} is not a member of the channel! Status: {channel_status.status}")

        # Cek apakah verifikasi berhasil
        if group_status.status in ['member', 'administrator', 'creator'] and channel_status.status in ['member', 'administrator', 'creator']:
            # Pesan jika berhasil
            if callback_data == 'verify_claim_freebet':
                context.user_data['last_action'] = 'claim_freebet'
                text = (
                    "<b>🎁 KLAIM FREEBET HARI INI!</b>\n\n"
                    "✅ Anda sudah bergabung di grup dan channel!\n"
                    "🎉 Klaim freebet Anda segera dengan daftar link di bawah ini:\n"
                    "Link Situs\n"
                    "👉 https://koloni2025.com/\n\n"
                    "⚠️ <b>PERINGATAN!!</b>\n"
                    "Pastikan Anda mendaftarkan nomor rekening bank atau e-wallet yang benar. Jika Anda melakukan penarikan (WD) dan nomor rekening/e-wallet yang terdaftar tidak valid, maka TIDAK DAPAT DIBANTU untuk diganti atau diperbaiki.  Kesalahan dalam pengisian data sepenuhnya menjadi tanggung jawab pengguna.\n\n"

                    "⚠️ <b>Hanya Bisa Claim Freebet Akun Baru !!</b>"
                )
            elif callback_data == 'verify_konten_gratis':
                context.user_data['last_action'] = 'konten_gratis'
                text = (
                    "<b>📺 KONTEN GRATIS UNTUK KAMU!</b>\n\n"
                    "✅ Anda sudah bergabung di grup dan channel!\n"
                    "🎉 Akses konten gratis tersedia di bawah:\n\n"
                    "Selamat Menikmati !! \n"
                )
            elif callback_data == 'verify_konten_vip':
                context.user_data['last_action'] = 'konten_vip'
                text = (
                  "<b>🔒 KONTEN VIP EKSKLUSIF</b>\n\n"
                  "🎉 Kini Anda dapat mengakses berbagai konten spesial hanya untuk member VIP:\n\n"
                  "🎉 Akses VIP eksklusif tersedia di bawah:\n\n"
                  "📦 <b>Daftar Konten VIP:</b>\n\n"
                  "🎥 <b>Video Reguler</b>\n"
                  "💰 Rp20.000\n"
                  "🕐 Akses: 1 - 5 Hari\n\n"
                  "🎞️ <b>Video VIP</b>\n"
                  "💰 Rp50.000\n"
                  "♾️ Akses: Permanen\n\n"
                  "📸 <b>Foto Hot</b>\n"
                  "💥 <b>GRATIS!</b>\n"
                  "🆓 Cukup gabung grup, tanpa bayar — langsung bisa lihat koleksi foto-foto hot eksklusif!\n\n"
                  "📩 Tertarik akses konten premium lainnya?\n"
                  "Hubungi admin sekarang:\n"
                  "👉 <a href='https://t.me/Koloni_4d'>@Koloni_4d</a>"
                )
            else:
                text = "✅ Anda telah diverifikasi!"

            # Tambah tombol "Klik untuk Lanjut"
            lanjut_button = InlineKeyboardMarkup([[ 
                InlineKeyboardButton("🔓 Klik untuk Lanjut", callback_data="thank_you_after_verify")
            ]])

            await query.edit_message_text(text=text, parse_mode='HTML', reply_markup=lanjut_button)

        else:
            # Jika gagal
            await query.answer("❗ Anda belum bergabung di grup dan channel!", show_alert=True)
            await send_welcome_message(query, context)

    except Exception as e:
        logging.error(f"Error occurred while verifying membership for user {user_id}: {e}")
        await query.answer("⚠️ WAJIB JOIN KEDUA GRUP & CHANNEL.", show_alert=True)
        await send_welcome_message(query, context)
        logging.error(f"Error occurred while verifying membership for user {user_id}: {e}")
        await query.answer("⚠️ Terjadi kesalahan saat verifikasi.", show_alert=True)
        await send_welcome_message(query, context)

    # Fungsi untuk menampilkan pesan terima kasih setelah verifikasi berhasil
async def thank_you_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Mendapatkan nilai 'last_action' dari context
    last_action = context.user_data.get('last_action', '')

    # Debugging untuk memastikan nilai last_action
    print(f"Last action value: {last_action}")

    if last_action == 'claim_freebet':
        text = ( "🎁 Terima kasih! Untuk klaim FREEBET, kirim user ID lalu konfirmasi ke WA\n\n"
        "Link Wa Official\n 👉 https://shortlyq.link/wa-koloni4d\n\n"
        "💬 <b>PERHATIAN:</b>\n"
        "Bagi member FREEBET yang melakukan penarikan (WD), WAJIB konfirmasi ke WA OFFICIAL agar proses lancar dan tidak tertunda.\n\n"
        "<b>🎊 Selamat Bermain & semoga hoki terus ya!</b>"
)
        print(text)

        await query.edit_message_text(text=text, parse_mode='HTML')

    elif last_action == 'konten_gratis':
        group_link = "https://dm.fandome.co/feed?wid=88ESU7NX"  
        text = "📚 Terima kasih! Klik tombol di bawah ini untuk masuk ke grup konten GRATIS:"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("📥 Masuk Grup Gratis", url=group_link)]])
        await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode='HTML')

    elif last_action == 'konten_vip':
        group_link = "https://dm.fandome.co/feed?wid=88ESU7NX"  # Ganti dengan link grup VIP
        text = "💎 Terima kasih! Klik tombol di bawah ini untuk masuk ke grup VIP:"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("💎 Masuk Grup VIP", url=group_link)]])
        await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode='HTML')

    else:
        print("Last action tidak cocok dengan kondisi!")
        await query.edit_message_text(text="✅ Terima kasih telah mengikuti langkah-langkah!", parse_mode='HTML')


async def auto_send_messages(app: Application):
    index = 0
    duration = 24 * 60 * 60  # 24 jam
    start_time = asyncio.get_event_loop().time()

    while True:
        current_time = asyncio.get_event_loop().time()
        if current_time - start_time > duration:
            logging.info("⏱️ 24 jam selesai. Stop kirim otomatis.")
            break

        try:
            if not messages:
                logging.warning("🚫 List messages kosong.")
                await asyncio.sleep(60)
                continue

            message_data = messages[index]
            image = message_data.get("image")
            text = message_data.get("text", "")

            if not image:
                logging.warning(f"⚠️ Gambar kosong di index {index}. Lewati.")
                index = (index + 1) % len(messages)
                await asyncio.sleep(10)
                continue

            await app.bot.send_photo(
                chat_id=TARGET_CHAT_ID,
                photo=image,
                caption=text,
                parse_mode='HTML'
            )

            logging.info(f"✅ Pesan ke-{index + 1} terkirim.")
            index = (index + 1) % len(messages)
            await asyncio.sleep(3600)  # 2 jam (ubah jadi 10 saat testing)

        except Exception as e:
            logging.error(f"❌ Gagal kirim pesan otomatis (index {index}): {e}")
            await asyncio.sleep(30)


# Menambahkan handler untuk callback yang sesuai
from telegram.ext import Application

async def on_startup(app: Application):
    global auto_task
    if auto_task is None or auto_task.done():
        auto_task = asyncio.create_task(auto_send_messages(app))
        logging.info("🚀 Auto-send dimulai saat startup.")
    
# Jalankan bot
if __name__ == '__main__':
    app = Applicationbuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button, pattern="^(claim_freebet|konten_gratis|konten_vip)$"))
    app.add_handler(CallbackQueryHandler(verify_membership, pattern="^verify_"))
    app.add_handler(CallbackQueryHandler(thank_you_message, pattern="^thank_you_after_verify$"))

    app.post_init = on_startup
    app.run_polling()
