from textblob import TextBlob
import json
import matplotlib
def duygu_analizi(tweet):
    blob = TextBlob(tweet)
    polarite = blob.sentiment.polarity
    nesnellik = blob.sentiment.subjectivity

    # Duygu kategorisi belirleme
    duygu = "Pozitif" if polarite > 0 else "Negatif" if polarite < 0 else "Nötr"

    # Duygu analizi sonuçlarını bir sözlük olarak döndürme
    return {"tweet": tweet, "polarite": polarite, "nesnellik": nesnellik, "duygu": duygu}

# Dosya yolunu belirtin
dosya_yolu = r'...\...\...\...\...\tweet_icerikleri.txt '

# Her bir tweet için duygu analizi sonuçlarını toplamak için bir liste oluşturun
duygu_analizi_sonuclari = []

# TXT dosyasını okuma
with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
    tweetler = dosya.readlines()

# Her bir tweet için duygu analizi yapma
for tweet in tweetler:
    sonuc = duygu_analizi(tweet)
    duygu_analizi_sonuclari.append(sonuc)

# Duygu analizi sonuçlarını JSON dosyasına yazma
with open("duygu_analizi.json", "w", encoding="utf-8") as json_dosyasi:
    json.dump(duygu_analizi_sonuclari, json_dosyasi, indent=4, ensure_ascii=False)


print("Duygu analizi sonuçları JSON dosyasına kaydedildi.")
