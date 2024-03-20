#####################################################
# dict | task 4                                     #
#####################################################
# to do                                             #
#####################################################
# author, book title, genre, year of publication,   #
# number of pages, publisher.                       #
#####################################################
# Add, remove, find, change                         #
#####################################################
"""
Book_dict = {
    Author: {
        book_title: {
            genre: value,
            year_of_publication: value,
            number_of_pages: value,
            publisher: value
        }
    }
}
"""

Book_dict = {
    "F. Scott Fitzgerald": {
        "The Great Gatsby": {
            "genre": "Tragedy",
            "year of publication": "April 10, 1925",
            "number of pages": "208 pages",
            "publisher": "Charles Scribner's Sons"}}}

sub_key_list = ["genre", "year of publication", "number of pages", "publisher"]

for author in Book_dict.keys():
    print(f"\n{author}")
    for title in Book_dict[author].keys():
        print(f"\t{title}")
        for info in sub_key_list:
            print(f"\t\t{info}: {Book_dict[author][title][info]}")

print(f"\n{'This program can:{_add}{_remove}{_find}{_change}'}".format(
    _add=f"\n{'Add new info:':<19}1",
    _remove=f"\n{'Remove some info:':<19}2",
    _find=f"\n{'Find something:':<19}3",
    _change=f"\n{'Change anything:':<19}4"))

choice = input(f"\nEnter a number of the function what you want to use: ")
if choice.isnumeric():
    choice = int(choice)
match choice:
    case 1:
        add_word = input(f"Add new AUTHOR or info ABOUT existing author?\n").upper()
        match add_word:
            case "AUTHOR":
                author = input(f"Enter a new author: ")
                title = input(f"Enter a title of the book: ")
                Book_dict[author] = {title: {}}
                for i in sub_key_list:
                    Book_dict[author][title][i] = input(f"Enter {i}: ")
            case "ABOUT":
                author = input(f"Enter an author: ")
                title = input(f"Enter a new title: ")
                Book_dict[author].update({title: {}})
                for i in sub_key_list:
                    Book_dict[author][title][i] = input(f"Enter {i}: ")

    case 2:
        rem_word = input(f"Remove the whole AUTHOR or info ABOUT title?\n").upper()
        match rem_word:
            case "AUTHOR":
                author = input(f"Enter the author: ")
                print(Book_dict.pop(author, f"There are no \"{author}\""))
            case "ABOUT":
                author = input(f"Enter the author: ")
                if author in Book_dict.keys():
                    for i in Book_dict[author].keys():
                        print(i)
                    title = input(f"Enter the title: ")
                    rem = input(f"Delete the whole TITLE or info ABOUT title?").upper()
                    match rem:
                        case "TITLE":
                            print(Book_dict[author].pop(title, f"There are no \n{title}\n"))
                        case "ABOUT":
                            for i in Book_dict[author][title].keys():
                                print(i)
                            rem = input(f"Enter info to remove").lower()
                            for i in sub_key_list:
                                if i in rem:
                                    Book_dict[author][title].pop(i)
                else:
                    print(f"There are no {author}")

    case 3:
        find_word = input(f"Find AUTHOR, or TITLE?\n").upper()
        match find_word:
            case "AUTHOR":
                author = input(f"Enter the author: ")
                if author in Book_dict.keys():
                    print(f"Titles by {author}:")
                    for i in Book_dict[author].keys():
                        print(i)
            case "TITLE":
                title = input(f"Enter the title: ")
                k = 0
                for i in Book_dict.keys():
                    for j in Book_dict[i].keys():
                        if j.upper() in title.upper():
                            print(f"The author of {title} is {i}")
                            k = 1
                if k == 0:
                    print(f"There are no \"{title}\"")

    case 4:
        change = input(f"RENAME author or change info about TITLE?\n").upper()
        match change:
            case "RENAME":
                author = input(f"Enter the author: ")
                if author in Book_dict.keys():
                    new_title = input(f"Enter the new name: ")
                    Book_dict[new_title] = Book_dict[author].copy()
                    Book_dict.pop(author)
                else:
                    print(f"There are no {author}")
            case "TITLE":
                author = input(f"Enter the author: ")
                for i in Book_dict[author].keys():
                    print(i)
                title = input(f"Enter the title: ")
                if title in Book_dict[author].keys():
                    change = input(f"Rename TITLE or change info ABOUT?\n").upper()
                    match change:
                        case "TITLE":
                            new_title = input(f"Enter a new name of title: ")
                            Book_dict[author][new_title] = Book_dict[author][title].copy()
                            Book_dict[author].pop(title)
                        case "ABOUT":
                            for i in Book_dict[author][title]:
                                print(i)
                            change = input(f"Which info do you wanna change?\n")
                            change = change.split(",")
                            for i in sub_key_list:
                                for j in change:
                                    if j.strip().lower() in i:
                                        Book_dict[author][title][i] = input(f"Enter a new {i}: ")
                else:
                    print(f"There are no {title}")

for author in Book_dict.keys():
    print(f"\n{author}")
    for title in Book_dict[author].keys():
        print(f"\n\t{title}")
        for info in sub_key_list:
            print(f"\t\t{info}: {Book_dict[author][title][info]}")
input()
