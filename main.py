from machine import Pin
import network
import time

# Konfigurasi WiFi - GANTI DENGAN SSID DAN PASSWORD ANDA
SSID = "Wifi Sekolah B"
PASSWORD = ""

# Inisialisasi LED pada pin GPIO2 (LED built-in)
led = Pin(2, Pin.OUT)

# Fungsi untuk koneksi WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Menghubungkan ke WiFi...')
        wlan.connect(SSID, PASSWORD)
        
        # Tunggu hingga terhubung (maksimal 10 detik)
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            led.on()
            time.sleep(0.1)
            led.off()
            time.sleep(0.1)
            timeout -= 0.2
            
    if wlan.isconnected():
        print('WiFi Terhubung!')
        print('IP Address:', wlan.ifconfig()[0])
        
        # LED berkedip cepat 3x sebagai indikator berhasil
        for i in range(3):
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
        return True
    else:
        print('Gagal terhubung ke WiFi')
        return False

# Jalankan koneksi WiFi
if connect_wifi():
    # Setelah terhubung, nyalakan LED
    led.on()
    print("LED Menyala - WiFi Terhubung")
    
    time.sleep(3)
    
    # LED berkedip terus sebagai indikator WiFi aktif
    print("LED Berkedip - WiFi Aktif")
    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)
else:
    # Jika gagal, LED mati
    led.off()
    print("LED Mati - WiFi Gagal Terhubung")
