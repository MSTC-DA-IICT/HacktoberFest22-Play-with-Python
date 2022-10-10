

from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st
#import functions from main

root = Tk()
root.title("Grammer Tools")

def open_file():
    #take file from the user as input
    file_type = [('text files', '*.txt')]
    filename = filedialog.askopenfilename(filetypes=file_type)
    pathh.insert(END, filename)
    filename = open(filename)  # or tf = open(tf, 'r')
    data = filename.read()
    filename.close()
    #next read the content from the file and pass it to get_text()

def Take_input():
    #print the text user submitted in terminal.
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    txtarea.configure(state ='disabled')

def call_find_noun():
    pass
    #call find_noun function from main   

#resize the tkinter window and design it using your creativity
root.geometry("450x630")
root['bg']='#182747'

frame = Frame(root,bg='#C98474')
frame.pack(pady=10)
l = Label(frame,text = "Grammer Tools",font=('Times New Roman', 16),bg='#C98474')
l.pack(padx=(140,140),pady=(0,0))

#Create an input box to take 'text' as input from the user
frame1 = Frame(root,bd=2, 
    bg='#E8DFCA',
    relief=SOLID)
frame1.pack(pady=10)
l = Label(frame1,text = "Enter the text below and click on submit. ",font=('Times New Roman', 12),bg='#E8DFCA')
l.grid(row=0, column=0, sticky=W,padx=10,pady=(20,0))
inputtxt = Text(frame1, height = 10,
                width = 37,bd=1,relief=SOLID)
inputtxt.grid(row=1, column=0, sticky=W,padx=(10,15),pady=(0,20))
 
#create an upload button for user to upload his text
Display = Button(frame1, height = 1,
                 width = 10,
                 text ="Submit",
                 command = lambda:Take_input(),relief=SOLID,bd=1)
Display.grid(row=1, column=1, sticky=W,padx=(0,20))

#display the path for file selected
frame2 = Frame(root,bd=2, 
    bg='#E8DFCA',
    relief=SOLID)
frame2.pack(pady=(10,30))
l = Label(frame2,text = "Click on open file button to select the text file ",font=('Times New Roman', 12),bg='#E8DFCA')
l.grid(row=0, column=0, sticky=W,padx=(10,0),pady=(20,0))
pathh = Entry(frame2,width=50,bd=1,relief=SOLID)
pathh.grid(row=1, column=0, sticky=W,padx=(10,15),pady=(0,20))

#create a button for calling open_file function
Button(
    frame2, height=1,width=10,
    text="Open File", 
    command=open_file,relief=SOLID,bd=1).grid(row=1, column=1, sticky=W,pady=(0,20),padx=(0,20))

#display the text of the text file selected
# Add a Scrollbar(horizontal)
frame3 = Frame(root,bd=2, 
    bg='#E8DFCA',
    relief=SOLID)
frame3.pack(pady=10)
l = Label(frame3,text = "Answer",font=('Times New Roman', 14),bg='#E8DFCA')
l.grid(row=0, column=0, sticky=W,padx=(0,0))
txtarea = st.ScrolledText(frame3, width=51 ,height=20)
txtarea.grid(row=1, column=0, sticky=W)


root.mainloop()
