class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_user(self, name, email, user_books=[]):
        if email in self.users:
            print ("User {} already exists.".format(email))
            return()
        self.users[email] = User(name, email)
        for book in user_books:
            self.add_book_to_user(book, email)

    def check_isbn_exists(self, isbn):
        isbn_list = [book.get_isbn() for book in self.books.keys()]
        return (isbn in isbn_list)

    def create_book(self, title, isbn):
        if self.check_isbn_exists(isbn):
            print("Book with isbn {} already exists.".format(isbn))
        else:
            return (Book(title, isbn))

    def create_novel(self, title, author, isbn):
        if self.check_isbn_exists(isbn):
            print("Book with isbn {} already exists.".format(isbn))
        else:
            return (Fiction(title, author, isbn))


    def create_non_fiction(self, title, subject, level, isbn):
        if self.check_isbn_exists(isbn):
            print("Book with isbn {} already exists.".format(isbn))
        else:
            return (Non_Fiction(title, subject, level, isbn))

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            user = self.users[email]
        else:
            print("No user with the email {}!".format(email))
            return ()

        user.read_book(book, rating)
        if rating:
            book.add_rating(rating)
        if book in self.books:
            self.books[book] = self.books[book] + 1
        else:
            self.books[book] = 1

    def print_catalog(self):
        print("\nTomeRater Current Catalog of Books")
        [print("\t{}".format(book)) for book in self.books.keys()]


    def print_users(self):
        print("\nTomeRater Current List of Users")
        [print("\t{}".format(user)) for user in self.users.keys()]

    def get_most_read_book(self):
        max_read = max(self.books.values())
        max_read_books = []
        for book, times_read in self.books.items():
            if (times_read == max_read):
                max_read_books.append(book)
        return (max_read_books)

    def highest_rated_book(self):
        max_rated_book = []
        max_rating = max([book.get_average_rating() for book in self.books.keys()])
        for book in self.books.keys():
            if book.get_average_rating() == max_rating:
                max_rated_book.append(book)
        return (max_rated_book)

    def most_positive_user(self):
        most_positive_users= []
        max_rating = max([user.get_average_rating() for user in self.users.values()])
        for user in self.users.values():
            if user.get_average_rating() == max_rating:
                most_positive_users.append(user)
        return (most_positive_users)


class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return (self.email)

    def change_email(self, address):
        self.email = address

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        try:
            return (sum({value for (key, value) in self.books.items() if value != None})/float(len(self.books)))
        except ZeroDivisionError:
            return (0)

    def __repr__(self):
        if len(self.books) > 0:
            return ("{}, email {}, has read {} books.".format(self.name, self.email, str(len(self.books))))
        else:
            return ("{}, email {}, has not read any books.".format(self.name, self.email))

    def __eq__(self, other_user):
        if (self.name == other_user.name) & (self.email == other_user.email):
            return True
        else:
            return False

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings=[]

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return (self.title)

    def get_isbn(self):
        return (self.isbn)

    def set_isbn(self, isbn):
        print("Somebody messed up, changing ISBN from {} to {}".format(str(self.isbn), isbn))
        self.isbn = isbn

    def add_rating(self, rating):
        if 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print ("Rating of {} is not valid".format(str(rating)))

    def get_average_rating(self):
        return (sum([num for num in self.ratings])/float(len(self.ratings)))

    def __repr__(self):
        return ("{} with isbn {}".format(self.title, self.isbn))

    def __eq__ (self, other_book):
        if (self.isbn == other_book.isbn) & (self.title == otehr_book.title):
            return True
        else:
            return False

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return (self.author)

    def __repr__(self):
        return ("{} by {}".format(self.title, self.author))


class Non_Fiction(Book):
    
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return (self.subject)

    def get_level(self):
        return (self.level)

    def __repr__(self):
        if (self.level[0].lower() == "a"):
            return ("{}, an {} manual on {}".format(self.title, self.level, self.subject))
        else:
            return ("{}, a {} manual on {}".format(self.title, self.level, self.subject))
    
