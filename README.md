# Shift-OrAlgorithm
Shift-or algorithm on Alice in wonderland text

Shift-Or algoritması, iki metni karşılaştırmak ve birinde diğerinin alt metni olarak var olup olmadığını belirlemek için kullanılan bir dize eşleştirme algoritmasıdır.

Algoritmanın temel mantığı, önceden işlenmiş bir maske tablosu ve kaydırma operasyonlarını kullanarak eşleştirmeyi gerçekleştirmektir. Maske tablosu, aranacak metindeki karakterlerin hangilerinin aranan metindeki karakterlerle eşleştiğini belirleyen bir bit maske dizisidir. Kaydırma operasyonu, aranan metnin sağa doğru kaydırılması işlemidir.

Shift-Or algoritması, birinci adımda maske tablosunu oluşturur ve ikinci adımda aranan metni sağa doğru kaydırır. Her kaydırma işlemi sırasında, maske tablosunda belirtilen karakterlerin aranan metindeki karakterlerle eşleşip eşleşmediği kontrol edilir. Eşleşme bulunursa, aranan metindeki alt metin bulunmuş demektir.

Shift-Or algoritması, boyutu ve önceden işlenmiş maske tablosu nedeniyle biraz belleği yoğun kullanır. Ancak, diğer bazı dize eşleştirme algoritmalarına kıyasla hızlıdır ve özellikle küçük metinler için etkilidir. Ayrıca, genişletilmiş versiyonları, dinamik programlama ve paralel hesaplama gibi diğer problemler için de kullanılabilir.

-Algoritma Analizi-

Shift-Or algoritmasının çalışma zamanı, metin uzunluğu n olan bir metinde bir desen uzunluğu m aramak için O(nm/w) zamanında gerçekleşir, burada w, sözcük boyutunu belirtir. Bu zamana, önceden hesaplanmış maske tablosunun oluşturulması sırasında bir miktarda eklenir.

En iyi durumda, desen metinde hiç geçmiyorsa, algoritmanın çalışma zamanı O(n/w) olacaktır. Bu durumda, metnin tamamı yalnızca bir kez işlenir ve aranan desen bulunamaz.

En kötü durumda, her desen karakteri ile metin karakterleri arasında tam bir eşleşme olmadığında, algoritmanın çalışma zamanı O(nm/w) olacaktır. Bu durumda, maske tablosunun her karakteri için m adımı atılır ve n - m + 1 adımda arama yapılır.

Ortalama durum, desenin metinde rastgele bir şekilde yerleştirildiği durumdur. Shift-Or algoritması, diğer dize eşleştirme algoritmaları gibi, aranan metnin belirli bir bölgesine odaklanmaz, bu nedenle ortalama durum da O(nm/w) olacaktır.
