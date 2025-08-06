# http://python.web.id/angka-terbilang-pada-python/#.VQpS8s2sXQo

satuan = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh',
          'delapan', 'sembilan', 'sepuluh', 'sebelas']


def terbilang_(n):
    n = int(n)
    if n >= 0 and n <= 11:
        hasil = [satuan[n]]
    elif n >= 12 and n <= 19:
        hasil = terbilang_(n % 10) + ['belas']
    elif n >= 20 and n <= 99:
        hasil = terbilang_(n / 10) + ['puluh'] + terbilang_(n % 10)
    elif n >= 100 and n <= 199:
        hasil = ['seratus'] + terbilang_(n - 100)
    elif n >= 200 and n <= 999:
        hasil = terbilang_(n / 100) + ['ratus'] + terbilang_(n % 100)
    elif n >= 1000 and n <= 1999:
        hasil = ['seribu'] + terbilang_(n - 1000)
    elif n >= 2000 and n <= 999999:
        hasil = terbilang_(n / 1000) + ['ribu'] + terbilang_(n % 1000)
    elif n >= 1000000 and n <= 999999999:
        hasil = terbilang_(n / 1000000) + ['juta'] + terbilang_(n % 1000000)
    else:
        hasil = terbilang_(n / 1000000000) + ['miliar'] + \
                terbilang_(n % 100000000)
    return hasil


def terbilang(n):
    if n == 0:
        return 'nol'
    t = terbilang_(n)
    while '' in t:
        t.remove('')
    return ' '.join(t)


if __name__ == '__main__':
    n = [0, 1, 2, 3, 4, 5, 10, 11, 12, 13, 19, 20, 21, 50, 99, 100, 102,
         989, 1000, 1001, 9891, 10000, 12500, 100000, 200001, 987123, 1000000,
         10000000, 10000000000]

    for i in n:
        s = '{:,}'.format(i)
        print('{i} -> {t}'.format(i=s, t=terbilang(i)))
