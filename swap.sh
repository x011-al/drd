#!/bin/bash

# Ukuran swap dalam GB
SWAP_SIZE_GB=2

# Nama file swap
SWAPFILE=/swapfile

echo "Menambahkan Swap Memory sebesar ${SWAP_SIZE_GB}GB..."

# Mengecek apakah file swap sudah ada
if [ -f "$SWAPFILE" ]; then
  echo "File swap sudah ada di $SWAPFILE."
  echo "Proses dihentikan."
  exit 1
fi

# Membuat file swap
echo "Membuat file swap sebesar ${SWAP_SIZE_GB}GB..."
fallocate -l ${SWAP_SIZE_GB}G $SWAPFILE

# Jika fallocate tidak ada, gunakan dd (pilihan alternatif)
if [ $? -ne 0 ]; then
  echo "Fallocate tidak tersedia, mencoba menggunakan dd..."
  dd if=/dev/zero of=$SWAPFILE bs=1M count=$((SWAP_SIZE_GB * 1024))
fi

# Memberikan hak akses yang benar
echo "Mengatur izin file swap..."
chmod 600 $SWAPFILE

# Format file sebagai swap
echo "Memformat file swap..."
mkswap $SWAPFILE

# Mengaktifkan swap
echo "Mengaktifkan swap..."
swapon $SWAPFILE

# Menambahkan ke fstab agar swap aktif saat boot
echo "Menambahkan swap ke /etc/fstab agar permanen..."
echo "$SWAPFILE none swap sw 0 0" >> /etc/fstab

# Menampilkan status swap
echo "Swap berhasil ditambahkan. Status swap saat ini:"
swapon --show

# Selesai
echo "Proses selesai."
