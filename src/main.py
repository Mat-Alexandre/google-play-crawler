import csv, sys
import requests
import os.path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from apps_categories import apps_url_dict

BASE_URL = 'https://play.google.com'
COMT_URL = '&showAllReviews=true'
CURR_URL = ''
HREF_LIST = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
}

def update_csv_file(category_name):
    """
    Atualiza o arquivo .csv com as informações correspondentes ao Banco de Dados. 
    Caso o arquivo não exista, ele será criado no diretório atual com o cabeçalho corresponddente. 
    ex.: 
    título do aplicativo;
    nome do desenvolvedor;
    categoria do app;
    número de avaliações;
    avaliação do aplicativo;
    tamanho do aplicativo.
    """

    global CURR_URL

    # Abrindo a CURR_URL + COMT_URL com o selenium e executando o geckodriver
    driver = webdriver.Firefox(executable_path=os.getcwd() + "/geckodriver/geckodriver.exe")
    
    driver.get(CURR_URL+""+COMT_URL)
    comment_page = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    file_name_1 = "bd_"+category_name+".csv"
    file_name_2 = "bd_"+category_name+"_comments.csv"
    
    # Verificando se o arquivo .csv correspondente às informações do app existe e cria as colunas da table
    if(os.path.exists(file_name_1) == False):
        with open(file_name_1, "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(['Titulo', 'Desenvolvedor', 'Categoria', 'Num_Avaliacoes', 'Avali_Media', 'Tamanho'])

    # Verificando se o arquivo .csv correspondente às informações dos comentários existe
    if(os.path.exists(file_name_2) == False):
        with open(file_name_2, "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow(['UNome', 'ULink_Foto', 'Avali_App', 'Data_Comentario', 'Avali_Comentario', 'Resenha', 'Aplicativo'])
    
    # Pegando as informações da página inicial
    page = requests.get(CURR_URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Salvando as informações dos apps no file_name_1
    with open(file_name_1, "a") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        
        app_title = soup.find("h1", class_="AHFaub", itemprop="name").get_text()
        dev_name = soup.find("a", class_="hrTbp R8zArc").get_text()
        app_cat = soup.find("a", class_="hrTbp R8zArc", itemprop="genre").get_text()
        eval_tmp = soup.find("span", class_="AYi5wd TBRnV")
        if eval_tmp == None:
            eval_ = 0
        else:
            eval_ = int(eval_tmp.get_text().replace(",",""))
        
        rate_tmp = soup.find("div", class_="BHMmbe")
        if rate_tmp == None:
            rate = 0
        else:
            rate = float(rate_tmp.get_text().replace(",",""))
            
        size = soup.find_all("span", attrs={"class": "htlgb"})[3].get_text()

        csv_writer.writerow([app_title, dev_name, app_cat, eval_, rate, size])
    
    soup = BeautifulSoup(comment_page, 'html.parser')
    
    # Separando somente a seção de comentários do html
    comment_section = soup.find_all("div", jsmodel="y8Aajc", jscontroller="H6eOGe")

    # Salvando as informações dos comentários
    with open(file_name_2, "a") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

        for num, comment in enumerate(comment_section):
            if(num < 10):
                # Seção de comentários
                user_name = comment.find("span", class_="X43Kjb").get_text()
                user_link = comment.find("img", class_="T75of ZqMJr")['src']
                user_comment_rate = int(comment.find("div", class_="pf5lIe").div['aria-label'][13])
                comment_date = comment.find("span", class_="p2TkOb").get_text()
                comment_eval = int(comment.find("div", class_="jUL89d y92BAb").get_text())
                full_comment = comment.find("span", jsname="bN97Pc").get_text()

                csv_writer.writerow([user_name, user_link, user_comment_rate, comment_date, comment_eval, full_comment, app_title])
            else:
                # Recolher no máximo 4 comentários para cada aplicativo
                break


def main(arg):
    global HREF_LIST
    global CURR_URL

    category = int(arg[1])
    cat_name = apps_url_dict[category][0]
    APPS_URL = apps_url_dict[category][1]

    page = requests.get(APPS_URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Todos os links de apps da APPS_URL
    HREF_LIST = soup.find_all(attrs={"class":"JC71ub"}, href=True)

    # Para todos os apps em APPS_URL
    for href in HREF_LIST:
        try:
            CURR_URL = BASE_URL + "" + href['href']
            update_csv_file(cat_name)
        except InvalidArgumentException as iae:
            print(iae)
    

if __name__ == '__main__':
    main(sys.argv)