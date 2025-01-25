# functions 
def wordscount(text_content):
    word_list = []
    word_list = text_content.split()
    return len(word_list)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(wordscount(file_contents))

