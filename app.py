import json # for data save and load
import os # system operation and file handling

data_file = 'library.txt'
def load_library():
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file) 
        except json.JSONDecodeError:
            print("Error: Library file is corrupted. Starting with an empty library.")
            return[]
    return []

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")

    while True:
        year = input("Enter the year of the book: ")
        if year.isdigit():
            break
        print('Invalid year. Please enter a number.')
    genre = input("Enter the genre of the book: ")
    read = input("Have you read this book? (yes/no): ").lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' has been added to the library.")

def remove_book(library):
    title = input("Enter the title of the book to remove from the library: ") 
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' has been removed from the library.")
    else:
        print(f"Book {title} not found in the library.")

def search_library(library):
    search_by = input('Search by title or author: ').lower()

    if search_by not in ['title', 'author']:
        print("Invalid input. Please enter 'title' or 'author'.")
        return

    search_term = input(f'Enter the {search_by} to search for: ').lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\nSearch Results:")
        print("-" * 50)
        for book in results:
            status = '✅ Read' if book['read'] else '❌ Not Read'
            print(f"{book['title']} - {book['author']} ({book['year']}) - {status}")
        print("-" * 50)
    else:
        print(f"No book found matching '{search_term}' in the {search_by} field.")

def display_books(library):
    if library:
        print('\nLibrary Collection:')
        print('-' * 50)
        for book in library:
            status = '✅ Read' if book['read'] else '❌ Not Read'
            print(f"{book['title']} - {book['author']} ({book['year']}) - {status}")
        print('-' * 50)
    else:
        print('library is empty.')

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
        try:
            print("\n📚 Library Menu 📚")
            print('1. Add a book')
            print('2. Remove a book')
            print('3. Search the library')
            print('4. Display all books')
            print('5. Display statistics')
            print('6. Exit')

            choice = input('Enter your choice: ') 
            if choice == '1':
                add_book(library)
            elif choice == '2':
                remove_book(library)
            elif choice == '3':
                search_library(library)
            elif choice == '4':
                display_books(library)
            elif choice == '5':
                display_statistics(library)            
            elif choice == '6':
                print('Thank you for using the library! Have a great day!')
                break
            else:
                print('Invalid choice. Please try again')
        except KeyboardInterrupt:
            print("\nExiting program. Goodbye! 😊")
            break

if __name__ == '__main__':
    main()