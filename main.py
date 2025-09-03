from stats import get_book_text
from stats import word_count
from stats import count_character_instance
from stats import sorted_list
from stats import printPrettyCharacterReport
import sys

def main():
  #print(get_book_text("./books/frankenstein.txt"))
  if len(sys.argv)<=1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_content = get_book_text(sys.argv[1])
  letter_instance_dictionary = count_character_instance(book_content)
  print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
  print(f"Found {word_count(book_content)} total words")

  #print(letter_instance_dictionary)
  nice_list = (sorted_list(letter_instance_dictionary))
  printPrettyCharacterReport(nice_list)
  print("============= END ===============")
main()
