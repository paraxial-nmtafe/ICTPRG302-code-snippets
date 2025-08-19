all_books = [{
    "title": "All Systems Red",
    "author": "Martha Wells",
    "genre": "SciFi",
    "rating": 5,
    "status": "read", # want-to-read; gave-up
}]
app_running = True

def print_menu():
    print("Welcome to YourReads")
    print("====================")
    print("q to Quit")
    print("s to Show all books")
    print("a to Add a book")
    print("====================")
    print()

def print_all_books():
    print()
    for book in all_books:
        print("[" + book["status"].upper() + "] " + book["title"] + ", by " + book["author"])
    print()

def add_a_book():
    new_book = {}
    split_information = []
    while len(split_information) != 3:
        print("Enter your book in the format:")
        print("title;author;genre")
        combined_input = input("Your book?\n")
        split_information = combined_input.split(";")

    new_book["title"] = split_information[0]
    new_book["author"] = split_information[1]
    new_book["genre"] = split_information[2]
    rating = -1
    while rating < 1 or rating > 5:
        rating = int(input("What would you rate this book? (1-5) "))

    new_book["rating"] = rating
    status = ""
    while status not in ["read", "want-to-read", "gave-up"]:
        status = input("What's your reading status?(read, want-to-read, gave-up) ").lower()

    new_book["status"] = status

    return new_book

while app_running:
    print_menu()
    menu_choice = input("What do you want to do? ").lower()

    if (menu_choice == 'q'):
        app_running = False
    if (menu_choice == 's'):
        print_all_books()
    if (menu_choice == 'a'):
        all_books.append(add_a_book())
