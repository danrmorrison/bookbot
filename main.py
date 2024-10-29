def main():
    with open("bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def wordcount():
    book = main()
    words = book.split()
    count = len(words)
    return count

print(wordcount())