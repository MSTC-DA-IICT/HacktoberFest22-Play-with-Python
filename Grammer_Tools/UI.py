from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
#import functions from main

root = Tk()
root.title("Grammer Tools")

#resize the tkinter window and design it using your creativity

def open_file():
    #take file from the user as input
    file_type = ['''set file type as .txt''']
    filename = filedialog.askopenfilename(filetypes=file_type)
    #next read the content from the file and pass it to get_text()

#Create an input box to take 'text' as input from the user

def call_find_noun():
    pass
    #call find_noun function from main    

#create an upload button for user to upload his text
#create a button for calling open_file function

root.mainloop()