Penggunaan Microcontroller ESP32
================================

Papan / *board* yang memuat microcontroller ini dikenal memiliki ciri:

1. WiFi
2. Memori yang cukup besar untuk `MicroPython <https://micropython.org>`_
3. Lampu daya
4. Lampu uji coba 

Ada beragam papan / *kit* / *board* yang dirakit untuknya. Berikut kriteria pemilihan:

1. USB tipe C agar tidak berpikir lagi mengenai posisi colokan saat menancapkan
   kabel. Hal yang merepotkan saat menggunakan micro USB.
2. Pengisi baterai / *charger* 
3. Charger memiliki kemampuan *auto cut-off* agar berhenti mengisi baterai bila sudah penuh 

Oleh karena itu dipilihlah
`ESP32 LOLIN32 Lite <https://www.tokopedia.com/tokorytech/esp32-lolin32-lite-usb-type-c-wifi-bluetooth-4mb-1731171320402773303>`_
seharga Rp 42.000 (26 Juli 2025).

.. list-table:: Perbandingan Berbagai Papan ESP32 
   :header-rows: 1

   * - Kemampuan 
     - `ESP32 DevKit V1 <https://www.tokopedia.com/electracore-id/esp32-devkit-v1-30-pin-ch340-cp2102-usb-type-c-modul-wifi-bluetooth-1731154629195433959>`_
     - `ESP32 LOLIN32 Lite <https://www.tokopedia.com/tokorytech/esp32-lolin32-lite-usb-type-c-wifi-bluetooth-4mb-1731171320402773303>`_
   * - USB
     - Tipe C, driver chip CH340
     - Tipe C, driver chip CH340
   * - WiFi 
     - Ada 
     - Ada 
   * - Pin Voltage Input
     - 3,3V dan 5V
     - 3,3V
   * - LED
     - Pin 2, 0 = OFF, 1 = ON
     - Pin 22, 0 = ON, 1 = OFF
   * - Konektor baterai
     - Tidak ada 
     - 3,7V `konektor JST PH (jarak antar pin 2 mm) <https://www.mattmillman.com/info/crimpconnectors/common-jst-connector-types/#shsr>`_ male
   * - Charger baterai
     - Tidak ada
     - Ada melalui USB yang sama
   * - Perlindungan baterai agar tidak overcharge
     - Tidak ada
     - Ada
   * - Firmware
     - `v1.25.0 (2025-04-15) .bin <https://micropython.org/resources/firmware/ESP32_GENERIC-20250415-v1.25.0.bin>`_
     - `v1.25.0 (2025-04-15) .bin <https://micropython.org/resources/firmware/ESP32_GENERIC-20250415-v1.25.0.bin>`_
   * - Teruji dengan papan `audio amplifier MAX98357 I2S <https://www.tokopedia.com/permony/max98357-i2s-audio-amplifier-module-filterless-class-d-amplification-supports-esp32-raspberry-pi>`_
       dan `speaker 4 Ohm 3 Watt <https://www.tokopedia.com/permony/speaker-4-ohm-3w-5w-sepiker-3-5-watt-4ohm-31mm-3w-e4b62>`_
     - Ya
     - Ya


Baterai
-------

Adapun baterai yang dibutuhkan bertegangan 3,7V. Kita bisa gunakan
`baterai lithium polymer 3,7V 1000mAh 523450 <https://www.tokopedia.com/makershop/baterai-lithium-polymer-3-7v-1000mah-523450>`_
seharga Rp 39.900 (29 Juli 2025).

Baterai tidak wajib ada. Sebuah kabel USB tipe C yang biasa digunakan untuk
mengisi handphone yang ditancapkan ke laptop sudah cukup untuk
menghidupkannya.


Jenis Colokan
-------------

ESP32 dan baterai tadi memiliki colokan / *connector*. Bila berbeda maka mudahnya
potong saja kabel pada baterai lalu **solder** ke papan ESP32.

Alternatifnya menggunakan colokan yang sesuai dengan **ESP32**. Unit yang dibeli
itu menggunakan colokan berstandar
`JST (Japan Solderless Terminal) <https://www.mattmillman.com/info/crimpconnectors/common-jst-connector-types/>`_
dengan ciri:

    1. Jenis: `PH <https://www.mattmillman.com/info/crimpconnectors/common-jst-connector-types/#ph>`_,
       artinya jarak antar pin 2 mm
    2. Bentuk: *male*
    3. Jumlah pin: 2

Oleh karena itu kita memerlukan
`colokan female <https://www.tokopedia.com/alladinshop/kabel-konektor-jst-ph2-0-ph-2-0-3pin-4pin-5pin-6pin-7pin-8pin-12pin-2pin>`_
untuk disambungkan ke baterai.

PERHATIAN:

    Unit female pada tautan di atas saat dipasangkan ke ESP32 kabel hitamnya
    terhubung ke kutub positif. Sedangkan pada baterai kutub positif adalah
    kabel merah. Sesuaikanlah!

Jika masih *tidak tega* memotong kabel **baterai** maka informasinya adalah baterai
pada tautan tadi konektornya berciri:

    1. Jenis:
       `GH <https://www.mattmillman.com/info/crimpconnectors/common-jst-connector-types/#gh>`_,
       artinya jarak antar pin 1,25 mm
    2. Bentuk: female
    3. Jumlah pin: 2

Di toko online cari dengan kata kunci ``jst gh``.


Lampu Daya
----------

Berikut penjelasan mengenai lampu daya yang ada di papan ESP32.

.. list-table:: Penjelasan Lampu Daya

   * - **USB** 
     - **Baterai** 
     - **Lampu Daya** 
     - **Status Baterai** 
   * - Terpasang 
     - Lepas
     - Redup 
     -
   * - Terpasang 
     - Terpasang 
     - Terang
     - Pengisian 
   * - Terpasang 
     - Terpasang 
     - Padam 
     - Penuh
   * - Lepas
     - Terpasang
     - Padam 
     - Terpakai 


Sistem Operasi
--------------

Adapun sistem operasi komputer / laptop yang digunakan adalah
`Linux <https://linux.org>`_ dengan distro berbasis
`Debian <https://debian.org>`_. Saya menggunakan
`Linux Mint 22.1 xia <https://linuxmint.com>`_ yang berbasis
`Ubuntu 24.04 noble <https://ubuntu.com>`_. Tentunya Ubuntu berbasis Debian.

Tancapkan kabel USB ke laptop dan ke perangkat ESP32. Periksalah pesan kernel
mengenai nama port-nya::

    $ sudo dmesg -T | tail

    [Jum Jul 18 19:55:11 2025] usb 1-9: ch341-uart converter now attached to ttyUSB0

Itu artinya ada di port ``/dev/ttyUSB0``.

Catatan:

    Papan ESP32 yang digunakan memiliki chip CH340 untuk urusan USB tipe C.
    Linux yang saya gunakan sudah memuat driver-nya secara bawaan. Jadi
    pahamilah hal driver ini untuk sistem operasi lain.

Lalu perhatikan hak aksesnya::

    $ ls -lh /dev/ttyUSB0

    crw-rw---- 1 root dialout 188, 0 Jul 19 06:21 /dev/ttyUSB0

Dia hanya boleh diakses oleh grup ``dialout``. Agar kita tidak selalu
mengetikkan ``sudo`` saat menggunakannya maka sertakan user sebagai grup itu::

    $ sudo adduser sugiana dialout

Login ulang agar ini berdampak.


Python Virtual Environment
--------------------------

Selanjutnya buat Python Virtual Environment::

    $ python3.12 -m venv ~/env 
    $ ~/env/bin/pip install esptool adafruit-ampy

Versi Python ini bisa yang lain seperti 3.11, 3.10, atau 3.9.


Firmware
--------

Firmware merupakan istilah lain dari sistem operasi yang melekat di perangkat
kecil seperti ESP32 ini. Hapuslah firmware bawaan yang melekat di ESP32::

    $ ~/env/bin/esptool erase-flash

    esptool v5.0.1
    Connected to ESP32 on /dev/ttyUSB0:
    Chip type:          ESP32-D0WD-V3 (revision v3.1)
    Features:           Wi-Fi, BT, Dual Core + LP Core, 240MHz, Vref calibration in eFuse, Coding Scheme None
    Crystal frequency:  40MHz
    MAC:                6c:c8:40:56:44:e4

    Stub flasher running.

    Flash memory erased successfully in 2.3 seconds.

    Hard resetting via RTS pin...

Bersiaplah untuk unduh firmware MicroPython. Buka web
`ESP32 / WROOM <https://micropython.org/download/ESP32_GENERIC/>`_. Pada judul
**Firmware** lihat edisi terakhir seperti ini::

    v1.25.0 (2025-04-15) .bin / [.app-bin] / [.elf] / [.map] / [Release notes] (latest)

Singkatnya `ini tautannya <https://micropython.org/resources/firmware/ESP32_GENERIC-20250415-v1.25.0.bin>`_.
Lalu *flash* firmware tersebut::

    $ ~/env/bin/esptool write-flash 0x1000 ESP32_GENERIC-20250415-v1.25.0.bin 

    esptool v5.0.1
    Connected to ESP32 on /dev/ttyUSB0:
    Chip type:          ESP32-D0WD-V3 (revision v3.1)
    Features:           Wi-Fi, BT, Dual Core + LP Core, 240MHz, Vref calibration in eFuse, Coding Scheme None
    Crystal frequency:  40MHz
    MAC:                6c:c8:40:56:44:e4

    Stub flasher running.

    Configuring flash size...
    Flash will be erased from 0x00001000 to 0x001a0fff...
    Compressed 1702240 bytes to 1117021...
    Writing at 0x0003a9af [=>                            ]   7.3% 81920/1117021 bytes... 

Ini berlangsung tidak sampai dua menit hingga akhirnya tampil ini::

    Wrote 1702240 bytes (1117021 compressed) at 0x00001000 in 99.8 seconds (136.5 kbit/s).
    Hash of data verified.

    Hard resetting via RTS pin...


Debugger
--------

Debugger merupakan istilah untuk alat yang dapat memantau aktivitas script yang
kita buat. Jadi kita membutuhkan aplikasi yang bisa membaca dan menulis
``/dev/ttyUSB0`` dan menampilkannya di layar.

Pasanglah paket Debian bernama ``tio``::

    $ sudo apt install tio

Jalankan untuk mendapatkan prompt Python di ESP32::

    $ tio /dev/ttyUSB0

    [23:51:48.332] tio v2.7
    [23:51:48.332] Press ctrl-t q to quit
    [23:51:48.333] Connected

Tekan Enter agar prompt Python tampil::

    >>>

Cobalah::

    print('Hello world')

hasilnya::

    Hello world
    >>>

Lanjut menyalakan *lampu uji coba*::

    >>> from machine import Pin
    >>> led = Pin(22, Pin.OUT)
    >>>

Sampai di sini lampu menyala. Kita lihat statusnya::

    >>> led.value()
    0
    >>>

Ini artinya nol berarti lampu hidup. Coba kita matikan::

    >>> led.value(1)
    >>>

Itu berarti angka satu membuat lampu padam, ini tidak lazim. Di papan yang lain seperti
`ESP32 Dev Kit v1 <https://www.tokopedia.com/electracore-id/esp32-devkit-v1-30-pin-ch340-cp2102-usb-type-c-modul-wifi-bluetooth-1731154629195433959>`_
yang terjadi adalah sebaliknya yaitu nol berarti padam, satu berarti hidup.

Untuk mengakhiri ``tio`` tekan ``Ctrl T Q``.

Sekarang lihat ada file apa saja di dalamnya::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 ls

    /boot.py

Lihat isi file itu::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 get boot.py

    # This file is executed on every boot (including wake-boot from deepsleep)
    #import esp
    #esp.osdebug(None)
    #import webrepl
    #webrepl.start()

Biarkan ia tidak menjalankan apapun.

PERHATIAN:

    Pastikan ``tio`` tidak aktif saat hendak menjalankan ``ampy`` karena
    keduanya menggunakan port yang sama.

Unggahlah file ``led.py``::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 put esp32-lolin32-lite/led.py 

Cobalah::

    $ tio /dev/ttyUSB0

    >>> import led

Lihat status lampu::

    >>> led.is_on()
    False
    >>>

Hidupkan::

    >>> led.on()
    >>>

Matikan::

    >>> led.off()
    >>>

Jika kita memiliki ESP32 yang lain maka cobalah gunakan file ``esp32-generic/led.py``.


Script Utama
------------

Saat ESP32 dihidupkan maka yang pertama dijalankan adalah ``boot.py``, lalu
``main.py``. Adapun ``boot.py`` dikhususkan untuk menjalankan yang jarang berubah.
Namun bila ada kesalahan di ``boot.py`` maka kemungkinan kita tidak dapat lagi
menggunakan perangkat ini. Jadi amannya kita buat semua di ``main.py`` saja.

Rencananya adalah membuat lampu berkedip. Unggah filenya::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 put berkedip/main.py

Lalu di perangkat tekan tombol RESET. Di papannya tertulis EN yang artinya
*enable*. Kalau kita menghadap ke colokan USB maka posisi tombol ini berada di
sebelah kiri.

Alternatif menekan tombol RESET pada papan ESP32 adalah dengan menekan
``Ctrl D`` pada ``tio``.

   
WiFi Manager
------------

Berikut ini alur agar perangkat bisa menyimpan username dan password WiFi:

1. Pengguna: menghidupkan perangkat
2. Script: kalau tidak ada file ``wifi.dat`` atau gagal terhubung ke WiFi maka aktifkan moda **Access Point** (AP)
3. Pengguna: arahkan handphone ke AP itu yang bernama ``WifiManager``
4. Pengguna: di web browser buka ``http://192.168.4.1`` untuk memilih SSID dan mengisi password. Klik Submit.
5. Script: mencoba login ke AP yang ada di rumah. Jika berhasil simpan ke file
   ``wifi.dat``, lalu otomatis *reboot*. Bila gagal maka tampilkan di web.
6. Script: kalau berhasil terhubung ke WiFi lanjutkan ke aplikasi utama. Sampai
   di sini si perangkat sebagai **Station**.

Catatan:

    Terkait poin 5 maka firmware terbaru tidak mendukung enkripsi WPA maupun
    WPA-PSK. Jadi meski username dan password sudah benar maka akan tampil
    pesan kegagalan. Yang sudah teruji adalah WPA2 dan WPA3. Di modem Indihome
    enkripsi ini bisa diganti.

Unggah ``wifimgr.py``::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 put wifimgr.py

Unggah ``main.py`` yang berisi aplikasi untuk kita menghidupkan lampu melalui web::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 put web/main.py

Aktifkan pemantaunya::

    $ tio /dev/ttyUSB0

    [09:18:28.918] tio v2.7
    [09:18:28.918] Press ctrl-t q to quit
    [09:18:28.920] Connected

Tekan ``Ctrl D`` untuk reboot.

Catatan:

    Jika sebelumnya sudah terhubung ke jaringan - sebagai station - maka
    ``Ctrl D`` tidak akan memutusnya, kita tetap perlu menekan tombol RESET.

Di ``tio`` akan tampil seperti ini::

    ets Jul 29 2019 12:21:46

    rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)

    Connect to WiFi ssid WifiManager, default password: 123456789
    and access the ESP via your favorite web browser at 192.168.4.1.
    Listening on: ('0.0.0.0', 80)

Kini arahkan handphone ke access point bernama ``WifiManager``. Lalu di web
browser seperti Chrome buka ``http://192.168.4.1`` untuk memilih SSID dan
mengisi password. Klik Submit.

Selanjutnya akan tampil seperti ini::

    ssid: OPPO A3 chan: 6 rssi: -50 authmode: ?
    Trying to connect to Rumah Indihome...
    with password ['17171717']
    ...........................
    Connected. Network config:  ('10.62.1.242', '255.255.255.0', '10.62.1.204', '10.62.1.204')
    ESP OK

Tampak IP-nya adalah ``10.62.1.242``. Di web browser buka
``http://10.62.1.242``, nanti akan tampil dua tombol ON dan OFF. Klik ON maka
*lampu uji coba* di ESP32 akan menyala. Klik OFF untuk mematikannya.


Diakses dari Jaringan Berbeda 
-----------------------------

Tadi kita dapat mengakses perangkat karena handphone atau laptop berada di
jaringan yang sama. Bila berbeda maka kita butuh server yang dapat diakses oleh
laptop maupun ESP32. Server dan perangkat yang dimaksud bisa saja ada di Rumah
B, lalu laptop ada di Rumah D.

Atau lebih luas lagi yaitu server ada di Internet, ESP32 di rumah B, dan
laptop ada di rumah D.


Protokol MQTT
-------------

Adalah `MQTT <https://mqtt.org>`_ yaitu sebuah protokol komunikasi ringan yang
dirancang untuk perangkat dengan sumber daya terbatas dan jaringan yang tidak
stabil, terutama digunakan dalam Internet of Things (IoT).

Catatan:

    IoT merupakan istilah yang dikaitkan dengan penerapan perangkat yang dapat
    dikendalikan dari Internet, seperti ESP32 ini.

Untuk kebutuhan menyalakan lampu dari laptop maka alurnya::

    publisher (laptop) -> broker (server) -> subscriber (perangkat) 

Sedangkan untuk situasi perangkat melaporkan ketinggian air sungai maka alurnya::

    publisher (perangkat) -> broker (server) -> subscriber (laptop)

Tentu nantinya akan ada banyak publisher yang terhubung ke **broker yang sama**.
Bagaimana subscriber memilahnya ?

Di sini ada yang namanya **topic** yang merupakan penghubung publisher dan
subscriber-nya. Berikut contohnya::

    Publisher
        Topic: lampu/cac20c5871dcc
        Send Message: on 

    Subscriber:
        Topic: lampu/cac20c5871dcc
        Receive Message: on 

Adapun kode ``cac20c5871dcc`` merupakan identitas perangkat yang bisa kita
peroleh dari MAC address yaitu identitas chip jaringan. Tapi ini tidak
harus. Kita bisa menggunakan topik lain seperti ``rumah-b/lampu/teras``
misalnya.

Cermatilah konsep ini.


Broker
------

Broker atau server menggunakan sistem operasi Linux yang berbasis distro
Debian. Kita bisa sewa VPS yang banyak tersedia di Internet. Untuk uji coba
bisa menggunakan laptop ini. Pasanglah::

    $ sudo apt install mosquitto

Lalu buat file ``/etc/mosquitto/conf.d/listener.conf``::

    listener 1883
    allow_anonymous true

Restart::

    $ sudo systemctl restart mosquitto

Broker ini *listen network* di port 1883.


Subscriber
----------

Karena kita akan menyalakan lampu yang ada di ESP32 dari laptop maka ESP32
sebagai penerima pesan / suscriber. Pesannya berisi perintah ``on``, ``off``,
dan ``status``.

Buatlah file ``broker.dat`` yang berisi IP dan port broker tadi, dipisahkan
oleh titik dua::

    10.93.64.249:1883

Apakah IP bisa diganti dengan hostname ? Bisa contoh::

    warga.web.id:1883

Hostname berguna bila broker berada di Internet, sewaktu-waktu IP-nya berubah
maka file ``broker.dat`` yang ada di perangkat IoT tidak perlu diubah.

Selanjutnya unggah file itu::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 broker.dat

Juga script subscriber::

    $ ~/env/bin/ampy -p /dev/ttyUSB0 mqtt/common.py
    $ ~/env/bin/ampy -p /dev/ttyUSB0 mqtt/main.py

Aktifkan *debugger*::

    $ tio /dev/ttyUSB0

Tekan ``Ctrl D`` untuk reboot, atau tekan tombol RESET pada papan ESP32. Nanti
akan tampil seperti ini::

    Sudah terhubung ke MQTT broker 10.93.64.249:1883.
    Subscribe ke topik lampu/cac20c5871dcc
    Menunggu ...
    Menunggu ..
    Menunggu ...
    Menunggu ..

Biarkan dia menunggu.


Publisher
---------

Sekarang beralih ke pengirim perintah / pesan alias sebagai publisher yaitu
laptop ini. Jalankan::

    $ ~/env/bin/python mqtt/publisher.py --help

Hasilnya::

    usage: publisher.py [-h] [--host HOST] [--port PORT] [--client-id CLIENT_ID] [--topic TOPIC] [--message MESSAGE] [--wait-seconds WAIT_SECONDS]

    options:
      -h, --help            show this help message and exit
      --host HOST           default localhost
      --port PORT           default 1883
      --client-id CLIENT_ID
                            default: laptop-sugiana
      --topic TOPIC         default: lampu/cac20c5871dcc
      --message MESSAGE     default: on
      --wait-seconds WAIT_SECONDS
                            default 30

Hidupkan lampu::

    $ ~/env/bin/python publisher.py --topic=lampu/cac20c5871dcc --message=on

Jika MQTT broker bukan di ``localhost`` maka::

    $ ~/env/bin/python publisher.py --host=warga.web.id --topic=lampu/cac20c5871dcc --message=on

Tentu saja MAC address ESP32 yang saya punya berbeda dengan yang kamu punya.
Jadi gantilah ``cac20c5871dcc`` dengan yang tadi tampil di ``tio``. Hasilnya
seperti ini::

    Sudah terhubung ke MQTT broker 10.93.64.249:1883.
    Subscribe ke topik lampu/cac20c5871dcc/response
    Publish {'message': 'on', 'id': '002522'} dengan topik lampu/cac20c5871dcc
    Diterima {'code': 0, 'id': '002522', 'message': 'on'} dari topik lampu/cac20c5871dcc/response
    Penantian 0.72 detik

Berikut yang tampak di ESP32::

    Diterima {'message': 'on', 'id': '002522'} dari topik lampu/cac20c5871dcc
    Publish {'code': 0, 'id': '002522', 'message': 'on'} ke topic lampu/cac20c5871dcc/response
    Menunggu ..
    Menunggu ...
    Menunggu ..
    Menunggu ...

Cermati lagi pesannya.

Mengapa ESP32 juga melakukan publish padahal ia subscriber ? Ini dilakukan agar
si laptop tahu bahwa pesan yang dikirim sudah diterima. Perhatikan ada
``id`` yang merupakan identitas pesan. Topiknya juga berbeda yaitu
berakhiran ``/response``. Berikut urutan kejadiannya.

.. list-table:: Komunikasi Antara Laptop dan ESP32 

   * - **No.** 
     - **ESP32** 
     - **Laptop**
   * - 1 
     - Sudah terhubung ke MQTT broker 10.93.64.249:1883.
     -
   * - 2
     - Subscribe ke topik lampu/cac20c5871dcc
     -
   * - 4 
     - Menunggu
     - Sudah terhubung ke MQTT broker 10.93.64.249:1883.
   * - 5 
     - Menunggu
     - Subscribe ke topik lampu/cac20c5871dcc/response 
   * - 6 
     - Menunggu
     - Publish {'message': 'on', 'id': '002522'} dengan topik lampu/cac20c5871dcc
   * - 7
     - Diterima {'message': 'on', 'id': '002522'} dari topik lampu/cac20c5871dcc
     - Menunggu
   * - 8
     - Publish {'code': 0, 'id': '002522', 'message': 'on'} ke topic lampu/cac20c5871dcc/response
     - Menunggu
   * - 9
     - Menunggu
     - Diterima {'code': 0, 'id': '002522', 'message': 'on'} dari topik lampu/cac20c5871dcc/response
 
Jadi tidak seperti Virtual Private Network yaitu keduanya terhubung langsung.
Di MQTT semua pesan yang dikirim ditampung dulu di *broker*.

Beberapa hal yang perlu diketahui tentang **cara kerja broker**:

    1. Saat menerima pesan dari publisher dia akan mengirimkannya ke para
       subscriber yang sedang online, lalu **menghapusnya**. Subscriber
       lain yang telat online tidak akan menerima pesan tersebut.
    2. Client ID yang sama akan memutus koneksi sebelumnya. Jadi pastikan ia
       unik. Di ``publisher.py`` bisa kita tetapkan dengan opsi
       ``--client-id``. Sedangkan di ESP32 client ID adalah **MAC address**
       yang seharusnya unik di jagat perangkat.

Pahamilah.


Kotak Bersuara
--------------

Mari lanjut ke kehidupan sebenarnya. Kita akan membuatnya bersuara mengucapkan
kalimat yang dikirim publisher.

Misalkan Anda telah membuat sistem antrian di sebuah layanan masyarakat. Selain
nomor antrian tampil di layar juga ada suara yang mengucapkannya seperti::

    nomor antrian tujuh belas di loket b

Jadi aplikasi antrian sebagai publisher, dan ESP32 sebagai subscriber-nya,
masih sama situasinya dengan penyalaan lampu tadi. Apa yang dilakukan ESP32
dengan kalimat itu ?

Ia akan memecahnya menjadi kumpulan kata dan menyuarakan (*play*) file WAV
setiap kata. Jadi ia akan menyuarakan file ``nomor.wav``, ``antrian.wav``,
``tujuh.wav``, ``belas.wav``, ``di.wav``, ``loket.wav``, dan ``b.wav``.
File-file ini sudah tersedia di direktori ``ucapkan``, silakan diunggah.

Secara hardware papan ESP32 ini tersambung dengan *audio amplifier* serta
*speaker*.


.. list-table:: Konektivitas Pin ESP32 dengan Audio Amplifier
   :header-rows: 1

   * - `ESP32 LOLIN32 Lite <https://www.tokopedia.com/tokorytech/esp32-lolin32-lite-usb-type-c-wifi-bluetooth-4mb-1731171320402773303>`_
     - `Audio Amplifier MAX98357 I2S <https://www.tokopedia.com/permony/max98357-i2s-audio-amplifier-module-filterless-class-d-amplification-supports-esp32-raspberry-pi>`_
   * - 3.3V
     - Vin 
   * - GND
     - GND
   * - 25
     - LRCLK
   * - 26
     - BCLK
   * - 27
     - DIN

Setelah kaki bawaan mereka disolder kita bisa menghubungkannya dengan
`kabel jumper female to female <https://tokopedia.com/elektronikdr/kabel-cable-jumper-pelangi-female-to-female-20cm-1-pin-helai-biji>`_.


.. list-table:: Konektivitas Pin Amplifier dengan Speaker
   :header-rows: 1

   * - Amplifier
     - Speaker
   * - Positif (+)
     - Positif (+)
   * - Negatif (-)
     - Negatif (-)

Kalau ini butuh
`kabel jumper male to male <https://www.tokopedia.com/elektronikdr/kabel-cable-jumper-pelangi-male-to-male-10cm-1-pin-helai-biji>`_.
Di bagian amplifier sudah ada colokannya, sedangkan di bagian speaker masih perlu disolder.

Setelah semua terhubung mulailah unggah file-file WAV yang ada di direktori ``ucapkan/``. Unggah juga script Python-nya:

    1. ``ucapkan/play.py``
    2. ``ucapkan/main.py``

Jalankan ``tio``, lalu reset. Seharusnya terdengar::

    kotak suara diaktifkan

Lalu tampil::

    Connected. Network config:  ('10.93.64.246', '255.255.255.0', '10.93.64.127', '10.93.64.127')
    Sudah terhubung ke MQTT broker 10.93.64.249:1883.
    Subscribe ke topik pengucapan/cac20c5871dcc

Lalu jalankan publisher-nya::

    $ ~/env/bin/python mqtt/publisher.py --topic=pengucapan/cac20c5871dcc --message="nomor antrian tujuh belas di loket b"
    
hasilnya::

    Sudah terhubung ke MQTT broker warga.web.id:1883.
    Subscribe ke topik pengucapan/3c71bf4268e0/response
    Publish {'message': 'nomor antrian tujuh belas di loket b', 'id': '222945'} dengan topik pengucapan/3c71bf4268e0
    Diterima {'code': 0, 'id': '222945', 'message': 'OK'} dari topik pengucapan/3c71bf4268e0/response

Ujilah dengan berbagai kondisi seperti:

    1. Kata yang dikirim belum ada file WAV-nya
    2. Hotspot dimatikan, setelah 30 detik dihidupkan lagi
    3. MQTT broker dimatikan, setelah 30 detik hidupkan lagi

Apakah pengujian tersebut membuat ESP32 berhenti bekerja ? Atau kembali bekerja ?

Cobalah.


Referensi
---------
* `ESP32 / WROOM <https://micropython.org/download/ESP32_GENERIC/>`_
* `MicroPython untuk Pemula : Ep. 1 Pengenalan dan Instalasi <https://www.youtube.com/watch?v=_DHEfQWEBIo>`_
* `MicroPython: Wi-Fi Manager with ESP32 <https://randomnerdtutorials.com/micropython-wi-fi-manager-esp32-esp8266/>`_
* `problems with network.WLAN.connect in v1.24.0 and 1.23.0 <https://github.com/orgs/micropython/discussions/16089>`_
* `Gemini <https://gemini.google.com>`_
* `ESP32 WeMos LOLIN32 Lite high resolution pinout and specs <https://mischianti.org/esp32-wemos-lolin32-lite-high-resolution-pinout-and-specs/>`_
