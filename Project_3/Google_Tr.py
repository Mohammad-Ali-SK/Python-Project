from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def change(text="type",src ="English",dest= 'Hindi'):
    text1 = text
    src1 =src
    dest1 =dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = combo_sor.get()
    d = combo_dest.get()
    msg = sor_text.get(1.0,END)
    textget = change(text=msg,src=s,dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)
    
    
    

root = Tk()
root.title("ali_translator")
root.geometry("500x650")
root.config(bg="black")

# Heading-Translate
lab_text = Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg='black',fg='white')
lab_text.place(x=100,y=30,height=100,width=270)

# Frame
frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(root,text="Source Text",font=("Time New Roman",15,"bold"),fg="white",bg='black')
lab_text.place(x=100,y=110,height=24,width=270)

# Enter Text Area
sor_text = Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
sor_text.place(x=10,y=140,height=200,width=480)

# Select Languag
list_text = list(LANGUAGES.values())
combo_sor =ttk.Combobox(frame,value=list_text)
combo_sor.place(x=10,y=350,height=30,width=100)
combo_sor.set("english")


# Button
button_change =Button(frame,text="Translate", font = ("Time New Roman",10,"bold"),relief=RAISED,bg='red',fg='black',command=data)
button_change.place(x=120,y=350,height = 30, width = 100)

# destination
combo_dest = ttk.Combobox(frame,value =list_text)
combo_dest.place(x=230,y=350,height=30,width=100)
combo_dest.set("english")

# dest sor_text
dest_text = Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
dest_text.place(x=10,y=400,height=200,width=480)


root.mainloop() 