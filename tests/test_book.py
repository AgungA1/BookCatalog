import unittest
from books.book import Book

class TestBook(unittest.TestCase):
    def test_book_attributes(self):
        book = Book("Python Programming", "John Doe", 2022)
        self.assertEqual(book.title, "Python Programming")
        self.assertEqual(book.author, "John Doe")
        self.assertEqual(book.year, 2022)

if __name__ == '__main__':
    unittest.main()
