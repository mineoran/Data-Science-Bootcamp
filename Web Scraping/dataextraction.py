from tkinter import N
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    url = 'https://www.indeed.com/jobs?q=data%20analyst&l=United%20States&start={page}&vjk=19e020dcfeffa883'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup #With this soup object, you can navigate and search through the HTML for data that you want.

def transform(soup):
    divs = soup.find_all('div', class_ = "job_seen_beacon") # ilk sayfada class="job_seen_beacon" eşleşen div sayısı> 15
    for item in divs:
        company = item.find('span',class_ ="companyName").text.strip()
        title = item.find(class_ ="jobTitle").text.strip()
        location =item.find(class_ = "companyLocation").text.strip()
        posted_date =item.find(class_ ="date").text.strip('')
        summary = item.find('div',class_="job-snippet").text.strip().replace('\n','')
        try:
            salary =item.find('div', class_ = "attribute_snippet").text.strip()
        except:
            salary = ''


        job = {
        'company': company,
        'title': title,
        'location':location,
        'job posted date':posted_date,
        'job salary':salary,
        'summary':summary
        }
        joblist.append(job)
    return


joblist = []
for i in range(0,15,15):
    print(f'Getting page,{i}')
    c = extract(10)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())

df.to_csv('dataanalyst.csv')