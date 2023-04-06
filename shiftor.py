def shift_or(text, pattern):
    # önceden işlenmiş maske tablosu oluşturma
    m = len(pattern)
    mask = [0xFFFFFFFF] * (m + 1)
    for i in range(m):
        mask[i] = mask[i] ^ (1 << (m - i - 1))

    # metni sağa doğru kaydırarak eşleşmeyi bul
    n = len(text)
    count = 0
    for i in range(n - m + 1):
        r = 0xFFFFFFFF
        for j in range(m):
            r = r & mask[j]
            r = r & (1 << (m - j - 1 - 1 - ord(text[i+j])))  # ASCII koduna göre kaydırdık
        if (r & 1) == 0:
            count += 1
    return count

# 'Alice in Wonderland' metnini oku
with open('alice_in_wonderland.txt', 'r') as f:
    text = f.read()

# kaçış karakterlerini kaldır
text = text.replace('\n', ' ').replace('\r', '')

# aranan ifadeleri say
patterns = ['upon', 'sigh', 'Dormouse', 'jury-box', 'swim']
for pattern in patterns:
    count = shift_or(text, pattern)
    print(f"'{pattern}' ifadesi {count} kez geçiyor.")