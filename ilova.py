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