# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan program

# Mevcut yılı bir değişkende saklıyoruz
mevcut_yil = 2026

# Kullanıcıdan adını metin (string) olarak istiyoruz
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını alıp işlem yapabilmek için tam sayıya (int) çeviriyoruz
dogum_yili = int(input("Doğum yılınız nedir? "))

# Kendi eklediğim geliştirme: Doğum yılı gelecekteyse veya 1900'den küçükse uyarı veriyoruz
if dogum_yili > mevcut_yil:
    print(f"Uyarı: {dogum_yili} yılı henüz gelmedi! Lütfen geçerli bir doğum yılı giriniz.")
elif dogum_yili < 1900:
    print("Uyarı: Lütfen 1900 veya sonrası geçerli bir doğum yılı giriniz.")
else:
    # Mevcut yıldan doğum yılını çıkararak yaşı hesaplıyoruz
    yas = mevcut_yil - dogum_yili

    # Kullanıcıya adı ve yaşıyla özel karşılama mesajı yazdırıyoruz
    print(f"Merhaba {ad}! {yas} yaşındasın. Kodlama yolculuğuna hoş geldin!")

# Pencerenin hemen kapanmaması için kullanıcıdan giriş bekliyoruz
input("\nÇıkmak için Enter tuşuna basın...")