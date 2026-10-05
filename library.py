import datetime 
import time 

class Book: 
  ID = 1
  def __init__(self, title: str = "Unknown", author: str = "Unknown", genre: str = "Default", publication_date: datetime.date =  None,
                stars: int = 5, isCheckedOut: bool = False, status: str = "Perfect", returnDate: datetime.date = None, 
                onPreOrder: bool = False, language: str = "EN", pages: int = None, link: str = None, words: int = None, book_type: str = None, statistics: dict = {}, 
                last_read_date: datetime.date = None):
    self.author = author
    self.genre = genre
    self.title = title
    self.publication_date = publication_date
    self.stars = stars 
    self.isCheckedOut = isCheckedOut
    self.status = status 
    self.returnDate = returnDate
    self.onPreOrder = onPreOrder
    self.language = language
    self.pages = pages
    self.link = link 
    self.num_words = words
    self.book_type = book_type
    self.statistics = statistics
    self.last_read_date = last_read_date
    self.ID = f"B{Book.ID:04d}";
    Book.ID += 1;  
  def __str__(self):
    return self.title
  def display_stars(self) -> None:
    print(self.stars * "\u2605")    
  def read(self):
    import textwrap
    import shutil 
    with open(self.link, "r") as file:
      for line in file: 
        print(textwrap.fill(line, width= shutil.get_terminal_size().columns))
        time.sleep(0.5);
  def have_audio_book_read(self):
    if self.link is not None and testLink(self.link):
      import pyttsx3
      with open(self.link, "r") as file:
        engine = pyttsx3.init();
        for line in file:
          engine.say(line)
          engine.runAndWait()
          time.sleep()



  
class Library:
  def __init__(self, name: str, availableBooks: list[Book], catalog: list[Book]):
    self.name = name
    self.AvailableBooks = availableBooks
    self.catalog = catalog
    self.numBooks = len(self.catalog)
  def insert(self, book: Book) -> None:
    if not book in self.catalog:
      self.catalog.append(book)
      self.AvailableBooks.append(book);
    else:
      print(f"The book: {book.title} is already in the library")
  def checkout(self, book: Book) -> None:
    if book in self.AvailableBooks:
      self.AvailableBooks.remove(book);
      book.isCheckedOut = True
      print(f"You have checked out {book.title} by {book.author} on {datetime.date.today()}. ")
    elif book in self.catalog:
      if book.isCheckedOut: 
        print(f"{book.title} is already checked out. ");
      else:
        print(f"{book.title} is not currently available. ");
    else:
      print(f"{book.title} is not in this library. ");
  def checkStatusOfBook(self, book: Book):
    return book.isCheckedOut;     
  def search(self, book, attribute: str, matches):
    return [book for book in self.catalog if matches(getattr(book, attribute))]    
  def statistics(self, book: Book):
    pass;
  def __str__(self):
    return self.name
  
class Person:
  names = set();
  def __init__(self, name: str = "John Doe", books: list[Book] = None, membership: bool = False, books_on_preorder: list[Book] = None, email: str = None):
    if name in Person.names:
      raise ValueError(f"Name {name} is already taken. ");
    self.name = name
    Person.names.add(name);
    self.checked_out_books = books
    self.library_member = membership 
    self.books_on_preorder = books_on_preorder
    self.email = email 
  def check_out_book(self, book: Book, library: Library):
      if book in library.AvailableBooks:
        library.AvailableBooks.remove(book);
        book.isCheckedOut = True
      elif book in library.catalog and book.isCheckedOut == True:
          print(f"The book is checked out; however, the return date of book: {book.title} is {book.returnDate}");
          print(f"Would you like to pre-order {book.title}, Yes or No?")
          val = input("Would you like to preorder? Yes or No: ").strip().upper()
          while val != "YES" and val != "NO":
           print("Your input is not valid, try again.")
           val = input("Would you like to preorder? Yes or No: ").strip().upper()
          if val == "YES":
            self.preOrder(book, library);
            exit
          else: 
            print(f"Understood, we will not preorder book: {book.title}")

      if self.library_member == True:
        book.returnDate = datetime.date.today() + datetime.timedelta(days = 30);
        print(f"SYSTEM: Person: {self.name} checked out book: TITLE {book.title}, on {datetime.date.today()} and must return it on {book.returnDate}. ");
      else:
        book.returnDate = datetime.date.today() + datetime.timedelta(days = 14);
        print(f"SYSTEM: Person: {self.name} checked out book: TITLE {book.title}, on {datetime.date.today()} and must return it on {book.returnDate}. ");
  def preOrder(self, book: Book, library: Library):
    if book in library.catalog and book not in library.AvailableBooks:
      loadingDots("Executing");
      print(f"Complete. {self.name} has preordered book: {book.title}.");
      book.onPreOrder = True
      if self.books_on_preorder is None:
        self.books_on_preorder = [book.title]
      else:
        self.books_on_preorder.append(book.title); 
    else:
      print("Either the book is already in our library or we don't offer this book, go visit our website.")

def loadingDots(word: str) -> None:
  for i in range(10):
    dots = "." * (i % 4)
    print(f"{word}{dots} ", end = "\r");
    time.sleep(0.5);

def testLink(link: str) -> bool:
  try: 
    with open(link, "r") as f:
      return True
  except:
    print(f"An error occurred when opening this link: {link}.")
    return False;
    

if __name__ == "__main__":  
  pass;