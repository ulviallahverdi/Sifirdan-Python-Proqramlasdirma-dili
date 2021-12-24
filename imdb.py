import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Rating-i yazin:"))

basliqlar = soup.find_all("td",{"class":"titleColumn"})
ratinqler = soup.find_all("td",{"class","ratingColumn imdbRating"})


for basliq, rating in zip(basliqlar,ratinqler):
    basliq = basliq.text
    rating = rating.text

    basliq = basliq.strip()
    basliq = basliq.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Filmin adi: {} Filmin Reytinqi: {}".format(basliq,rating))

    
