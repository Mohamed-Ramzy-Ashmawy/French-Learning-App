from vocab import VocabularyItem
from random import choice

def take_test(inp, vlist):
    words_used = []
    w = None
    while inp != 'q':
        if inp != 'n':
            print("Invalid input..")
            inp = input("Enter(n/q): ")
            continue
        
        if len(vlist) == len(words_used):
            words_used.clear()
        
        w = choice(vlist)
        while w in words_used:
            w = choice(vlist)
        
        words_used.append(w)
        user_ans = input(f"{w.Eng_word}: ").strip()

        if user_ans != w.ans:
            print(f"WRONG! It's {w.ans}")
        else:
            print("YOU'RE GODDAMN RIGHT!")
        
        inp = input("What's next?(n/q): ").strip()

def show_vlist(vlist):
    for item in vlist:
        print(f"\nEnglish word: {item.Eng_word}\nFrench noun phrase: {item.ans}")

    print(f"\nThere are {len(vlist)} items..")

