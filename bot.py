import subprocess
import pytz
from datetime import datetime, timedelta
from datetime import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, JobQueue
import asyncio

# Fungsi untuk mengeksekusi file enhanced_last24hourcase.py
async def execute_script_1(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'enhanced_last24hourcase.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Case dalam 24 Jam Terakhir yang belum di handle: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 1: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 1: {e}")

# Fungsi untuk mengeksekusi file sensordetails1.py
async def execute_script_2(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails1.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 1: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 2: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 2: {e}")

# Fungsi untuk mengeksekusi file sensordetails2.py
async def execute_script_3(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails2.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 2: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 3: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 3: {e}")

# Fungsi untuk mengeksekusi file sensordetails3.py
async def execute_script_4(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails3.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 3: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 4: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 4: {e}")

# Fungsi untuk mengeksekusi file sensordetails4.py
async def execute_script_5(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails4.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 4: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 5: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 5: {e}")

# Fungsi untuk mengeksekusi file sensordetails5.py
async def execute_script_6(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails5.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 5: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 6: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 6: {e}")

# Fungsi untuk mengeksekusi file sensordetails6.py
async def execute_script_7(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails6.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 6: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 7: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 7: {e}")

# Fungsi untuk mengeksekusi file sensordetails7.py
async def execute_script_8(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails7.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 7: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 8: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 8: {e}")

# Fungsi untuk mengeksekusi file sensordetails8.py
async def execute_script_9(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails8.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 8: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 9: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 9: {e}")

# Fungsi untuk mengeksekusi file sensordetails9.py
async def execute_script_10(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'sensordetails9.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Detail Sensor 9: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 10: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 10: {e}")
            
# Fungsi untuk mengeksekusi file NotYetHandledCases.py
async def execute_script_11(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'NotYetHandledCases.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut All Time Cases yang belum di handle  \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 11: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 11: {e}")
            
            
# Fungsi untuk mengeksekusi file LastResolvedCase.py
async def execute_script_12(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'LastResolvedCase.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Cases terakhir dengan status Resolved: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 12: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 12: {e}")
            
            
# Fungsi untuk mengeksekusi file LastCancelledCase.py
async def execute_script_13(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'LastCancelledCase.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Cases terakhir dengan status Cancelled: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 13: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 13: {e}")
            
            
# Fungsi untuk mengeksekusi file LastEscalatedCase.py
async def execute_script_14(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'LastEscalatedCase.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Cases terakhir dengan status Escalated: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 14: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 14: {e}")
            
            
# Fungsi untuk mengeksekusi file LastInProgressCase.py
async def execute_script_15(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'LastInProgressCase.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Berikut Cases terakhir dengan status In Progress: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 15: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 15: {e}")
            
            
# Fungsi untuk mengeksekusi file dataingestion.py
async def execute_script_16(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'dataingestion.py'],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Data API berhasil di retrieve: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 16: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 16: {e}")
            
            
# Fungsi untuk mengeksekusi dataingestion.py secara otomatis
async def scheduled_job(context):
    try:
        result = subprocess.run(
            ['python3', 'dataingestion.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            # Mengirimkan hasil output ke grup atau channel Telegram jika diinginkan
            await context.bot.send_message(chat_id='<your chat ID>', text=f"Data API berhasil di retrieve: \n{result.stdout}")
        else:
            await context.bot.send_message(chat_id='<your chat ID>', text=f"Terjadi kesalahan saat eksekusi script 16: \n{result.stderr}")
    except Exception as e:
        await context.bot.send_message(chat_id='<your chat ID>', text=f"Error saat mengeksekusi script 16: {e}")
            
            
# Fungsi untuk mengeksekusi file lastcve.py
async def execute_script_17(update: Update, context):
    vendor = context.args[0] if len(context.args) > 0 else None  # Mendapatkan vendor dari argumen perintah
    product = context.args[1] if len(context.args) > 1 else None  # Mendapatkan produk dari argumen perintah

    try:
        # Menyusun perintah untuk mengeksekusi lastcve.py dengan parameter vendor dan produk
        command = ['python3', 'lastcve.py']
        
        if vendor:
            command.append(vendor)  # Menambahkan vendor ke dalam perintah
        if product:
            command.append(product)  # Menambahkan produk ke dalam perintah jika ada
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=100
        )
        
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Data API berhasil di retrieve: \n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script: {e}")
            
# Fungsi untuk mengeksekusi file CVEdetails.py dengan filter cveID
async def execute_script_18(update: Update, context):
    # Mengecek apakah ada argumen yang diberikan oleh pengguna (cveID)
    if len(context.args) == 0:
        # Memberikan respon jika tidak ada cveID yang diberikan
        await update.message.reply_text("Silakan masukkan cveID setelah perintah. Contoh: /CVEdetails CVE-2024-43522")
        return

    # Mengambil cveID yang diberikan oleh pengguna
    cve_id = context.args[0]
    
    try:
        # Menyusun perintah untuk mengeksekusi CVE.py dengan parameter cveID
        result = subprocess.run(
            ['python3', 'CVEdetails.py', cve_id],  # Menambahkan cveID sebagai argumen
            capture_output=True,
            text=True,
            timeout=30  # Menetapkan timeout untuk eksekusi
        )

        if result.returncode == 0:
            # Jika perintah berhasil, mengirimkan hasilnya ke pengguna
            if update.message:
                await update.message.reply_text(f"Berikut adalah detail CVE {cve_id}:\n{result.stdout}")
        else:
            # Jika ada error dalam eksekusi, menampilkan error
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi CVE script: \n{result.stderr}")
    except Exception as e:
        # Menangani kesalahan jika ada error lain
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script CVE: {e}")
            
# Fungsi untuk mengeksekusi file listvendor.py
async def execute_script_19(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'listvendor.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 19: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 19: {e}")
            
# Fungsi untuk mengeksekusi file connector.py
async def execute_script_20(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'connector.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Data API berhasil di retrieve: {result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 20: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 20: {e}")
            
# Fungsi untuk mengeksekusi file IngestionDetail.py
async def execute_script_21(update: Update, context):
    try:
        result = subprocess.run(
            ['python3', 'IngestionDetail.py'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Data API berhasil di retrieve: \n {result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 21: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 21: {e}")
            
# Fungsi untuk mengeksekusi file virustotal.py dengan IP yang dikirimkan oleh pengguna
async def execute_script_22(update: Update, context):
    try:
        # Mengambil alamat IP yang dikirim oleh pengguna
        ip_address = context.args[0]  # Mengambil argumen pertama dari perintah /VirusTotal <ip_address>
        
        # Menjalankan analisis VirusTotal dengan IP tersebut
        result = subprocess.run(
            ['python3', 'virustotal.py', ip_address],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            if update.message:
                await update.message.reply_text(f"Data API berhasil di retrieve \n {result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat eksekusi script 22: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi script 22: {e}")

# Fungsi untuk mengeksekusi file pullalert.py            
async def execute_script_23(update: Update, context):
    try:
        # Mengambil status yang dikirim oleh pengguna
        if len(context.args) < 1:
            await update.message.reply_text("Harap masukkan status yang ingin dicari (contoh: New, Closed).")
            return
        
        status = context.args[0]  # Status yang diberikan oleh pengguna
        
        # Menjalankan pullalert.py dengan status yang diberikan
        result = subprocess.run(
            ['python3', 'pullalert.py', status],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            if update.message:
                # Mengirimkan hasil output dari pullalert.py
                await update.message.reply_text(f"Berikut Alert dengan Status '{status}' hari ini:\n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat mengeksekusi pullalert.py: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi pullalert.py: {e}")
            

# Fungsi untuk mengeksekusi file slacalculation.py            
async def execute_script_24(update: Update, context):
    try:
        # Memastikan pengguna memberikan argumen (filter waktu)
        if len(context.args) < 1:
            await update.message.reply_text("Masukkan filter waktu cuy (contoh: Today, Yesterday, Weekly, Monthly).")
            return
        
        time_filter = context.args[0].capitalize()  # Mengambil filter waktu dan mengubah ke format yang benar
        
        # Menjalankan slacalculation.py dengan filter waktu yang diberikan
        result = subprocess.run(
            ['python3', 'slacalculation.py', time_filter],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            # Mengirimkan hasil output dari slacalculation.py
            await update.message.reply_text(f"{result.stdout}")
        else:
            await update.message.reply_text(f"Terjadi kesalahan saat eksekusi slacalculation.py: \n{result.stderr}")
    except Exception as e:
        await update.message.reply_text(f"Error saat mengeksekusi slacalculation.py: {e}")
        

# Fungsi untuk mengeksekusi file pullalertshift.py        
async def execute_script_25(update: Update, context):
    try:
        # Memastikan pengguna memberikan dua argumen (status dan shift)
        if len(context.args) < 2:
            await update.message.reply_text("Harap masukkan status dan shift (contoh: /Alert New Shift1).")
            return
        
        status = context.args[0]  # Status yang diberikan oleh pengguna
        shift = context.args[1].lower()  # Shift yang diberikan oleh pengguna (Shift1, Shift2, Shift3)

        if shift not in ['shift1', 'shift2', 'shift3']:
            await update.message.reply_text("Shift tidak valid. Gunakan Shift1, Shift2, atau Shift3.")
            return
        
        # Menjalankan pullalert.py dengan status dan shift yang diberikan
        result = subprocess.run(
            ['python3', 'pullalertshift.py', status, shift],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            if update.message:
                # Mengirimkan hasil output dari pullalert.py
                await update.message.reply_text(f"Berikut Alert dengan Status '{status}' pada {shift} :\n{result.stdout}")
        else:
            if update.message:
                await update.message.reply_text(f"Terjadi kesalahan saat mengeksekusi pullalertshiftt.py: \n{result.stderr}")
    except Exception as e:
        if update.message:
            await update.message.reply_text(f"Error saat mengeksekusi pullalertshift.py: {e}")

# Fungsi untuk menyapa pengguna dengan perintah /start
async def start(update: Update, context):
    if update.message:
        await update.message.reply_text(
            "Halo \U0001F60A! Saya adalah Punggawa Bot yang terintegrasi dengan Stellar Cyber \n Gunakan perintah:\n"
            "- /start untuk menampilkan pesan ini\n"
            "- /last24case untuk mendapatkan New Case dalam kurun waktu 24 jam\n"
            "- /detailsensors1 sampai /detailsensors9 untuk mendapatkan data sensor 1 hingga 9 dan statusnya\n"
            "- /NotYetHandledCases untuk mendapatkan cases yang belum di Handle, di resolved atau di cancel dan statusnya \n"
            "- /LastResolvedCases untuk mendapatkan data Case terakhir dengan status 'Resolved' maksimal 5 case \n"
            "- /LastCancelledCases untuk mendapatkan data Case terakhir dengan status 'Cancelled' maksimal 5 case \n"
            "- /LastEscalatedCases untuk mendapatkan data Case terakhir dengan status 'Escalated' maksimal 5 case \n"
            "- /LastInProgressCases untuk mendapatkan data Case terakhir dengan status 'In Progress' maksimal 5 case \n"
            "- /SLAcalculation <spasi> Filter waktu bisa today, yesterday, weekly dan monthly \n"
            "- /Alert <Status (New, CLosed dll)> <shift (shift1, shift2 dan shift3) menampilkan jumlah Alert per shift berdasarkan status \n"
            "- /DataIngestion untuk mendapatkan data ingestion 5 hari terakhir \n"
            "- /Connector untuk mendapatkan detail connector yang terhubung dengan Stellar Cyber \n"
            "- /IngestionDetail untuk mendapatkan detail Data Ingestion dari masing2 log source \n"
            "- /MoodBooster untuk itu iya itu tau ga lu jan iya iya aja"
        )
        
# Fungsi untuk menambahkan job otomatis pada JobQueue
async def job_callback(context):
    context.job_queue.run_daily(scheduled_job, time=datetime.time(11, 0, 0), days=(0, 1, 2, 3, 4, 5, 6), context=context)
        
# Fungsi untuk moodbooster /MoodBooster
async def moodbooster(update: Update, context):
    if update.message:
        await update.message.reply_text(
            "Semangat kerjanya kakak, jangan lupa makan \U0001F60A \n"
            "Ikan sepat ikan tongkol"
        )

if __name__ == '__main__':
    TOKEN = '<Your Telegram Bot Token>'

    # Membuat aplikasi bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Menambahkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))
    
    # Menambahkan handler untuk perintah /MoodBooster
    application.add_handler(CommandHandler("MoodBooster", moodbooster))

    # Menambahkan handler untuk perintah eksekusi script
    application.add_handler(CommandHandler("last24case", execute_script_1))
    application.add_handler(CommandHandler("detailsensors1", execute_script_2))
    application.add_handler(CommandHandler("detailsensors2", execute_script_3))
    application.add_handler(CommandHandler("detailsensors3", execute_script_4))
    application.add_handler(CommandHandler("detailsensors4", execute_script_5))
    application.add_handler(CommandHandler("detailsensors5", execute_script_6))
    application.add_handler(CommandHandler("detailsensors6", execute_script_7))
    application.add_handler(CommandHandler("detailsensors7", execute_script_8))
    application.add_handler(CommandHandler("detailsensors8", execute_script_9))
    application.add_handler(CommandHandler("detailsensors9", execute_script_10))
    application.add_handler(CommandHandler("NotYetHandledCases", execute_script_11))
    application.add_handler(CommandHandler("LastResolvedCases", execute_script_12))
    application.add_handler(CommandHandler("LastCancelledCases", execute_script_13))
    application.add_handler(CommandHandler("LastEscalatedCases", execute_script_14))
    application.add_handler(CommandHandler("LastInProgressCases", execute_script_15))
    application.add_handler(CommandHandler("DataIngestion", execute_script_16))
    application.add_handler(CommandHandler("Connector", execute_script_20))
    application.add_handler(CommandHandler("IngestionDetail", execute_script_21))
    application.add_handler(CommandHandler("Alert", execute_script_25))
    application.add_handler(CommandHandler("AlertDaily", execute_script_23))
    application.add_handler(CommandHandler("SLAcalculation", execute_script_24))
    
    # Menambahkan JobQueue untuk eksekusi otomatis setiap jam 11.00 AM UTC+7
    job_queue = application.job_queue
    job_queue.run_daily(scheduled_job, time=time(4, 0), days=(0, 1, 2, 3, 4, 5, 6))  # 15:30 UTC+7 = 08:30 UTC

    # Menjalankan bot
    application.run_polling()
