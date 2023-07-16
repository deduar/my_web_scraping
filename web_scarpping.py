import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

list_url = []
for i in [1,2]:
    url = "https://thehub.io/startups?industries=greentechhttps%3A%2F%2Fthehub.io%2Fstartups%3Findustries%3Dagriculture&industries=consumergoods&industries=greentech&industries=fashion&industries=food&industries=manufacturing&industries=robotics&industries=agriculture&sdgs=zeroHunger&sdgs=goodHealth&sdgs=cleanWater&sdgs=cleanEnergy&sdgs=industry&sdgs=suistainableCities&sdgs=responsibleConsumption&sdgs=climateAction&sdgs=lifeBelowWater&sdgs=lifeOnLand&page="+str(i)
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    page_url = soup.find_all("div",{"class":["card card-startup"]})
    for item in page_url:
        list_url.append("https://thehub.io"+item.find('a')['href'])
        # print(f"https://thehub.io{item.find('a')['href']}")

print(list_url)
print("****************")

# list_url = ['https://thehub.io/startups/pluto','https://thehub.io/startups/andlight']

for url in list_url:
    # ul = "https://thehub.io/startups/pluto"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    header_name = soup.find_all('h2', class_='startup-header__name')
    print(f'Name: {header_name[0].get_text()}')
    header__logo__image = soup.find_all('img', class_='startup-header__logo__image')
    print(f'Logo: {header__logo__image[0]["src"]}')
    key_value_list = soup.find_all("td",  {"class": ["key-value-list__value"]})
    for item in key_value_list:
        print(item.get_text())
    sdg__list = soup.find_all("div",  {"class": ["sdg"]})
    for item in sdg__list:
        print(item.img['src'])
    tm__list = soup.find_all("div",{"class":["card-person"]})
    for item in tm__list:
        print(item.h4.get_text().strip())
        print(item.find("div",{"class":["card-person__position"]}).get_text().strip())
        if item.find("a",{"class":["card-person__linkedin"]}):
            print(item.find("a",{"class":["card-person__linkedin"]})['href'])
    print("--------------------")
    
    