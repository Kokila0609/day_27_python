from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=100)

#Labels
label1 = Label(text="is equal to")
#label1.config(text="This is new text")
label1.grid(row=2, column=1)

label2 = Label(text="0")

label2.grid(row=2, column=2)


label3 = Label(text="Km")
#label1.config(text="This is new text")
label3.grid(row=2, column=3)

label3 = Label(text="Miles")
#label1.config(text="This is new text")
label3.grid(row=0, column=3)

# Buttons
def action():
    Miles = float(entry.get())
    
    kilometers = round((Miles*1.60934))
    label2.config(text=f"{kilometers}")

# #calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=3, column=2)

#Entries
kilometers =  0
entry = Entry(text = kilometers, width=10)
#Add some text to begin with    

#Gets text in entry

entry.grid(row=0, column=2)





window.mainloop()

