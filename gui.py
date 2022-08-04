from tkinter import *

# * ------> all

# object of tkinter
window = Tk()

window.title('gui')



# textbox
# label
# button

# label
Label(window,text = 'Hello from GUI',bg='red',fg = 'black').grid(row = 0,column=0)

# textbox

textbox = Entry(window,width = 50,bg = 'white').grid(row = 0,column=1)

# button


Button(window,text = 'Submit',command = 'click',bg = 'black',fg = 'white',width = 20 ).grid(row = 1,column=1)


# output
output = Text(window,width = 30,height = 10,bg = 'white')
output.grid(row = 1, column=2)








# dict

my_dict = {
    'animal':['cow','lion'],
    'code':['logic op']
}




window.mainloop()





