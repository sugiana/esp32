import sys
from pydub import AudioSegment
from pydub.silence import detect_leading_silence

def remove_leading_and_trailing_silence(audio_path, silence_threshold=-40, chunk_size=100):
    """
    Menghapus keheningan di awal dan akhir file audio.

    Args:
        audio_path (str): Jalur lengkap ke file audio (misal: 'audio_saya.wav').
        silence_threshold (int): Ambang batas (dalam dBFS) di bawah mana audio dianggap hening.
                                 Nilai yang lebih rendah berarti lebih hening. Default: -40 dBFS.
        chunk_size (int): Ukuran potongan (dalam milidetik) untuk menganalisis audio.
                          Default: 100 ms.

    Returns:
        AudioSegment: Objek AudioSegment yang telah diproses.
                      Mengembalikan None jika ada masalah saat memuat file.
    """
    try:
        audio = AudioSegment.from_wav(audio_path)
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di '{audio_path}'")
        return None
    except Exception as e:
        print(f"Error saat memuat file audio: {e}")
        return None

    # Hapus keheningan di awal
    # detect_leading_silence mengembalikan jumlah milidetik keheningan di awal
    start_trim = detect_leading_silence(audio, silence_threshold=silence_threshold, chunk_size=chunk_size)
    trimmed_audio = audio[start_trim:]

    # Hapus keheningan di akhir
    # Untuk menghapus keheningan di akhir, kita bisa membalik audio,
    # menghapus keheningan di awal (yang sekarang keheningan akhir),
    # dan kemudian membalikkannya kembali.
    reversed_audio = trimmed_audio.reverse()
    end_trim_reversed = detect_leading_silence(reversed_audio, silence_threshold=silence_threshold, chunk_size=chunk_size)
    final_trimmed_audio = reversed_audio[end_trim_reversed:].reverse()

    return final_trimmed_audio

def save_processed_audio(audio_segment, output_path):
    """
    Menyimpan objek AudioSegment ke file WAV.

    Args:
        audio_segment (AudioSegment): Objek AudioSegment yang akan disimpan.
        output_path (str): Jalur lengkap untuk menyimpan file output (misal: 'audio_bersih.wav').
    """
    try:
        audio_segment.export(output_path, format="wav")
        print(f"Audio berhasil disimpan ke '{output_path}'")
    except Exception as e:
        print(f"Error saat menyimpan file audio: {e}")

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    input_file = sys.argv[1]  # Ganti dengan nama file WAV Anda

    # Proses penghapusan keheningan
    processed_audio = remove_leading_and_trailing_silence(input_file)

    if processed_audio:
        save_processed_audio(processed_audio, input_file)
