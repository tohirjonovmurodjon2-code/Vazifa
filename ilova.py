FAYL = "malumotlar.txt"
vazifalar = []

def yuklash():
    try:
        with open(FAYL, "r", encoding="utf-8") as f:
            return [q.rstrip("\n") for q in f]
    except FileNotFoundError:
        return []

def saqlash():
    with open(FAYL, "w", encoding="utf-8") as f:
        for v in vazifalar:
            f.write(v + "\n")

def menyu():
    print("\n--- Vazifalar ilovasi ---")
    print("1 - Vazifa qo'shish")
    print("2 - Ro'yxatni ko'rish")
    print("3 - Vazifani o'chirish")
    print("0 - Chiqish")

def vazifa_qoshish():
    matn = input("Yangi vazifani kiriting: ").strip()
    if not matn:
        print("❗ Bo'sh vazifa qo'shib bo'lmaydi.")
        return
    vazifalar.append(matn)
    print("✅ Vazifa qo'shildi.")

def royxatni_korish():
    if not vazifalar:
        print("Ro'yxat bo'sh.")
        return
    for i, v in enumerate(vazifalar, start=1):
        print(f"{i}. {v}")

def vazifa_ochirish():
    if not vazifalar:
        print("O'chirish uchun vazifa yo'q.")
        return
    royxatni_korish()
    raqam_str = input("O'chirish uchun vazifa raqamini kiriting: ").strip()
    if not raqam_str.isdigit():
        print("❗ Faqat raqam kiriting.")
        return
    raqam = int(raqam_str)
    if 1 <= raqam <= len(vazifalar):
        olingan = vazifalar.pop(raqam - 1)
        print(f"🗑️ O'chirildi: {olingan}")
    else:
        print("❗ Bunday raqamli vazifa yo'q.")

if __name__ == "main":
    vazifalar = yuklash()
    while True:
        menyu()
        tanlov = input("Tanlovingizni kiriting: ")
        if tanlov == "1":
            vazifa_qoshish()
        elif tanlov == "2":
            royxatni_korish()
        elif tanlov == "3":
            vazifa_ochirish()
        elif tanlov == "0":
            saqlash()
            print("Vazifalar saqlandi. Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov.")