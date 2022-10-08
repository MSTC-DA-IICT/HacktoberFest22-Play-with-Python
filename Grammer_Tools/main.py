import spacy
npl=spacy.load("en_core_web_sm")

def get_text(text):
    print(text)
    global doc
    doc = npl(text)

def find_noun():
    for x in doc:
        if x.pos_=="NOUN":
            print(x)

#create more functionality using space like find pronoun, adverbs etc.