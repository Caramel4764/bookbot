def get_book_text(file_path):
  with open(file_path) as f:
    # do something with f (the file) here
      # f is a file object
    file_contents = f.read()
    return file_contents
def word_count(text):
  return len(text.split())