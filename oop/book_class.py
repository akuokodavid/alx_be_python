# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous string representation (used for debugging)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
