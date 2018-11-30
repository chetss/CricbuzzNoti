import requests
from bs4 import BeautifulSoup as bs

mydict = {}

def add_to_mydict(key,value):
    mydict[key] = value

def get_cric_data():
    url = 'https://www.cricbuzz.com/'

    data = requests.get(url)

    page_content = bs(data.text,"html.parser")

    # this will get you the first matches
    featured_matches= page_content.find('div',attrs={'class':'cb-mtch-blk'})
    title = featured_matches.a['title']
    batting_team = featured_matches.find('div',attrs={'class':'cb-hmscg-bat-txt'}).div.text.strip()
    bowling_team = featured_matches.find('div',attrs={'class':'cb-hmscg-bwl-txt'}).div.text.strip()
    score = featured_matches.select_one("div div:nth-of-type(2)").text
    info = featured_matches.find('div',attrs={'class':'cb-text-live'}).text.strip()

    add_to_mydict('title',title)
    add_to_mydict('batting_team',batting_team)
    add_to_mydict('bowling_team',bowling_team)
    add_to_mydict('score',score)
    add_to_mydict('info',info)
    
    return mydict

'''
def call_get_cric():
    import time
    starttime=time.time()
    while True:
        print((get_cric_data()))
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

call_get_cric()
'''
# print(get_cric_data())
# to save the content in to the html file

# with open('test.html','w') as f:
#     f.write(str(featured_matches.encode('utf-8')))