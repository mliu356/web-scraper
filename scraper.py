import requests

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# print(page.status_code) # 200 = success

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")

# how to do for one period
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="temp").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
desc = tonight.find("img")['title']

# how to do in general
periods = [pt.get_text() for pt in seven_day.select(".tombstone-container .period-name")]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

import pandas as pd
weather = pd.DataFrame({"period": periods, "short_desc": short_descs, "temp":
    temps, "desc": descs})
print(weather)






# how to access a single p tag (dataquest.io):
# html = list(soup.children)[2] #html body = 3rd element of list made by parser
# body = list(html.children)[3]
# p = list(body.children)[1]
# print(p.get_text())