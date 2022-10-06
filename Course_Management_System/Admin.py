from tkinter import *
from PIL import *
from numpy import *


root = Tk()
root.title("Course Management System")

lbl_title = Label(root)

Main_frame = Frame(root)

upper_frame = LabelFrame(Main_frame)



# Department ''

# Create dropdown list to select the department of the student

# Name
lbl_Name = Label(upper_frame)


# Address field

# Email ''

# DOB ''

# Join Date ''

# Id proof ''

# gender ''

# Phone no ''

# State ''

# City ''

# Functions ''

def show_data():
    # Show the data from tyhe data file student_data.csv   

def clear_tree():
    # clear the inputted data

def save_data():
    # save the inputed data by admin

def delete():
    # Delete specific data    

# Button frame

# Save button

# Update Button

# Delete Button

# Clear Button

# Show data button (show data from data base)

#  down frame to show the data

# Use tree view from pandas
root.mainloop()