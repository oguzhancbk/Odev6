def kare(k):
    print("Karenin alanı = {}".format(k * k))

def dikdortgen(k, u):
    print("Dikdörtgenin alanı = {}".format(k * u))
    
def daire(pi,r):
    print("Dairenin alanı = {}".format((pi)*(r^2)))
    
def ucgenin_alanı(taban, yükseklik):
    print(f"Üçgenin alanı {taban * yükseklik / 2}")

def eskenardortgen(a_k, y_k):
    print("Eşkenar dörtgenin alanı = {}".format((a_k * y_k) / 2))
    
if __name__ == '__main__':
    print("""
    1 - Kare
    2 - Dikdörtgen
    3 - Daire
    4 - Üçgen
    5 - Eşkenar Dörtgen

    """)

    secim = int(input("Alanını hesaplamak istediğiniz şekil: "))

    if secim == 1:
        k = int(input("Karenin bir kenarı: "))
        kare(k)

    elif secim == 2:
        k = int(input("Dikdörtgenin kısa kenarı: "))
        u = int(input("Dikdörtgenin uzun kenarı: "))
        dikdortgen(k, u)
        
    elif secim == 3:
        pi = 3.14
        r = float(input("Yarı çap giriniz: "))
        daire(pi,r)

    elif secim == 3:
        t = int(input("Taban Girin : "))
        h = int(input("Yükseklik girin : "))
        ucgenin_alanı(t, h)
         
    elif secim == 4:
        a = int(input("Eşkenar dörtgenin alt kenar uzunluğu: "))
        y = int(input("Eşkenar dörtgenin yan kenar uzunluğu: "))
        eskenardortgen(a, y)

    else:
        print("Sadece belirtilen sayılardan birini giriniz.")
