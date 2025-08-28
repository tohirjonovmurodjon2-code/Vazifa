import vazifa

def menyu():
    print("\n--- Vazifalar ilovasi ---")
    print("1 - Vazifa qo'shish")
    print("2 - Ro'yxatni ko'rish")
    print("3 - Vazifani o'chirish")
    print("0 - Chiqish")

def vazifa_qoshish(vazifalar):
    matn = input("Yangi vazifani kiriting: ")
    if vazifa.qoshish(vazifalar, matn):
        print("✅ Vazifa qo'shildi.")
    else:
        print("❗ Bo'sh vazifa qo'shib bo'lmaydi.")

def royxatni_korish(vazifalar):
    lst = vazifa.royxat(vazifalar)
    if not lst:
        print("Ro'yxat bo'sh.")
        return
    for i, v in enumerate(lst, start=1):
        print(f"{i}. {v}")

def vazifa_ochirish(vazifalar):
    if not vazifa.royxat(vazifalar):
        print("O'chirish uchun vazifa yo'q.")
        return
    royxatni_korish(vazifalar)
    raqam_str = input("O'chirish uchun vazifa raqamini kiriting: ").strip()
    if not raqam_str.isdigit():
        print("❗ Faqat raqam kiriting.")
        return
    raqam = int(raqam_str)
    if vazifa.ochirish(vazifalar, raqam):
        print("🗑️ Vazifa o'chirildi.")
    else:
        print("❗ Bunday raqamli vazifa yo'q.")

if __name__ == "main":
    vazifalar = vazifa.yuklash()
    while True:
        menyu()
        tanlov = input("Tanlovingizni kiriting: ")
        if tanlov == "1":
            vazifa_qoshish(vazifalar)
        elif tanlov == "2":
            royxatni_korish(vazifalar)
        elif tanlov == "3":
            vazifa_ochirish(vazifalar)
        elif tanlov == "0":
            vazifa.saqlash(vazifalar)
            print("Vazifalar saqlandi. Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov.")