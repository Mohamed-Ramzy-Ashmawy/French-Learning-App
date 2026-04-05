import json
from vocab import VocabularyItem


with open("words.json") as f:
    data = json.load(f)
    
    vlist = []

    for item in data:
        word = VocabularyItem(
            item["Eng_word"],
            item["Fr_word"],
            item["Indef_Article"],
            item["Def_Article"]
        )
        vlist.append(word)