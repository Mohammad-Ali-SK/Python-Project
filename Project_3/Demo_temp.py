from tkinter import *
from tkinter import ttk
import requests

def weather():
   city = city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cb84423847e333e76eafdb9b7dd9364a").json()
   w_lable1.config(text=data["weather"][0]['main'])
   wd_lable1.config(text=data['weather'][0]['description'])
   wt_lable1.config(text=int(data['main']['temp']-273.15))
   wp_lable1.config(text=data['main']['pressure'])
   
   




win = Tk()
win.title("Weather_app")
win.geometry("500x600")
win.config(bg='black')


name_lable = Label(win,text='Weather App',font=("Time New Roman",30),bg='red',fg='white')
name_lable.place(x=50,y=40,height=50,width=400)

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name = StringVar()
com = ttk.Combobox(win,font=("Time New Roman",15),values=list_name,textvariable=city_name)
com.place(x=50,y=120,height=50,width=400)





w_lable = Label(win,text="Weather Cliemate :",font=("Time New Roman",15),bg='black',fg='white')
w_lable.place(x=50,y=300,height=30,width=200)
w_lable1 = Label(win,text="Cloudy",font=("Time New Roman",10),bg='black',fg='white')
w_lable1.place(x=250,y=300,height=30,width=200)


wd_lable = Label(win,text="Weather Description :",font=("Time New Roman",15),bg='black',fg='white')
wd_lable.place(x=50,y=360,height=30,width=200)
wd_lable1 = Label(win,text="Sunny and Worm",font=("Time New Roman",10),bg='black',fg='white')
wd_lable1.place(x=250,y=360,height=30,width=200)


wt_lable = Label(win,text="Temp :",font=("Time New Roman",15),bg='black',fg='white')
wt_lable.place(x=50,y=420,height=30,width=200)
wt_lable1 = Label(win,text="42c",font=("Time New Roman",10),bg='black',fg='white')
wt_lable1.place(x=250,y=420,height=30,width=200)

wp_lable = Label(win,text="Pressure :",font=("Time New Roman",15),bg='black',fg='white')
wp_lable.place(x=50,y=480,height=30,width=200)
wp_lable1 = Label(win,text="34%",font=("Time New Roman",10),bg='black',fg='white')
wp_lable1.place(x=250,y=480,height=30,width=200)

done_button = Button(win,text="Done",font=('Time New Roman',20,'bold'),bg="red",fg='white',relief=RAISED,command=weather)
done_button.place(x=200,y=210,height=50,width=100)








win.mainloop()
