FAYL_NOMI = "malumotlar.txt"

def yuklash(fayl=FAYL_NOMI):
    try:
        with open(fayl, "r", encoding="utf-8") as f:
            return [q.rstrip("\n") for q in f]
    except FileNotFoundError:
        return []

def saqlash(vazifalar, fayl=FAYL_NOMI):
    with open(fayl, "w", encoding="utf-8") as f:
        for v in vazifalar:
            f.write(v + "\n")

def qoshish(vazifalar, matn):
    matn = (matn or "").strip()
    if not matn:
        return False
    vazifalar.append(matn)
    return True

def royxat(vazifalar):
    return list(vazifalar)

def ochirish(vazifalar, raqam):
    if 1 <= raqam <= len(vazifalar):
        vazifalar.pop(raqam - 1)
        return True
    return False