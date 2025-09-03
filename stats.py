def get_book_text(file_path):
  with open(file_path) as f:
    # do something with f (the file) here
      # f is a file object
    file_contents = f.read()
    return file_contents
def count_character_instance(text):
  text = text.lower()
  instance_counter = {}
  #check if character exists, if not add dictionary, otherwise counter 1
  for i in range(0, len(text)):
    curr_letter = text[i:i+1]
    if curr_letter not in instance_counter and curr_letter!=" ":
      instance_counter[curr_letter]=1
    else:
      for letter in instance_counter:
        if (curr_letter == letter):
          instance_counter[letter]+=1
  return instance_counter
def word_count(text):
  return len(text.split())
def sorted_list(instance_dictionary):
  sorted_list = []
  for letter in instance_dictionary:
    sorted_list.append({"char":letter, "num": instance_dictionary[letter]})
  sorted_list.sort(key=return_num_key, reverse=True)
  return sorted_list
def return_num_key(char):
  return char["num"]
def printPrettyCharacterReport(sorted_list):
  print("--------- Character Count -------")
  for char in sorted_list:
    if (char["char"].isalpha()):
      print(f"{char['char']}: {char['num']}")
