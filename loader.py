from json import load
from vocab import VocabularyItem

# The file makes VocabularyItem objects from words.json
with open("words.json") as f:
    data = load(f)
    
    vlist = []

    for item in data:
        word = VocabularyItem(
            item["Eng_word"],
            item["Fr_word"],
            item["Indef_Article"],
            item["Def_Article"]
        )
        vlist.append(word)