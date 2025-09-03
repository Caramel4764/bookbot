from stats import get_book_text
from stats import word_count

def main():
  #print(get_book_text("./books/frankenstein.txt"))
  book_content = get_book_text("./books/frankenstein.txt")
  print(f"{word_count(book_content)} words found in the document")
main()