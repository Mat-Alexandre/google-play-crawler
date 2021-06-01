import requests
from bs4 import BeautifulSoup

def get_app_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    app_name = soup.find('h1', class_='AHFaub', itemprop='name').get_text()
    developer = soup.find('a', class_='hrTbp R8zArc').get_text()
    category = soup.find('a', class_='hrTbp R8zArc', itemprop='genre').get_text()
    rating = soup.find('span', class_='AYi5wd TBRnV').get_text().replace(',','')
    classification = soup.find('div', class_='BHMmbe').get_text().replace(',','')
    updated = soup.select(
        '#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(3) > div.W4P4ne > div.JHTxhe.IQ1z0d > div > div:nth-child(1) > span > div > span'
    )[0].get_text()
    size = soup.select(
        '#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(3) > div.W4P4ne > div.JHTxhe.IQ1z0d > div > div:nth-child(2) > span > div > span'
    )[0].get_text()
    installs = soup.select(
        '#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(3) > div.W4P4ne > div.JHTxhe.IQ1z0d > div > div:nth-child(3) > span > div > span'
    )[0].get_text().replace(',','')
    version = soup.select(
        '#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(3) > div.W4P4ne > div.JHTxhe.IQ1z0d > div > div:nth-child(4) > span > div > span'
    )[0].get_text()
    min_android_ver = soup.select(
        '#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div > main > c-wiz:nth-child(3) > div.W4P4ne > div.JHTxhe.IQ1z0d > div > div:nth-child(5) > span > div > span'
    )[0].get_text().split(' ')[0]

    return {
        'app_name': app_name,
        'developer': developer,
        'category': category,
        'rating': rating,
        'classification': classification,
        'updated': updated,
        'size': size,
        'installs': installs,
        'version': version,
        'min_android_ver': min_android_ver
    }
