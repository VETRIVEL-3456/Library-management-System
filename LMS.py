library = []
users = []
borrowed_books = {}


def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print(f"'{book}' added successfully!\n")


def view_books():
    if len(library) == 0:
        print("No books available.\n")
    else:
        print("\nAvailable Books:")
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book}")
        print()


def remove_book():
    book = input("Enter book name to remove: ")

    if book in library:
        library.remove(book)
        print(f"'{book}' removed successfully!\n")
    else:
        print("Book not found.\n")


def add_user():
    user = input("Enter user name: ")
    users.append(user)
    print(f"User '{user}' added successfully!\n")


def view_users():
    if len(users) == 0:
        print("No users registered.\n")
    else:
        print("\nRegistered Users:")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user}")
        print()


def lend_book():
    user = input("Enter user name: ")
    book = input("Enter book name to lend: ")

    if user not in users:
        print("User not found.\n")

    elif book not in library:
        print("Book not available.\n")

    else:
        library.remove(book)
        borrowed_books[book] = user
        print(f"'{book}' lent to {user} successfully!\n")


def return_book():
    book = input("Enter book name to return: ")

    if book in borrowed_books:
        user = borrowed_books[book]
        library.append(book)
        del borrowed_books[book]

        print(f"'{book}' returned successfully by {user}!\n")

    else:
        print("This book was not borrowed.\n")


def view_borrowed_books():
    if len(borrowed_books) == 0:
        print("No borrowed books.\n")

    else:
        print("\nBorrowed Books:")
        for book, user in borrowed_books.items():
            print(f"{book} --> Borrowed by {user}")
        print()


while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Add User")
    print("5. View Users")
    print("6. Lend Book")
    print("7. Return Book")
    print("8. View Borrowed Books")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        remove_book()

    elif choice == "4":
        add_user()

    elif choice == "5":
        view_users()

    elif choice == "6":
        lend_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        view_borrowed_books()

    elif choice == "9":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please try again.\n")
