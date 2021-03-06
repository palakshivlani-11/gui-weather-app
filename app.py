from tkinter import *
import tkinter as tk
from datetime import datetime
from PIL import ImageTk,Image
import requests
from tkinter import messagebox

class Weather():
  def weather_report(self):
    self.url="http://api.openweathermap.org/data/2.5/weather?q="
    self.cityname=self.loc.get(1.0,END)
    self.api_key='864b926b2e4c1174a58588f503eb21fc'
    self.data=requests.get(self.url+self.cityname+'&appid='+self.api_key).json()

    if self.data['cod']=='404':
      messagebox.showerror('Error','City Not Found !!')
    else:
      self.location['text']=self.data['name']+","+self.data['sys']['country']
      self.c=self.data['main']['temp_max']-273.15
      self.f=self.c*9/5+32
      self.weather['text']=self.data['weather'][0]['main']
      self.weather['font']=('verdana',20,'bold')
      self.temperature['text'] = f'{self.c}°C \n {self.f}°F'
      self.temperature['font'] = ('verdana',15,'bold')
      self.humidity['text'] = self.data['main']['humidity']
      self.humidity['font'] = ('verdana',15,'bold')
      self.pressure['text'] = self.data['main']['pressure']
      self.pressure['font'] = ('verdana',15,'bold')
  
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry('500x300')
    self.root.title("Weather Application")
    self.root.maxsize(500,300)
    self.root.minsize(500,300)

    self.header = Label(self.root,width=100,height=2,bg="#66ffff")
    self.header.place(x=0,y=0)

    self.font = ('verdana',10,'bold')

    self.date = Label(self.root,text=datetime.now().date(),bg="#66ffff",fg="black",font=self.font)
    self.date.place(x=400,y=5)

    self.heading = Label(self.root,text="Weather Report",bg="#66ffff",fg="black",font=self.font)
    self.heading.place(x=180,y=5)

    self.location = Label(self.root,text="NA-/",bg="#66ffff",fg="black",font=self.font)
    self.location.place(x=10,y=5)

    self.name = Label(self.root,text="City or Country Name",fg="black",font=self.font)
    self.name.place(x=140,y=45)

    self.loc = Text(self.root,width=25,height=2)
    self.loc.place(x=140,y=70)

    self.button = Button(self.root,text="Search",bg="#66ffff",fg="black",font=self.font,relief=RAISED,borderwidth=3,command=self.weather_report)
    self.button.place(x=350,y=73)

    self.line1 = Label(self.root,bg="#66ffff",width=20,height=0)
    self.line1.place(x=0,y=150)
    self.line2 = Label(self.root,bg="#66ffff",width=20,height=0)
    self.line2.place(x=360,y=150)

    self.report = Label(self.root,text="Weather Report",bg="#66ffff",fg="black",font=self.font,padx=10)
    self.report.place(x=180,y=150)

    self.weather = Label(self.root,text="NA/-",fg="black",font=self.font)
    self.weather.place(x=90,y=230)

    self.temperature = Label(self.root,text="NA/-",fg="black",font=self.font)
    self.temperature.place(x=200,y=230)

    self.humidity = Label(self.root,text="NA/-",fg="black",font=self.font)
    self.humidity.place(x=310,y=230)

    self.pressure = Label(self.root,text="NA/-",fg="black",font=self.font)
    self.pressure.place(x=380,y=230)

    self.root.mainloop()



if __name__ == '__main__':
   Weather()



     
    
