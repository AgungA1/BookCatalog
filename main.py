import json
from books.book import Book

class BookCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def save_books_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)

    def load_books_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                self.books.append(Book(item['title'], item['author'], item['year']))


if __name__ == "__main__":
    catalog = BookCatalog()
    catalog.load_books_from_file('data/books.json')

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Simpan dan Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            title = input("Masukkan judul buku: ")
            author = input("Masukkan nama penulis: ")
            year = input("Masukkan tahun terbit: ")
            catalog.add_book(title, author, year)
            print("Buku berhasil ditambahkan!")

        elif pilihan == "2":
            title = input("Masukkan judul buku yang ingin dicari: ")
            book = catalog.search_book(title)
            if book:
                print("Buku ditemukan:")
                print(f"Judul: {book.title}")
                print(f"Penulis: {book.author}")
                print(f"Tahun Terbit: {book.year}")
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == "3":
            catalog.save_books_to_file('data/books.json')
            print("Data buku telah disimpan.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
