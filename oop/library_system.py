class Book:
  """
  Base class representing a book with title and author.
  """
  def __init__(self, title, author):
    self.title = title
    self.author = author

class EBook(Book):
  """
  Derived class representing an EBook with additional file size attribute.
  """
  def __init__(self, title, author, file_size):
    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size

class PrintBook(Book):
  """
  Derived class representing a PrintBook with additional page count attribute.
  """
  def __init__(self, title, author, page_count):
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

class Library:
  """
  Class representing a library that manages a collection of books.
  """
  def __init__(self):
    self.books = []

  def add_book(self, book):
    """
    Adds a Book, EBook, or PrintBook instance to the library collection.
    """
    if isinstance(book, Book):
      self.books.append(book)
    else:
      print("Invalid book type. Only Book, EBook, or PrintBook allowed.")

  def list_books(self):
    """
    Prints details of each book in the library.
    """
    for book in self.books:
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
      else:
        print(f"Book: {book.title} by {book.author}")