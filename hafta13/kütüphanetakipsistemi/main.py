import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_FILE = os.path.join(BASE_DIR, "kitaplar.txt")


def load_books():
    books = {}
    if not os.path.exists(DATA_FILE):
        return books

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = [part.strip() for part in line.split(",")]
            if len(parts) < 3:
                continue

            title = parts[0]
            author = parts[1]
            try:
                stock = int(parts[2])
            except ValueError:
                stock = 0

            books[title] = [author, stock]

    return books


def save_books(books):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for title, value in books.items():
            author, stock = value
            file.write(f"{title}, {author}, {stock}\n")


def show_books(books):
    if not books:
        print("Dosyada henüz kitap kaydı yok.")
        return

    print("\nKütüphanedeki kitaplar:")
    for title, (author, stock) in books.items():
        print(f"- {title} | Yazar: {author} | Stok: {stock}")
    print()


def add_book():
    books = load_books()
    title = input("Eklemek istediğiniz kitabın adını giriniz: ").strip()
    if not title:
        print("Kitap adı boş olamaz.")
        return

    author = input("Kitabın yazarını giriniz: ").strip()
    try:
        stock = int(input("Kitabın stok sayısını giriniz: ").strip())
    except ValueError:
        print("Stok sayısı tam sayı olmalıdır.")
        return

    if title in books:
        books[title][1] += stock
        print(f"{title} kitabının stoğu {stock} adet artırıldı.")
    else:
        books[title] = [author, stock]
        print(f"{title} kitabı kaydedildi.")

    save_books(books)


def decrease_stock():
    books = load_books()
    if not books:
        print("Kitap listesi boş; önce kitap ekleyin.")
        return

    show_books(books)
    title = input("Stoktan düşmek istediğiniz kitabın adını giriniz: ").strip()
    if title not in books:
        print(f"{title} adlı kitap bulunamadı.")
        return

    author, stock = books[title]
    if stock <= 0:
        print(f"{title} kitabının stokta yeterli adedi yok.")
        return

    books[title][1] = stock - 1
    save_books(books)
    print(f"{title} kitabının stoğu güncellendi. Kalan stok: {books[title][1]}")


def main():
    while True:
        print("\nKütüphane takip sistemine hoş geldiniz!")
        print("1 - Kitap kaydını göster")
        print("2 - Kitap ekle")
        print("3 - Kitap stoğunu azalt")
        print("4 - Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            show_books(load_books())
        elif choice == "2":
            add_book()
        elif choice == "3":
            decrease_stock()
        elif choice == "4":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
