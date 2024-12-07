#!/bin/bash
# Perbarui repositori
sudo yum update -y

# Instal XFCE4 desktop environment dan terminalnya
sudo yum groupinstall "Xfce" -y
sudo yum install xfce4-terminal -y

# Unduh Chrome Remote Desktop
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_x86_64.rpm

# Instal Chrome Remote Desktop
sudo yum localinstall chrome-remote-desktop_current_x86_64.rpm -y

# Instal dependensi tambahan jika diperlukan
sudo yum install -f -y
