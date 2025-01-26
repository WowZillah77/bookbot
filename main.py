# functions 

#function that count the number of words in a String
def wordscount(text_content):
    word_list = []
    word_list = text_content.split()
    return len(word_list)

##function that count the occurences of the different symbols in the String
def charCount(tex_content):
    resultDict = {}
    text_lowered = tex_content.lower()
    for symbol in text_lowered:
        if symbol in resultDict:
            count = resultDict[symbol]
            count +=1
            resultDict[symbol] = count
        else:
            resultDict[symbol] = 1
    return resultDict
# function that print the report(only Alpha characters)
def report(fcontents):
    print("--- Begin report of books/frankenstein.txt ---")
    count = wordscount(fcontents)
    dictionary = charCount(fcontents)
    print(f"{count} words found in the document")
    print("")
    for index in sorted(dictionary, key=dictionary.get, reverse=True):
        if index .isalpha():
            print(f"The '{index}' character was found {dictionary[index]} times")
    print("--- End report ---")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    report(file_contents)
