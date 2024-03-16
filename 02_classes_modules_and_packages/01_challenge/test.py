import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    data = [
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    ]

    def setUp(self) -> None:
        self.library = Library()
        return super().setUp()

    def test_add_book(self):
        book = self.data[0]

        self.library.add_book(
            title=book["title"],
            author=book["author"],
        )

        books = self.library.retrieve_books()

        self.assertEqual(books[0]["title"], book["title"])
        self.assertEqual(books[0]["author"], book["author"])

    def test_remove_book(self):
        """Note: No error handling is expected."""
        book = self.data[0]

        self.library.add_book(
            title=book["title"],
            author=book["author"],
        )

        self.library.remove_book(book["title"])

        self.assertEqual(len(self.library.retrieve_books()), 0)

    def test_retrieve_books(self):
        self.assertEqual(len(self.library.retrieve_books()), 0)

        for book in self.data:
            self.library.add_book(
                title=book["title"],
                author=book["author"],
            )

        books = self.library.retrieve_books()

        self.assertEqual(len(books), len(self.data))

        for i, book in enumerate(books):
            self.assertEqual(book["title"], self.data[i]["title"])
            self.assertEqual(book["author"], self.data[i]["author"])

    def tearDown(self) -> None:
        self.library = None
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
