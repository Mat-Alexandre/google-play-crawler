import json
import requests
from bs4 import BeautifulSoup
from crawler.url_categories import APPS_CATEGORIES_URL
from crawler.crawler import get_app_info
from arguments_parser.arg_parser import arguments

def main():
    results = []
    if arguments.url:
        results.append(get_app_info(arguments.url[0]))
    elif arguments.category:
        APPS_URL = APPS_CATEGORIES_URL[arguments.category[0]]
        page = requests.get(APPS_URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        HREF_LIST = soup.find_all(attrs={"class":"JC71ub"}, href=True)
        BASE_URL = 'https://play.google.com'
        for href in HREF_LIST:
            results.append(get_app_info(BASE_URL+href['href']))
    
    if arguments.verbose:
        print('The information about the app(s) given the specified url:')
        for result in results:
            print(result, '\n')
    elif arguments.outfile:
        with open(file=arguments.outfile.name, mode=arguments.outfile.mode) as file:
            file.write('[\n')
            for num, result in enumerate(results):
                json.dump(result, file, indent=4)
                if num < len(results) - 1:
                    file.write(',\n')
            file.write('\n]')

if __name__ == '__main__':
    main()