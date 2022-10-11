

from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st
#import functions from main
from main import get_text,find_noun

#create tkinter window.
root = Tk()
root.title("Grammer Tools")

#variale to store the data
data = ''

#take the data from uploaded file
def open_file():
    #take file from the user as input
    global data
    file_type = [('text files', '*.txt')]
    filename = filedialog.askopenfilename(filetypes=file_type)
    if filename:
        #print the path in the dilog box
        pathh.insert(END, filename)
        filename = open(filename)  # or tf = open(tf, 'r')
        data = filename.read()
        #next read the content from the file and pass it to get_text()
        get_text(data)
        filename.close()
    

def Take_input():
    #take input from the text box and call get_text
    global data
    data = inputtxt.get("1.0", "end-1c")
    if not data=='':
        get_text(data)


def call_function_from_main():
    if data == '':
        return
    # For functionality implementation
    text = v.get()
    #call find_noun function from main
    txtarea.insert(END,str(find_noun()))
     
    

#resize the tkinter window and design it using your creativity
root.geometry("450x630")
root['bg']='#182747'

#....................................Frame 0: For heading..............................................
frame = Frame(root,bg='#C98474')
frame.pack(pady=10)
l = Label(frame,text = "Grammer Tools",font=('Times New Roman', 16),bg='#C98474')
l.pack(padx=(140,140),pady=(0,0))

#....................................Frame 1: Take text as input.......................................
#Create an input box to take 'text' as input from the user
frame1 = Frame(root,bd=2, 
    bg='#E8DFCA',
    relief=SOLID)
frame1.pack(pady=10)
#create label for instruction to user
l = Label(frame1,text = "Enter the text below and click on submit. ",font=('Times New Roman', 12),bg='#E8DFCA')
l.grid(row=0, column=0, sticky=W,padx=10,pady=(20,0))

#textbox
inputtxt = Text(frame1, height = 10,
                width = 37,bd=1,relief=SOLID)
inputtxt.grid(row=1, column=0, sticky=W,padx=(10,15),pady=(0,20))
 
#create an upload button for user to upload the text
Display = Button(frame1, height = 1,
                 width = 10,
                 text ="Submit",
                 command = lambda:Take_input(),relief=SOLID,bd=1)
Display.grid(row=1, column=1, sticky=W,padx=(0,20))


#........................................Frame 2: For taking the file as input........................................
#display the path for file selected
frame2 = Frame(root,bd=2, 
    bg='#E8DFCA',
    relief=SOLID)
frame2.pack(pady=(10,30))

#label for instruction
l = Label(frame2,text = "Click on open file button to select the text file ",font=('Times New Roman', 12),bg='#E8DFCA')
l.grid(row=0, column=0, sticky=W,padx=(10,0),pady=(20,0))

#show the file path of selected path
pathh = Entry(frame2,width=50,bd=1,relief=SOLID)
pathh.grid(row=1, column=0, sticky=W,padx=(10,15),pady=(0,20))

#create a button for calling open_file function
Button(
    frame2, height=1,width=10,
    text="Open File", 
    command=open_file,relief=SOLID,bd=1).grid(row=1, column=1, sticky=W,pady=(0,20),padx=(0,20))


#..........................................Frame 3: Grammar Functionality..............................................
frame3 = Frame(root,bd=2, 
    bg='#E8DFCA',
    relief=SOLID)
frame3.pack(pady=10)

#label for instruction
l = Label(frame3,text = "What do you wamt to find?:",font=('Times New Roman', 12),bg='#E8DFCA')
l.grid(row=0, column=0, sticky=W,padx=(10,0),pady=(20,0))

# List to create multiple buttons
values = ["Noun","Pronoun","Adverb","Adjective","Verb","Preposition","Conjuction","Interjection","Punctuation","Determiners"]
# Tkinter string variable able to store any string value
v = StringVar(frame3, "Noun")
# Create Dropdown menu
drop = OptionMenu( frame3 , v , *values)
drop.config(bg='#ffffff',bd=0,width=10)
drop.grid(row=1,column=0,sticky=W,padx=(10,0))

# Create button, it will call the function from main
b=Button( frame3 , height=1, width=10, text = "Find" , command = call_function_from_main, relief=SOLID, bd=1)
b.grid(row=1,column=0,sticky=W,padx=(150,0))

#answer label
l = Label(frame3,text = "Answer",font=('Times New Roman', 14),bg='#E8DFCA')
l.grid(row=2, column=0, sticky=W,padx=(0,0),pady=(10,0))

#textarea for displaying the answer returned from the main
txtarea = st.ScrolledText(frame3, width=51 ,height=15)
txtarea.grid(row=3, column=0, sticky=W)


root.mainloop()
