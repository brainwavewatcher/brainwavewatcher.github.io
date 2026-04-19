import json
import os
import random
import string

BASE_PATH = "data"

LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2", "ielts", "toefl"]

# 🔤 rastgele kelime üretici
def random_word():
    length = random.randint(4, 10)
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# ✏️ kelime objesi
def generate_word(level):
    word = random_word()
    return {
        "word": word,
        "meaning": f"{word} meaning",
        "example": f"This is an example sentence with '{word}'.",
        "level": level.upper()
    }

# 📖 rastgele cümle üretici
def random_sentence():
    words = [random_word() for _ in range(random.randint(6, 12))]
    sentence = " ".join(words)
    return sentence.capitalize() + "."

# 📚 okuma parçası üretici
def generate_reading(index):
    sentences = [random_sentence() for _ in range(random.randint(5, 10))]
    return {
        "id": index,
        "title": f"Reading Passage {index+1}",
        "text": " ".join(sentences),
        "questions": [
            {
                "question": "What is the main idea of the text?",
                "answer": "It is randomly generated."
            },
            {
                "question": "How many sentences are there?",
                "answer": str(len(sentences))
            }
        ]
    }

def main():
    os.makedirs(BASE_PATH, exist_ok=True)

    # 📌 KELİMELER
    for level in LEVELS:
        path = os.path.join(BASE_PATH, level)
        os.makedirs(path, exist_ok=True)

        words = [generate_word(level) for _ in range(1000)]

        # 100’lük sayfalara böl
        for i in range(0, 1000, 100):
            chunk = words[i:i+100]
            page = i // 100

            with open(os.path.join(path, f"page{page}.json"), "w", encoding="utf-8") as f:
                json.dump(chunk, f, ensure_ascii=False, indent=2)

        print(f"✅ {level} tamamlandı")

    # 📖 READING
    reading_path = os.path.join(BASE_PATH, "reading")
    os.makedirs(reading_path, exist_ok=True)

    readings = [generate_reading(i) for i in range(100)]

    with open(os.path.join(reading_path, "reading.json"), "w", encoding="utf-8") as f:
        json.dump(readings, f, ensure_ascii=False, indent=2)

    print("📚 Reading tamamlandı")
    print("🚀 HER ŞEY BİTTİ")

if __name__ == "__main__":
    main()
