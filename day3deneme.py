#! Şirket çalışanları verilerini tutan dosya oluşturulacak
#! Kullanıcıdan çalışan sayısını alınacak
#! Çalışan sayısı kadar isim, soyisim, maaş bilgisi alınacak
#! Dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgileri eklenecek.
#! Programın sonunda bu dosyadan bilgileri satır satır okuyup listeleyecek kod yazılacak.
#! Eklenen çalışanlar mevcut çalışanları silmeyecek, üzerine yazılacak.
#! Programın belirli yerlerinde, hata yakalama işlemlerini unutma.

while True: 
    try:
        calisanSayisi = int(input('Çalışan Sayısını Giriniz:'))
    except ValueError:
        print('Hatalı Giriş.Tekrar giriş yapınız.')    
    else:
        break

for i in range(1,calisanSayisi+1):       

    isim = input(f'{i} . Çalışan Soyadını Giriniz: ')
    soyisim = input(f'{i}.Çalışan Soyadını Giriniz:')

    while True:
        try:
            maas = float(input(f'{i}. Çalışanın Maaşını Giriniz'))
        except:
            print('Hatali Giris. Tekrar giris yapınız.')
        else:
                break

    file = open('employees.txt' ',' 'a')        
    file.writelines(f"\n {isim} {soyisim} - {maas}")
    file.close()

print('Başarılı Bir Şekilde Eklenmiştir.')

file1 = open('employees.txt' ',' 'r')
lines = file1.readlines()
for line in lines : 
    print(line)

file1.close()    