import spacy
from collections import Counter

npl=spacy.load("en_core_web_sm")

def get_text(text):
    global doc
    doc = npl(text)

#Parts of Speech Finder

#Noun
def find_noun():
    ans = []
    for x in doc:
        if x.pos_=="NOUN" or x.pos_=="PROPN":
            ans.append(x)
    return ans

#Pronoun
def find_pronoun():
    ans = []
    for x in doc:
        if x.pos_ == "PRON":
            ans.append(x)
    return ans

#Adverb
def find_adverbs():
    ans = []
    for x in doc:
        if x.pos_ == "ADV":
            ans.append(x)
    return ans

#Adjective
def find_adjectives():
    ans = []
    for x in doc:
        if x.pos_ == "ADJ":
            ans.append(x)
    return ans

#Verb
def find_verb():
    ans = []
    for x in doc:
        if x.pos_ == "VERB" or x.pos_ == "AUX":
            ans.append(x)
    return ans

#Preposition
def find_preposition():
    ans = []
    for x in doc:
        if x.pos_ == "ADP":
            ans.append(x)
    return ans

#Conjuction     
def find_conjuction():
    ans = []
    for x in doc:
        if x.pos_ == "CONJ" or x.pos_ == "SCON":
            ans.append(x)
    return ans

#Interjection
def find_interjection():
    ans = []
    for x in doc:
        if x.pos_ == "INTJ":
            ans.append(x)
    return ans

#Punctuation
def find_punctuation():
    ans = []
    for x in doc:
        if x.pos_ == "PUNCT":
            ans.append(x)
    return ans

#Articles/Determiners
def find_determiners():
    ans = []
    for x in doc:
        if x.pos_ == "DET":
            ans.append(x)
    return ans


#create more functionality using space like find pronoun, adverbs etc.