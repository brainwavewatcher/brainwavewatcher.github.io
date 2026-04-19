import json
import os
import random

# 📁 Kategoriler
categories = [
    "words_a1", "words_a2", "words_b1", "words_b2",
    "words_c1", "words_c2",
    "toefl", "ielts",
    "daily_words", "daily_phrases"
]

base_path = "data"

# 📂 Klasörleri oluştur
for cat in categories:
    os.makedirs(f"{base_path}/{cat}", exist_ok=True)

# 🧠 Kelime havuzu (bunu sonra büyütebiliriz)
base_words = [
    "abandon","achieve","adapt","analyze","approach","assume","benefit",
    "create","define","develop","effect","establish","evaluate","focus",
    "function","identify","improve","indicate","interpret","maintain",
    "occur","percent","period","policy","principle","process","require",
    "respond","significant","similar","source","structure","theory"
]

# ✏️ Kelime üretici
def generate_word(level):
    word = random.choice(base_words)
    return {
        "word": word,
        "meaning": f"{word} anlamı",
        "example": f"This is an example sentence with '{word}'.",
        "level": level
    }

# 🚀 Her kategori için veri üret
for cat in categories:
    level = cat.upper()

    # 1000 kelime üret
    data = [generate_word(level) for _ in range(1000)]

    # 100'lü JSON dosyalarına böl
    for i in range(0, 1000, 100):
        chunk = data[i:i+100]
        page = i // 100

        file_path = f"{base_path}/{cat}/page{page}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(chunk, f, ensure_ascii=False, indent=2)

print("✅ Tüm veriler üretildi.")
