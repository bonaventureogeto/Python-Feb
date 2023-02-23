book = {
    "title": "The Great Gatsby",
    "Author": "F. Scott Fitzgerald",
    "ISBN": "978-3-16-148410-0",
    "Price": "Ksh. 1,000",
}


def books(filename):
    with open(filename, "r") as list:
        for dictionary in list:
            first_dict = dictionary[0]
            print(first_dict["title"])
            print(len(dictionary))

books("books.txt")