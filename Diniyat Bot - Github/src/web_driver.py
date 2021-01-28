import requests
from bs4 import BeautifulSoup



class WebScraper():
    def __init__(self):
        self.site = requests.get("https://iec-houston.org/")
        self.soup = BeautifulSoup(self.site.content, 'html.parser')

    def fajr_time(self):
        fajr = self.soup.find('li', class_='fjar_time')
        fajr_time = fajr.find('span', class_='prayer_time')
        return fajr_time.text

    def sunrise_time(self):
        sunrise = self.soup.find('li', class_='sunrise_time')
        sunrise_time = sunrise.find('span', class_='prayer_time')
        return sunrise_time.text

    def dhuhr_time(self):
        dhuhr = self.soup.find('li', class_='dhuhr_time')
        dhuhr_time = dhuhr.find('span', class_='prayer_time')
        return dhuhr_time.text

    def asr_time(self):
        asr = self.soup.find('li', class_='asr_time')
        asr_time = asr.find('span', class_='prayer_time')
        return asr_time.text

    def maghrib_time(self):
        maghrib = self.soup.find('li', class_='maghrib_time')
        maghrib_time = maghrib.find('span', class_='prayer_time')
        return maghrib_time.text

    def isha_time(self):
        isha = self.soup.find('li', class_='isha_time')
        isha_time = isha.find('span', class_='prayer_time')
        return isha_time.text



