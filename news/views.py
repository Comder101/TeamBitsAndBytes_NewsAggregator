from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:17]

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



ot_r = requests.get("https://www.outlookindia.com/national")
ot_soup = BeautifulSoup(ot_r.content, 'html5lib')
ot_headings = ot_soup.findAll('h4')
ot_headings = ot_headings[0:15] 
ot_news = []

for oth in ot_headings:
    ot_news.append(oth.text)


def home(req):
    return render(req, 'index.html')
def categories(req):
    return render(req, 'PblProject.html', {'toi_news':toi_news, 'ot_news': ot_news})

def aboutx(req):
    return render(req, 'about.html')


