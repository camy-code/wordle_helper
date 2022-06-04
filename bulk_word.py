#we need these imports
import sys
import os


# the following reads a master lists and then returns the lists of all 5 letter words
# para - word_list - the file we are reading from 
def book(word_list = "world_list.txt"):
    if not(os.path.exists(word_list) ):
        sys.exit("read file does not exist")

    try: #clean up this file junk later
        reader = open(word_list, "r")
    except:
        sys.exit("Cannot find file")

    ls = list()
    for x in reader: # the following will do all of our file reading 
        if len(x.strip()) == 5:ls.append(x.strip())

    reader.close()
    return ls

# the following method simply writes all 5 letter words in a file
# para: paper - read file that we will call book method within
# para: pen - write file
def author(pen = "5_letter.txt", paper ="world_list.txt" ):
    ls = book(paper)
    if not(os.path.exists(pen) ):
        sys.exit("write file does not exist")

    try:
            writer = open(pen, "w")
    except:
        sys.exit("cannot find writer")
    for i in ls:
        try:
            writer.write(i + "\n")
        except:
            sys.exit("Error writing to file in author")
    writer.close()

# This function does all the writing and 
# reading for what we need from bulk_word.py
def do_everything(pen = "5_letter.txt", paper ="world_list.txt"):
    #5 letter text is the file we are writing 
    # world list is all the english letters
    author(pen,paper)

# we might not need this 
# def main():
#     author()
    
#     pass


# if __name__ == "__main__":
#     main()