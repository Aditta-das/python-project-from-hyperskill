class Library:
    def __init__(self, list_of_books, library_name):
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        for books in self.list_of_books:
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index} {books}")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        print(f"book added")

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        print("Deleted")

    def lend_book(self, book_name, author):
        if book_name in self.list_of_books:
            if self.lend_data[book_name] is None:
                self.lend_data[book_name] = author
            else:
                print(f"Book landed by {self.lend_data[book_name]}")
        else:
            print(f"Sorry type is not right")


    def ret_book(self, book_name, author):
        if book_name in self.list_of_books:
            if self.lend_data[book_name] is not None:
                self.lend_data.pop(book_name)
                self.lend_data[book_name] = book_name
                print(f"Book return Confirm {self.lend_data[book_name]}")
            else:
                print(f"Sorry this book is not landed")
        else:
            print("Wrong typing")


def main():
    list_books = ["ABC", "BCD", "JKL", "TYU", "POU"]
    library_name = "nishad"
    code_no = "474700"
    nishad = Library(list_books, library_name)
    print(f"{nishad.library_name} welcome you\nPRESS d to Display Book\nPress del to Delete\nPress a to Add Book\nPress l to Lend Books\nPress r to Return Books\nPress q to Quit")
    exit = False
    while exit != True:
        add = input()
        if add == "q":
            print(f"Bye, See You Again")
            exit = True

        elif add == "d": 
            nishad.display_books()

        elif add == "a":
            new_book = input("What's your book name: ")
            nishad.add_book(new_book)

        elif add == "del":
            type_code = input("Enter The Secret Code: ")
            if type_code == code_no:
                del_book = input("Enter Name of Your Book To DELETE: ")
                nishad.delete_book(del_book)
            else:
                print(f"This right is reseerved by admin")

        elif add == "l":
            lend_auth = input("Whats your name: ")
            lend = input("book name: ")
            nishad.lend_book(lend, lend_auth)

        elif add == "r":
            lend_auth = input("Whats your name: ")
            ret = input("Book name: ")
            nishad.ret_book(ret, lend_auth)



if __name__ == "__main__":
    main()