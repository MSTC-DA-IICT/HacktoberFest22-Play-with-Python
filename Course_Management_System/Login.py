from tkinter import *
from PIL import *


root = Tk()
root.geometry("500x250+0+0")
root.title("Login Page")

def login():
    # Read the data from the login.csv and if it is Student redirect to the Student Page
    # If the Admin is loged in then redirect to the Admin page    


Main_frame = Frame(root)

upper_frame = LabelFrame(Main_frame)

# Create Username field
# Create Password field

# Login button
l_button = Button(upper_frame,text="Login")


# Create Reset button
# To clear the data added

root.mainloop()