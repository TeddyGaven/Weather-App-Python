#Python Mini-Project
#Weather App

#required modules
#geopy --> used to get latitudes and longitudes
#timezonefinder --> used to get the timezones of different places
#pytz --> enables timezone calculations

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim  #Nominatim uses OpenStreetMap data to find locations on Earth by name and address (geocoding)
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz    #enables timezone calculations


#Generating the main screen
root = Tk()   #using tkinter
root.title("Weather App")  #title of main page
root.geometry("900x700")   #dimensions of main page
root.resizable(False,False) #cannot resize the window
canvas1 = Canvas(root, width=900,height=700)  #creating canvas
canvas1.pack(fill = "both", expand = True)  
bg = PhotoImage(file="bg.png")   #giving the canvas a background image
canvas1.create_image(0,0, image = bg, anchor="nw") #nw=northwest/it is a anchor constant

#defining our weather function
def getWeather():
    try:    #try this first
        city=textfield.get()    #giving the text typed inside the search box to a variable named city
    
        geolocator= Nominatim(user_agent="geoapiExercises")     #initializing geolocator, Suppose if city is mumbai
        location = geolocator.geocode(city)         #giving the city name to geolocator.geocode(mumbai)  ...this will store the location of mumbai in a variuable called location   
        obj= TimezoneFinder()   #initializing obj variable to TimezoneFinder() module
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)   #will give the time zone at the specified latitude and longitude
        
        #to print it on the main page in place of clock and name...line no 66
        home=pytz.timezone(result)  #will calculate the timezone of city ..mumbai as per my example
        local_time=datetime.now(home)      #will store the current time in a variable named local_time
        current_time = local_time.strftime("%I:%M %p")    #srtftime is a module of python which returns various time related data...%I=hours as 0 added decimal, %M = minutes as zero added decimal, %p= Will give Am or Pm
        clock.config(text=current_time)     #(line no 109)      #putting the value of current_time in  clock  ...config will put the value in the specified label
        name.config(text="CURRENT WEATHER") #(line no 107)   #putting this text in name ...config will put the value in the specified label
        
        #weather
        #fetching the weather API
        api= "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4465035e268b46fd63f004f30f4e8caf"  #passing our city variable into the api Query to get the data of the city in searchbox
        
        json_data = requests.get(api).json()  #request the data in the api and convert it to json, Store this json is json_data
        
        #Store all the required data from the json in these variables
        condition = json_data['weather'][0]['main']    
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        #appending all of our stored values one by one on the main screen
        #putting the values in the text that will appear next to the image ...config will put the values in the specified labels
        t.config(text=(temp,"°"))  #(line no 129)
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°")) #(line no 131)
        
        #putting the values in the text that will appear in the bottom box ...config will put the values in the specified labels
        w.config(text=wind) #(line no 135)
        h.config(text=humidity) #(line no 137)
        d.config(text=description) #(line no 139)
        p.config(text=pressure) #(line no 141)
    
    except Exception as e:   #if input is wrong show this error in a message box
        messagebox.showerror("Weather App","Invalid Input!")    #a message box will pop on the screen if there is any error
        
#End of the function
                                                    
#Placing the elements on the User Interface   

#search box
search_img = PhotoImage(file="searchbgS.png")  #bringing an image
myimg = Label(image=search_img)  #making a label
myimg.place(x=30,y=20)  #placing it on the canvas 

#putting a text field inside the search box
textfield = tk.Entry(root,justify="center",width=20,font=("poppins",25,"bold"),bg="black",border=0,fg="yellow", insertbackground="yellow")    #fg=foreground colour(Changes colour of the text) of button,  insertbackground=changes cursor colour
textfield.place(x=60,y=24)    #making and placing a textfield on the page
textfield.focus()

#putting a search icon inside the search box
search_icon = PhotoImage(file="search-icon.png")   #bringing an image
myimg_icon = Button(image=search_icon, borderwidth=0,cursor="hand2",bg="yellow",command=getWeather)  #putting a button in the search bar, getWeather function will be called on clicking this
myimg_icon.place(x=390,y=30)   #placing the button on the correct coordinates


#Logo
logo_img = PhotoImage(file="Weather-Live-Logo.png")    
logo=Label(image=logo_img)     #making the logo 0f the app
logo.place(x=50,y=180)

#Bottom Box
box_img = PhotoImage(file="boxB.png")
frame_myimg = Label(image=box_img)  #making the bottom box
frame_myimg.place(x=50,y=520,) 


#putting clock and name ..the function will print the values of clock and name here
#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=40,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=40,y=130)



#label text inside of Bottom Blue Box
label1 = Label(root,text="WIND", font=("Helvetica",17,'bold'),fg="white", bg="skyblue")
label1.place(x=100,y=540)

label2 = Label(root,text="HUMIDITY", font=("Helvetica",17,'bold'),fg="white", bg="skyblue")
label2.place(x=240,y=540)

label3 = Label(root,text="DESCRIPTION", font=("Helvetica",17,'bold'),fg="white", bg="skyblue")
label3.place(x=400,y=540)

label4 = Label(root,text="PRESSURE", font=("Helvetica",17,'bold'),fg="white", bg="skyblue")
label4.place(x=600,y=540)


#Text that will appear next to the image
t=Label(font=("ariakl",70,"bold"),fg="#ee666d")
t.place(x=420,y=180)
c=Label(font=("arial",15,'bold'))
c.place(x=420,y=280)

#Text that will appear in the Bottom Box
w = Label(text="...",font=("arial",20,"bold"),bg="skyblue")
w.place(x=120,y=580)
h = Label(text="...",font=("arial",20,"bold"),bg="skyblue")
h.place(x=280,y=580)
d = Label(text="...",font=("arial",20,"bold"),bg="skyblue")
d.place(x=460,y=580)
p = Label(text="...",font=("arial",20,"bold"),bg="skyblue")
p.place(x=650,y=580)


root.mainloop() #execute tkinter