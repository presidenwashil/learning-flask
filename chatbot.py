import sqlite3
import datetime
from flask import url_for

def get_response(message):
    message = message.lower().strip()

    responses = []

    if "halo" in message:
        responses.append("Halo juga!")
    elif "selamat" in message:
        now = datetime.datetime.now()
        if now.hour < 12:
            responses.append("Selamat pagi!")
        elif now.hour < 18:
            responses.append("Selamat siang!")
        else:
            responses.append("Selamat malam!")

    elif "cara daftar" in message or "mendaftar" in message:
        responses.append("Cara mendaftar adalah dengan kunjungi <a href='https://pmb.wicida.ac.id'>https://pmb.wicida.ac.id</a> dan klik menu daftar, lalu lengkapi terlebih dahulu form yang tersedia untuk mendaftar menjadi mahasiswa baru di kampus STMIK Widya Cipta Dharma")

    elif "prosedur" in message:
        responses.append('Alur Pendaftaran Mahasiswa Baru di STMIK Widya Cipta Dharma Terdiri dari 3 Jalur, yaitu Jalur Reguler, Alih Jenjang dan PMDK')

    elif "reguler" in message:
        responses.append("Untuk persyaratan jalur reguler silahkan cek di <a href='https://pmb.wicida.ac.id/persyaratan-pendaftaran'>https://pmb.wicida.ac.id/persyaratan-pendaftaran</a> dan berikut adalah alur pendaftaran jalur reguler:")
        responses.append(f'<img src="{url_for("static", filename="reguler.png")}" alt="reguler">')

    elif "alih jenjang" in message:
        responses.append("Untuk persyaratan jalur alih jenjang silahkan cek di <a href='https://pmb.wicida.ac.id/persyaratan-pendaftaran'>https://pmb.wicida.ac.id/persyaratan-pendaftaran</a> dan berikut adalah alur pendaftaran jalur alih jenjang:")
        responses.append(f'<img src="{url_for("static", filename="alih_jenjang.png")}" alt="alih_jenjang">')

    elif "pmdk" in message:
        responses.append("Untuk persyaratan jalur PMDK silahkan cek di <a href='https://pmb.wicida.ac.id/persyaratan-pmdk'>https://pmb.wicida.ac.id/persyaratan-pmdk</a> dan berikut adalah alur pendaftaran jalur PMDK:")
        responses.append(f'<img src="{url_for("static", filename="pmdk.png")}" alt="pmdk">')

    elif "biaya pendaftaran" in message or "pendaftaran" in message:
        responses.append("Biaya pendaftaran di STMIK Widya Cipta Dharma hanya sebesar Rp. 50.000")

    elif "biaya daftar ulang" in message or "daftar ulang" in message:
        responses.append('Berikut adalah rincian biaya Daftar Ulang')
        responses.append(f'<img src="{url_for("static", filename="daftar_ulang.png")}" alt="daftar_ulang">')

    elif "cara bayar" in message or "membayar" in message or "pembayaran" in message:
        responses.append("Bank BNI dengan No Rekening : 1656788995 atas Nama : Panitia Penerimaan Mahasiswa Baru STMIK Widya Cipta Dharma")
        responses.append("GoPay / Ovo : 0822 35232 394 Atas Nama Ibu Reny Handini, SE")
        responses.append("Jangan Lupa untuk Lakukan Validasi setelah melakukan Pembayaran! silahkan klik <a href='https://wa.me/082155034678'>https://wa.me/082155034678</a>")

    elif "validasi" in message or "validasi pembayaran" in message:
        responses.append("Silahkan klik link ini untuk melakukan validasi pembayaran <a href='https://wa.me/082155034678'>https://wa.me/082155034678</a>")

    elif "akreditas" in message:
        if "kampus" in message or "stmik" in message or "wicida" in message:
            responses.append("STMIK Widya Cipta Dharma terakreditasi B Berdasarkan Keputusan BAN-PT No. 348/SK/BAN-PT/Ak-PPJ/PT/VI/2020 yang berlaku sejak tanggal 13 Juni 2020 sampai dengan 13 Juni 2025")
        elif "sistem informasi" in message or "si" in message:
            responses.append("Akreditasi Sistem Informasi adalah B")
        elif "teknik informatika" in message or "ti" in message:
            responses.append("Akreditasi Teknik Informatika adalah B")
        elif "bisnis digital" in message or "bd" in message:
            responses.append("Akreditasi Bisnis Digital adalah C")

    elif "prodi" in message or "program studi" in message or "jurusan" in message:
        responses.append("Di STMIK Wicida terdapat 3 Program Studi yaitu : Teknik Informatika, Sistem Informasi, dan Bisnis Digital")

    elif "lokasi" in message or "lokasi kampus" in message:
        responses.append("Jl. M. Yamin, Gn. Kelua, Kec. Samarinda Ulu, Kota Samarinda, Kalimantan Timur 75123  <a href='https://maps.app.goo.gl/wNXHeuVZ5dfnJ4Kb7'>https://maps.app.goo.gl/wNXHeuVZ5dfnJ4Kb7</a>")

    elif "kontak" in message or "narahubung" in message:
        responses.append("Silahkan klik link ini untuk menghubungi narahubung melalu whatsapp <a href='https://wa.me/082155034678'>https://wa.me/082155034678</a>")

    elif "kelas" in message or "kelas yang tersedia" in message:
        responses.append("Tersedia kelas Pagi dan kelas Malam")

    elif "fasilitas" in message or "prasarana" in message:
        responses.append("Tersedia perpustakaan yang lengkap, Ruang kelas yang nyaman dan tersedia 5 Laboratorium komputer")

    else:
        responses.append("Maaf saya tidak mengerti, mohon lebih perjelas lagi pertanyannya ya!")
        
    return responses


def save_message(user_id, user_message, bot_responses):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()

    for bot_response in bot_responses:
        cursor.execute('''
            INSERT INTO chat_history (user_id, user_message, bot_response)
            VALUES (?, ?, ?)
        ''', (user_id, user_message, bot_response))

    conn.commit()
    conn.close()

def get_or_create_user(name, phone):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE name = ? AND phone = ?', (name, phone))
    user = cursor.fetchone()

    if user:
        user_id = user[0]
    else:
        cursor.execute('INSERT INTO users (name, phone) VALUES (?, ?)', (name, phone))
        conn.commit()
        user_id = cursor.lastrowid

    conn.close()
    return user_id

def get_frequently_asked_questions():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT user_message, COUNT(*) as count
        FROM chat_history
        GROUP BY user_message
        ORDER BY count DESC
        LIMIT 5
    ''')
    faq_data = cursor.fetchall()
    conn.close()

    return dict(faq_data)


def get_recommended_questions(keyword):
    recommendations = []
    if "akreditas" in keyword and any(word in keyword for word in ("kampus", "stmik", "wicida")):
        recommendations = [
            "Apa akreditasi STMIK Wicida?",
            "Apa Akreditas Prodi Teknik Informatika?",
            "Apa Akreditas Prodi Sistem Informasi?",
            "Apa Akreditas Prodi Bisnis Digital?",
                                
        ]
    elif any(word in keyword for word in ("alur", "prosedur")):
        recommendations = [
            "Bagaimana alur pendaftaran jalur PMDK?",
            "Bagaimana alur pendaftaran jalur Reguler?",
            "Bagaimana alur pendaftaran jalur Alih Jenjang?",
        ]
    elif "daftar" in keyword and any(word in keyword for word in ("cara daftar", "mendaftar")):
        recommendations = [
            "Bagaimana cara mendaftar di STMIK Wicida?",
            "Prosedur pendaftaran di STMIK Wicida?",
        ]
    elif any(word in keyword for word in ("biaya", "bayar")):
        recommendations = [
            "Berapa biaya pendaftaran di STMIK Wicida?",
            "Berapa biaya daftar ulang di STMIK Wicida?",
            "Cara pembayaran biaya pendaftaran di STMIK Wicida?",
            "Bagaimana cara validasi pembayaran?",
        ]
    # Add additional logic for other relevant question recommendations here if needed
    return recommendations
