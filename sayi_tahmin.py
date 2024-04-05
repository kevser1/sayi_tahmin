import random
from random import randint
KOLAY_SEVIYE = 10
ZOR_SEVIYE = 5
hak = 0
def haklar():
    global hak
    print("Sayı tahmin oyununa hoşgeldiniz.")
    secim = input("Lütfen bir zorluk seviyesi seçiniz: Kolay/zor")

    if secim == "kolay":
        hak = KOLAY_SEVIYE

    elif secim == "zor":
        hak = ZOR_SEVIYE

def tahmin_kontrol():
    global hak
    while hak > 0:

        tahmin = int(input("Lütfen 1-100 arasında bir sayı seçiniz."))
        sayi = random.randint(1,101)
        if tahmin == sayi:
            print("Tebrikler kazandınız :)")
            break
        elif tahmin < sayi:
            print("Tahmininizi biraz daha yükseltmelisiniz ;)")

        elif tahmin > sayi:
            print("Tahmininizi biraz düşürmelisiniz ;)")
        hak -=1
        print(f"kalan hak sayısı:{hak}")
    else:
         print("hakkınız bitti oyunu kaybettiniz :'(")


haklar()
tahmin_kontrol()
