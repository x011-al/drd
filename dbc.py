import pyautogui
import time
from datetime import datetime, timedelta

# Setel fail-safe menjadi False
pyautogui.FAILSAFE = False

# Daftar koordinat untuk klik
coordinates = [
    (138, 181), 
    (446, 177), 
    (705, 199), 
    (952, 198), 
    (1250, 179), 
    (71, 386), 
    (435, 387), 
    (698, 395), 
    (971, 398), 
    (1204, 401), 
    (175, 584), 
    (1053, 611), 
]  

# Fungsi untuk melakukan double klik pada koordinat
def double_click(coord):
    pyautogui.moveTo(coord[0], coord[1], duration=0.5)  # Menggerakkan mouse dengan durasi 0.5 detik
    pyautogui.click(clicks=2, interval=0.25)  # Double klik dengan interval antar klik 0.25 detik
    print(f"[{datetime.now()}] Double klik dilakukan pada koordinat {coord}.")

# Hitung waktu akhir (24 jam dari sekarang)
end_time = datetime.now() + timedelta(hours=24)

# Loop utama
try:
    while datetime.now() < end_time:
        for coord in coordinates:
            double_click(coord)  # Double klik pada setiap koordinat
        print("Menunggu 2 menit sebelum klik berikutnya...")
        time.sleep(120)  # Tunggu selama 2 menit
    print("Program selesai setelah berjalan selama 24 jam.")
except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna.")
