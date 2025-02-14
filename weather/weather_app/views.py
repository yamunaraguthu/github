from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def home(request): 
          
    if 'city' in request.POST:
        city = request.POST['city']
    else:
         city ='indore'     
     
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=767c1905e7ab50e9f6751515fd1e7d46'
    params = {'units':'metric'}

    API_KEY =  'AIzaSyBPIvqCUFEGHd9FuxO6cqgW9W-vG3AbRiQ'
    SEARCH_ENGINE_ID = '22ec9abca78c5406a'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url=f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge'

    data = requests.get(city_url).json()
    count =0
    search_items = data.get("items")
    image_url=search_items[0].get('link',"image_url")if search_items and len(search_items)>1 else"image_url"
       

    try:
          
       data = requests.get(url,params).json()
       description = data['weather'][0]['description']
       icon = data['weather'][0]['icon']
       temp = data['main']['temp']
       day = datetime.date.today()
           
       return render(request,'index.html',{'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city , 'exception_occurred':False ,'image_url':image_url})

    except:
        exception_occurred = True
        messages.error(request,'Entered data is not available to API')   
        day = datetime.date.today()

        return render(request,'index.html',{'description':'clear sky', 'icon': '01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':exception_occurred})
               
    # get('link',"default_image_url")if search_items and len(search_items)>1 else"default_image_url"
    