class VocabularyItem:
    def __init__(self, Eng_word, Fr_word, Indef_Article, Def_Article):
        self.Eng_word = Eng_word
        self.Fr_word = Fr_word
        self.Indef_Article = Indef_Article
        self.Def_Article = Def_Article

        article = Def_Article or Indef_Article
        self.ans = f"{article} {Fr_word}" if article else Fr_word
        #The two previous lines ensure that the answer (`ans`) doesn't have a space at its start by assigning an article to `ans` if the answer is a noun phrase. 
        #Else, the answer simply equals the French word (`Fr_word`)
        
