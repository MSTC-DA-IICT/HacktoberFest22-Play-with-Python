import spacy
from collections import Counter

npl=spacy.load("en_core_web_sm")

def get_text(text):
    print(text)
    global doc
    doc = npl(text)

#Parts of Speech Finder

#Noun
def find_noun():
    for x in doc:
        if x.pos_=="NOUN" or x.pos_=="PROPN":
            print(x)

#Pronoun
def find_pronoun():
    for x in doc:
        if x.pos_ == "PRON":
            print(x)

#Adverb
def find_adverbs():
    for x in doc:
        if x.pos_ == "ADV":
            print(x)

#Adjective
def find_adjectives():
    for x in doc:
        if x.pos_ == "ADJ":
            print(x)

#Verb
def find_verb():
    for x in doc:
        if x.pos_ == "VERB" or x.pos_ == "AUX":
            print(x)

#Preposition
def find_preposition():
    for x in doc:
        if x.pos_ == "ADP":
            print(x)

#Conjuction     
def find_conjuction():
    for x in doc:
        if x.pos_ == "CONJ" or x.pos_ == "SCON":
            print(x)

#Interjection
def find_interjection():
    for x in doc:
        if x.pos_ == "INTJ":
            print(x)

#Punctuation
def find_punctuation():
    for x in doc:
        if x.pos_ == "PUNCT":
            print(x)

#Articles/Determiners
def find_determiners():
    for x in doc:
        if x.pos_ == "DET":
            print(x)


#create more functionality using space like find pronoun, adverbs etc.