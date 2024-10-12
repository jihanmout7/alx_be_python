class Book:
        """
        A class representing a book with title, author, and publication year.
        """

        def __init__(self, title, author, year):
            """
            Initializes a Book instance with the provided title, author, and year.
            """
            self.title = title
            self.author = author
            self.year = year

        def __str__(self):
            """
            Returns a string representation of the book in the format "(title) by (author), published in (year)".
            """
            return f"{self.title} by {self.author}, published in {self.year}"

        def __repr__(self):
            """
            Returns a string that can be used to recreate the Book instance.
            """
            return f"Book('{self.title}', '{self.author}', {self.year})"

        def __del__(self):
            """
            Prints a message indicating the book is being deleted. (Destructor)
            **Note:** Destructors are not guaranteed to be called in Python.
            """
            print(f"Deleting {self.title}")

    # Example usage
    # my_book = Book("1984", "George Orwell", 1949)
    # print(my_book)
    # print(repr(my_book))

