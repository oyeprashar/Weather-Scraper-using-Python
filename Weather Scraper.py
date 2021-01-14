import pandas as pd
import requests, time
from bs4 import BeautifulSoup

count = 0

while 1:
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.XxWVcSgzbIU")
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id='seven-day-forecast-list')
    items = week.find_all(class_='tombstone-container')

    period_names=[item.find(class_='period-name').get_text() for item in items]
    short_description=[item.find(class_='short-desc').get_text() for item in items]
    temp_names=[item.find(class_='temp').get_text() for item in items]

    weather_stuff = pd.DataFrame({
        'period':period_names,
        'short_description': short_description,
        'temperature':temp_names,
        })
    weather_stuff.to_csv('weather.csv')
    #count is used to know how many times the CSV has been updated
    count+=1
    print(count)
    #time.sleep() is used to give a delay so that we dont overload the website
    time.sleep(2)