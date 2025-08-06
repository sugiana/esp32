import machine
import os


I2S_LRCLK_PIN = 25
I2S_BCLK_PIN = 26
I2S_DIN_PIN = 27
I2S_ID = 0

# --- Ukuran Buffer I2S ---
# Semakin besar, semakin lancar, tapi butuh lebih banyak RAM
# Ukuran buffer harus kelipatan 8 (untuk 16-bit stereo)
# 512 cukup kecil untuk RAM terbatas, sesuaikan jika perlu
BUFFER_LEN_IN_BYTES = 2048


def init_i2s():
    return machine.I2S(
        I2S_ID,
        sck=machine.Pin(I2S_BCLK_PIN),
        ws=machine.Pin(I2S_LRCLK_PIN),
        sd=machine.Pin(I2S_DIN_PIN),
        mode=machine.I2S.TX,
        bits=16,
        rate=22050,
        ibuf=512,
        format=machine.I2S.MONO)


def ucapkan(s):
    audio_out = init_i2s()
    for t in s.split():
        filename = t + '.wav'
        with open(filename, 'rb') as f:
            f.seek(44)  # Abaikan header
            buffer = bytearray(BUFFER_LEN_IN_BYTES)
            while True:
                if not f.readinto(buffer):
                    break
                audio_out.write(buffer)
