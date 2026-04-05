class VocabularyItem:
    def __init__(self, Eng_word, Fr_word, Indef_Article, Def_Article):
        self.Eng_word = Eng_word
        self.Fr_word = Fr_word
        self.Indef_Article = Indef_Article
        self.Def_Article = Def_Article
        article = Def_Article or Indef_Article
        self.ans = f"{article} {Fr_word}" if article else Fr_word 
        
