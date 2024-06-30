import random

karakterler = "+-/*!&$?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


print("şifre oluşturucu ya hoş geldin")
ad = input("şifrede kullanacağın bir yazı parçası gir:")
sayi = int(input("şifrenin devamı kaç karakter olsun"))

sifre = ad

for i in range(sayi):
    sifre += random.choice(karakterler)

print(sifre)
print("bu şifreyi kopyalıyıp istediğiniz yere yapıştırın")
