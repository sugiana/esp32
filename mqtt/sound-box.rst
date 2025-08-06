Sound Box
=========

Ini adalah perangkat yang bersuara ketika mendapat pesan dari server. Dalam
kaitannya di
`protokol MQTT <https://www.hivemq.com/blog/mqtt-essentials-part2-publish-subscribe/>`_
maka:

- Server adalah publisher
- Sound Box adalah subscriber


Ucapkan Angka
-------------

Contoh kasusnya adalah QRIS Sound Box. Setelah pembayaran selesai selanjutnya
server - sebagai publisher - akan menyampaikan nilainya ke Sound Box yang
merupakan subscriber. Di Sound Box sudah tersimpan file-file WAV yang akan
dirangkai sebagai *ucapan terbilang*.

Catatan:

    Mengingatkan kembali bahwa alur di MQTT adalah publisher -> broker ->
    subscriber. IP broker harus dikenali oleh publisher dan subscriber. Jadi
    publisher dan subscriber adalah MQTT client. Di contoh kasus ini publisher
    dan broker bisa di mesin yang sama.

Adapun topiknya adalah **identitas QRIS** statik yang berisi kode-kode khusus
QRIS pada umumnya.

Catatan:

    Istilah *topik* di MQTT mengacu pada hal apa saja yang menjadi perhatian
    subscriber.



Referensi
---------

* `MQTT Publish/Subscribe Architecture (Pub/Sub) – MQTT Essentials: Part 2 <https://www.hivemq.com/blog/mqtt-essentials-part2-publish-subscribe/>`_
