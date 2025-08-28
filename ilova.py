def menyu():
    print("\n--- Vazifalar ilovasi ---")
    print("1 - Vazifa qo'shish")
    print("2 - Ro'yxatni ko'rish")
    print("3 - Vazifani o'chirish")
    print("0 - Chiqish")

if __name__ == "__main__":
    while True:
        menyu()
        tanlov = input("Tanlovingizni kiriting: ")
        if tanlov == "0":
            print("Dastur yakunlandi.")
            break
        else:
            print("Bu bosqichda funksiyalar hali yoqilmagan.")



vazifalar = []

def menyu():
    print("\n--- Vazifalar ilovasi ---")
    print("1 - Vazifa qo'shish")
    print("2 - Ro'yxatni ko'rish")
    print("3 - Vazifani o'chirish")
    print("0 - Chiqish")

def vazifa_qoshish():
    matn = input("Yangi vazifani kiriting: ")
    vazifalar.append(matn)
    print("✅ Vazifa qo'shildi.")

def royxatni_korish():
    if not vazifalar:
        print("Ro'yxat bo'sh.")
        return
    for i, v in enumerate(vazifalar, start=1):
        print(f"{i}. {v}")

if __name__ == "__main__":
    while True:
        menyu()
        tanlov = input("Tanlovingizni kiriting: ")
        if tanlov == "1":
            vazifa_qoshish()
        elif tanlov == "2":
            royxatni_korish()
        elif tanlov == "3":
            print("O'chirish keyingi bosqichda yoqiladi.")
        elif tanlov == "0":
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov.")
