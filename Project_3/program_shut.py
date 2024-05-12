from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logOut():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")


root = Tk()
root.title("ShutDown App")
root.geometry("500x500")
root.config(bg="black")


r_button = Button(root,text="Restart",font=('The New Roman',20,'bold'),bg='orange',fg="black",relief=RAISED,cursor="plus", command=restart)
r_button.place(x=150,y=60,height=50,width=200)



r2_button = Button(root,text="Restart Time",font=('The New Roman',20,'bold'),bg='orange',fg="black",relief=RAISED,cursor="plus",command=restart_time)
r2_button.place(x=150,y=150,height=50,width=200)


L_O = Button(root,text ="Log-Out",font=("The New Roman",20,"bold"),bg="orange",fg='black',relief=RAISED,cursor='plus',command=logOut)
L_O.place(x=150,y=240,height=50,width=200)


st_button = Button(root,text ="Shut-Down",font=("The New Roman",20,"bold"),bg="orange",fg='black',relief=RAISED,cursor='plus',command=shutdown)
st_button.place(x=150,y=330,height=50,width=200)





















root.mainloop()