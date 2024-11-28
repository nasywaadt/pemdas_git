data_panen = {
    'lokasi1' : {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500,
        }
    },
    'lokasi2' : {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450,
       }
   },
   'lokasi3' : {
       'nama_lokasi': 'Kebun C',
       'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600,
       }
   },
   'lokasi4' : {
       'nama_lokasi': 'Kebun D',
       'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550,
       }
   },
    'lokasi5' : {
       'nama_lokasi': 'Kebun E',
       'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480,
        }
   }
}

#Melakukan perubahan pada file
print ("=== Data Panen (Tugas Git) ===")



#Menampilkan seluruh data lokasi dan hasil panen
print (data_panen)

#Menampilkan jumlah hasil panen jagung dari lokasi2
print(data_panen['lokasi2']['hasil_panen']['jagung'])

#Menampilakan lokasi dari lokasi3
print(data_panen['lokasi3']['nama_lokasi'])

#Memasukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel yang berbeda
for i, j in data_panen.items():
    padi = j['hasil_panen']['padi']
    kedelai = j['hasil_panen']['kedelai']
    nama_lokasi = j['nama_lokasi']

    #Membuat percabangan jika jumlah hasil panen padi lebih dari 1300 
    # atau kedelai lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus. 
    # Jika tidak, maka lokasi tersebut dalam kondisi baik.
    if padi > 1300 or kedelai > 800:
        print(f"Lokasi {nama_lokasi} memerlukan perhatian khusus")
    else:
        print(f"Lokasi {nama_lokasi} dalam kondisi baik")

