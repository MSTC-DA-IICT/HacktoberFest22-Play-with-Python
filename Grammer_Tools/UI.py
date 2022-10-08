from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog

from main import *
#import functions from main

root = Tk()
root.title("Grammer Tools")

#resize the tkinter window and design it using your creativity

def open_file():
    #take file from the user as input
    file_type = ['.txt']
    file = filedialog.askopenfile()
    #next read the content from the file and pass it to get_text()
    if file is not None:
        get_text(file.read()) 

#Create an input box to take 'text' as input from the user

def call_find_feature(feature):
    if feature == "Noun":
        return find_noun
    elif feature == "Pronoun":
        return find_pronoun
    elif feature == "Adverb":
        return find_adverbs
    elif feature == "Adjective":
        return find_adjectives
    elif feature == "Preposition":
        return find_preposition
    elif feature == "Conjuction":
        return find_conjuction
    elif feature == "Interjection":
        return find_interjection
    elif feature == "Determiner":
        return find_determiners
    elif feature == "Punctuation":
        return find_punctuation
    
    #call find_noun function from main    

#create an upload button for user to upload his text
#create a button for calling open_file function
open_btn = Button(root, text ='Open', command = open_file)
open_btn.pack()

#Stores all the feature finding buttons
buttons = {}

#List of all features
feature_finder = ["Noun","Pronoun","Adverb","Adjective","Preposition","Conjuction",
            "Interjection","Determiner","Punctuation"]

for i in feature_finder:
    buttons[i] = Button(root, text=i,command=call_find_feature(i))
    buttons[i].pack()

root.mainloop()