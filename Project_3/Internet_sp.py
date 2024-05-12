import speedtest

from tkinter import *

# def speedcheck():
#    sp = speedtest.Speedtest()
#    sp.get_servers()
#    down = str(round(sp.download()/(10**6),3)) + "Mbps"
#    upload = str(round(sp.upload()/(10**6),3)) + "Mbps"
#    lab_3.config(text=down)
#    lab_5.config(text=upload)

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    upload = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lab_3.config(text=down)
    lab_5.config(text=upload)






root = Tk()
root.title("Speed_test")
root.geometry('500x500')
root.config(bg="black")



lab_1 = Label(root,text='Internet Speed Test', font = ('The New Roman',20,'bold'),bg='black',fg='white')
lab_1.place(x=50,y=40,height=50,width=380)


lab_2 = Label(root,text ='Download Speed', font=('The New Roman',20,'bold'))
lab_2.place(x=50,y=120,height=50,width=380)

lab_3 = Label(root,text='00', font=("The New Roman",20,'bold'),bg='black',fg='white')
lab_3.place(x=50,y=200,height=50,width=380)

lab_4 = Label(root,text="Upload Speed",font=('The New Roman',20,'bold'))
lab_4.place(x=50,y=280,height=50,width=380)

lab_5 = Label(root,text='00', font=("The New Roman",20,'bold'),bg='black',fg='white')
lab_5.place(x=50,y=360,height=50,width=380)


button = Button(root,text='Check Speed',font=('The New Roman',20,'bold'),bg='orange',fg='black',command=speedcheck)
button.place(x=50,y=420,height=50,width=380)



root.mainloop()

