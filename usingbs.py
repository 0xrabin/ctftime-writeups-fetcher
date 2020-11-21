
from bs4 import BeautifulSoup
import requests

headers={
    'authority': 'ctftime.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9',
    }

def getWriteuplinks(taskurl):
    allmainlinks=[]
    html_content = requests.get(taskurl,headers=headers).text
    soup = BeautifulSoup(html_content, "lxml")
    table = soup.find("table", attrs={"class": "table"})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            link = "https://ctftime.org"+cols[0].find('a').get('href')
            writeuppagehtml = requests.get(link,headers=headers).text
            soup2 = BeautifulSoup(writeuppagehtml,"lxml")

            goo = soup2.find('a', attrs = {'rel':'nofollow'})
            if goo:
                writeuplink = goo.get("href")
                allmainlinks.append(writeuplink)
            else:
                writeuplink = link
                allmainlinks.append(writeuplink)
    
    return allmainlinks
           

            
    



def getNameandTask(url):
    html_content = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html_content, "lxml")
    table = soup.find("table", attrs={"class": "table"})
    rows = table.find_all('tr')


    ctflist=[]
    for row in rows:
        cols = row.find_all('td') #returns list [<td><a href="/task/13249">Suspicious</a></td>, <td>460</td>, <td>\n<span class="label label-info">forensics</span>\n</td>, <td><a href="/task/13249">2</a></td>, <td></td>]
        if(len(cols)>1):        
            tasknames = cols[0].find('a').getText()

            tasklinks = "https://ctftime.org"+cols[0].find('a').get('href')
            #print("Trying "+tasklinks)
            writeuparray = getWriteuplinks(tasklinks)

            ctfdetails={
            'name':tasknames,
            'tasklink':tasklinks,
            'writeupurls':writeuparray
            }
            ctflist.append(ctfdetails)

    print(ctflist)

#getNameandTask("https://ctftime.org/event/1118/tasks/")


# Test WriteUPFUnctions
links = getWriteuplinks("https://ctftime.org/task/13189")
print(links)
