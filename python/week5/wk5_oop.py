class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def describe (self):
            print(f"This book is '{self.title}' by {self.author}")
        
#Child class using inheritance
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        
    def download(self):
        print(f"Downloading '{self.title}' by {self.author} of size {self.file_size}MB")
# Creating instances of the classes
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book1.describe()

book2 = EBook("1984", "George Orwell", 1.5)
book2.describe()
book2.download()