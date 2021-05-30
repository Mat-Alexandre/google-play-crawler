# Google-Play-Crawler

Esta aplicação coleta uma série de informações sobre aplicativos na loja Google Play.

## Coletando as Informações
Certifique-se que o seu navegador é suportado pelo [selenium](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/). Caso sua versão seja compatível, ainda será necessário fazer o download do geckodriver, disponível em:
  - [Firefox](https://github.com/mozilla/geckodriver/releases)
  - [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

O local de instalação do driver é "./geckodriver/".

Para executar o crawler basta estar no diretório e especificar a url do aplicativo:
```
python crawler.py https://play.google.com/store/apps/details?id=com.github.android
```
As informações serão inicialmente disponibilizadas em dois arquivos .json, um para o aplicativo e outro para seus comentários.