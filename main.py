import utils
import loader
import questionary

vlist = loader.vlist #vlist is a list of objects based on the VocabularyItem class in vocab.py. Each object is a word, noun phrase, adverb, Interjection / Locution, etc...

while True:
    #questionary.select handles the prompt and the arrows
    choice = questionary.select(
        "Welcome to the French training app. What are you up to today?",
        choices=[
            "Take test",
            "Show words",
            "Quit"
        ]
    ).ask()

    #If the user hits Ctrl+C, choice becomes None. This prevents a crash.
    if choice is None:
        break

    if choice == "Take test":
        #Passing "n" to keep existing utils logic compatible
        utils.take_test("n", vlist)
        
    elif choice == "Show words":
        utils.show_vlist(vlist)
        
    elif choice == "Quit":
        print("Au revoir!")
        break