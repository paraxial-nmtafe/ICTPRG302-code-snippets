books = [
    {
        "title": "All Systems Red",
        "author": "Martha Wells",
        "genre": "SciFi",
        "rating": 5,
        "status": "read"
    }
]

program_running = True

def print_menu():
    print("Welcome to Your Reads")
    print("===========================")
    print("Q to quit")
    print("S to show all books")
    print("A to add a book")
    print("===========================")

def show_all_books():
    print()
    for book in books:
        print("[" + book['status'].upper() + "] " + book['title'] + " by " + book['author'] + " rated: " + str(book.get('rating', 0)))
    print()

def add_a_book():
    new_book = {}
    detail_list = []
    while len(detail_list) != 3:
        raw_input = input("Please enter your book (title,author,genre): ")
        detail_list = raw_input.split(",")
    print("[DEBUG]", detail_list)
    new_book['title'] = detail_list[0]
    new_book['author'] = detail_list[1]
    new_book['genre'] = detail_list[2]

    while True:
        rating = input("What would you rate this book (0-5) ")
        print("[DEBUG]", rating, rating.isdigit())
        if rating.isdigit():
            rating = int(rating)
            if rating < 0 or rating > 5:
                continue
            new_book['rating'] = rating
            break

    status = ''
    while status not in ['read', 'want-to-read', 'gave-up']:
        status = input("Have you read the book (read, want-to-read, gave-up) ")

    new_book['status'] = status
    return new_book

while program_running:
    print_menu()
    user_input = input("Choose from the menu: ").upper()
    if user_input == "Q":
        program_running = False

    if user_input == "S":
        show_all_books()

    if user_input == "A":
        books.append(add_a_book())