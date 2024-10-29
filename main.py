def main():
    with open("bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def wordcount():
    book = main()
    words = book.split()
    count = len(words)
    return count

def characters():
    book = main()
    chars = {}
    for letter in book:
        chars[letter.lower()] = int(0)
    for letter in book:
        chars[letter.lower()] += 1
    return(chars)

def report():
    chars = characters()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount()} words found in the document\n")
    for i in chars:
        print(f"The {i} character was found {chars[i]} times")
    print("--- End report ---")

report()