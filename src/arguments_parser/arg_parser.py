import argparse
import sys

parser = argparse.ArgumentParser(description='Get app information from the Google Play store')
input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument(
    '-u', 
    '--url', 
    metavar='URL', 
    action='append',
    type=str, 
    help='URL from a specific application'
)
input_group.add_argument(
    '-c', 
    '--category', 
    metavar='CATEGORY', 
    action='append',
    choices=[
        'ART_AND_DESIGN',
        'BEAUTY',
        'LIBRARIES_AND_DEMO',
        'HOUSE_AND_HOME',
        'WEATHER',
        'FOOD_AND_DRINK',
        'SHOPPING',
        'COMMUNICATION',
        'BUSINESS',
        'PARENTING',
        'EDUCATION',
        'DATING',
        'ENTERTAINMENT',
        'SPORTS',
        'LIFESTYLE',
        'EVENTS',
        'TOOLS',
        'FINANCE',
        'PHOTOGRAPHY',
        'COMICS',
        'BOOKS_AND_REFERENCE',
        'MAPS_AND_NAVIGATION',
        'MEDICAL',
        'MUSIC_AND_AUDIO',
        'NEWS_AND_MAGAZINES',
        'PERSONALIZATION',
        'PRODUCTIVITY',
        'VIDEO_PLAYERS',
        'HEALTH_AND_FITNESS',
        'SOCIAL',
        'TRAVEL_AND_LOCAL',
        'AUTO_AND_VEHICLES',
        'ANDROID_WEAR',
    ],
    type=str, 
    help='apps from the first page of the selected category'
)
mode_group = parser.add_mutually_exclusive_group(required=True)
mode_group.add_argument(
    '-v',
    '--verbose',
    action='store_true',
    help='print the results on screen'
)
mode_group.add_argument(
    '-o',
    '--outfile',
    metavar='FILENAME',
    nargs='?', 
    type=argparse.FileType('w'),
    default=sys.stdout,
    help='stores the collected information in the specified file'
)

arguments = parser.parse_args()