import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = tkinter.Label(text = "Im a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.grid(column=1, row=1)

#my_label["text"] = "New Text"
#my_label.config(text="New Text")

#Buttons
def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

my_button = tkinter.Button(text = "click me", command = button_clicked)
my_button.grid(column=2, row =2)

new_button = tkinter.Button(text = "New Button")
new_button.grid(column=3, row =1)

#Entry

# def entry_updated():
#     new_text = input.get()
#     # input.insert(0,new_text)
#     # my_label.config(text = new_text)

input = tkinter.Entry(width=25)

input.grid(column=4, row=3)






window.mainloop()
