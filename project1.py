#weather project 

import tkinter as tk
import requests as rq

base_url="https://api.weatherapi.com/v1/current.json?"
api_key="your_api_key"


#function to get data

def get_weather():
    city=city_entry.get()

    params={
        "q":city,
        "key":api_key,
        "units":"metric"

       
        
    }

    #send request

    response=rq.get(base_url,params=params)
    data=response.json()
    #print(data)

    if "current" in data:
        temp=data["current"]["temp_c"]
        condition=data["current"]["condition"]["text"]
        output_label.config(text=f"Temperature: {temp}°C\nCondition: {condition}")
    else:
        output_label.config(text="City not found. Please try again.")






#gui of the app
root=tk.Tk()
root.title("weather app")
root.geometry("400x300")
root.config(bg="#369C9C")

#top label

top_label=tk.Label(root,text="weather app",font=("Georgia",20))
top_label.pack(pady=10)

#city label

city_label=tk.Label(root,text="enter the city",font=("Georgia",14))
city_label.pack(pady=10)

#entry

city_entry=tk.Entry(root,font=("Arial",14))
city_entry.pack(pady=10)

submit_button=tk.Button(root,text="submit",font=("Arial",15),command=get_weather)
submit_button.pack(pady=10)

#output

output_label=tk.Label(root,font=("Arial",14))
output_label.pack(pady=10)



root.mainloop()
