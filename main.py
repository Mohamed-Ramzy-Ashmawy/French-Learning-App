import utils
import loader

vlist = loader.vlist #vlist is a list of objects based on the VocabularyItem class in vocab.py. Each object is a word, noun phrase, adverb, Interjection / Locution, etc...

while True: 
    inp = input("\nWelcome to the French training app. What are you up to today?"
    "(n = take test | s = show words | q = quit): ")

    if inp == "n":
        utils.take_test(inp, vlist)
    elif inp == "s":
        utils.show_vlist(vlist)
    elif inp == "q":
        break
    else:
        print("\nInvalid input. Try again: ")
        continue