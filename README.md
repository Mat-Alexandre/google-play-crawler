# Google Play Crawler

This is a web crawler for collect the following infos:
* App name;
* Developer;
* Category;
* Rating count;
* Classification (number of stars);
* Last time updated;
* Size of app (in MB);
* Number of installations;
* App version;
* Minimun android version required;

## Usage:
```
main.py [-h] (-u URL | -c CATEGORY) (-v | -o [FILENAME])
```

## Optional arguments:
```
  -h, --help            show this help message and exit
  -u URL, --url URL     URL from a specific application
  -c CATEGORY, --category CATEGORY
                        apps from the first page of the selected category
  -v, --verbose         print the results on screen
  -o [FILENAME], --outfile [FILENAME]
                        stores the collected information in the specified file

```

## Dependencies:
```
beautifulsoup4==4.9.3
certifi==2021.5.30
chardet==4.0.0
idna==2.10
requests==2.25.1
soupsieve==2.2.1
urllib3==1.26.5
```