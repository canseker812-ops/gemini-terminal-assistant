from google import genai #Google resmi yapay zeka kütüphanesi (GenAI)  projeye dahil eder.


client = genai.Client() #API anahtarını ortam değişkeninden (GEMINI_API_KEY) otomatik çeker.

chat = client.chats.create(model = "gemini-3.1-flash-lite") # Sohbet oturumu başlatır; önceki mesajları hafızada tutarak sohbet akışının bozulmasını engeller.

print("Yapay Zeka Asistanı Başlatıldı.")                # Kullanıcıya programın hazır olduğunu bildiren karşılama mesajını basar.
print("Çıkmak için 'q' veya 'exit' yazabilirsiniz.\n")  # Programdan nasıl çıkılacağını anlatan yönlendirme metnini yazar.
exit_list = ['q','exit','cikis','bitir']                # Çıkış tetikleyicisi olarak kabul edilecek anahtar kelimeleri bir liste içinde tanımlar.

while True:                                             # Kullanıcı çıkış yapana kadar programın sürekli çalışmasını sağlayan sonsuz döngü başlatır.
    user_input = input("Siz: ").strip()                 # Kullanıcıdan klavye girdisi alır ve başındaki/sonundaki gereksiz boşlukları kırpar.

    if not user_input:                                  # Kullanıcı hiçbir şey yazmadan sadece Enter'a bastıysa (boş girdi)...
        continue                                        # ...alt satırlara geçmeden döngünün başına döner ve tekrar girdi bekler.

    if user_input.lower() in  exit_list:                # Girilen metni küçük harfe çevirip çıkış listesinde var mı diye kontrol eder.                     
        print("Sohbet sonlandırıldı.Görüşmek üzere!")   # Kullanıcıya veda mesajını gösterir.
        break                                           # Sonsuz while döngüsünü kırarak programı sonlandırır.

    try:                                                # Olası internet kesintisi, kota dolumu veya API hatalarını yakalamak için güvenli deneme bloğu açar.
        response = chat.send_message(user_input)        # Kullanıcının mesajını sohbet geçmişine ekleyerek Yapay Zeka modeline iletir.
        print(f"\nAI:{response.text}\n")                # Modelden gelen yanıt metnini ekrana yazdırır.
        
    except Exception as error:                          # İstek sırasında herhangi bir hata veya çökme meydana gelirse...
        print(f"\n Bir hata oluştu {error}\n")          # Programın kapanmasını engelleyip hatanın açıklamasını ekrana basar.