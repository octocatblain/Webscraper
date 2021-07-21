from bs4 import BeautifulSoup
from sys import displayhook

import bs4
import requests
import pandas as pd

#the page to be scraped
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")


soup = BeautifulSoup(page.content, 'html.parser') #parsing the page content

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0] #contains all information to be extracted

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

#use print function (commented in Comments below) to test if code is working

#print(period)
#print(short_desc)
#print(temp)

img = tonight.find("img") #extract the title attribute from the img tag
desc = img['title'] #attribute passed as key

#print(desc)

period_tags = seven_day.select(".tombstone-container .period-name") #Selects all items with the clas<<period-name>> inside an item with the class<<tombstone-container>> in the variable<<seven_day>>
periods = [pt.get_text() for pt in period_tags] # list comprehension to call the get_text method on each BeautifulSoup object

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

#print(short_descs)
#print(temps)
#print(descs)

#pandas library calls the DataFrame class, and passes in each list of items 
#they are passed in as part of a dictionary
#Each dictionary key will become a column in the DataFrame, and each list will become the values in the column
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
df = pd.DataFrame(weather)

# displaying the DataFrame
displayhook(df)

    ##using a regular expression and the Series.str.extract method to pull out the numeric temperature values
#temp_nums = weather["temp"].str.extractall()
#weather["temp_num"] = temp_nums.astype('int')

    ##finds the mean of all the high and low temperatures:
#weather["temp_num"].mean()

#is_night = weather["temp"].str.contains("Low")
#weather["is_night"] = is_night.replace

#print (period)
#print (short_desc)
#print (temp)
#print (desc)
#print (temp_nums)
#print (is_night.replace)

