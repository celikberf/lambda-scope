BerfHesap = {
    'ad' : 'Berfin Çelik',
    'hesapNo' : '12323212',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

GulerHesap = {
    'ad' : 'Güler Çelik',
    'hesapNo' : '54323454',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar) :
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar :
            ekHesapKullanimi = input('Ek Hesap Kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilcakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilcakMiktar
                print('Paranızı alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır")
    
        else:
            print('Bakiye yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']}")



paraCek(BerfHesap,3000)
bakiyeSorgula(BerfHesap)

paraCek(BerfHesap,2000)
bakiyeSorgula(BerfHesap)
