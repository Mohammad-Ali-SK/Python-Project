from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text='type',scr = 'English',des = 'Hindi'):
    text_1 = text
    scr_1 = scr
    des_1 = des
    trans = Translator()
    trans_1 = trans.translate(text,src=scr_1,dest=des)
    return trans_1.text

def getdata():
    s = combo_1.get()
    d = combo_2.get()
    msg = sor_text.get(1.0,END)
    result = change(msg,s,d)
    dest_src.delete(1.0,END)
    dest_src.insert(END,result)
    
root = Tk()
root.title('ali_translator')
root.geometry('500x650')
root.config(bg='black')


# Title
trans_lab = Label(root,text='Translator',font=('Time New Roman', 40, 'bold'), bg='black',fg='white')
trans_lab.place(x=110,y=20,height=40,width=300)

# frame
frame = Frame(root).pack(side=BOTTOM)

# lab-2
lab_2 = Label(root,text='Source text', font=('Time New Roman',13,), bg='black',fg='white')
lab_2.place(x=120,y=80,height=30,width=240)

# sor-text
sor_text = Text(frame,font=('Time New Roman',14))
sor_text.place(x=10,y=120,height=150,width=480)


# combobox
list = list(LANGUAGES.values()) 
combo_1 = ttk.Combobox(values=list)
combo_1.place(x=10,y=300,height=30,width=100)
combo_1.set('English')

# Button
button = Button(frame,text='Translate',font=('Time New Roman', 15),bg='red',fg='black',command=getdata)
button.place(x=160,y=300,height=30,width=100)

# combo-2
combo_2 = ttk.Combobox(values=list)
combo_2.place(x=300,y=300,height=30,width=100)
combo_2.set('Hindi')

lab_3 = Label(root,text="Dest text", font=('Time New Roman',12),bg='black',fg='white')
lab_3.place(x=120,y=347,height=30,width=240)

# dest_src
dest_src = Text(frame,font=('Time New Roman',14))
dest_src.place(x=10,y=400,height=200,width=480)



root.mainloop()