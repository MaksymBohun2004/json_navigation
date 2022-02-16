import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json


# downloaded from https://www.py4e.com/code3/


def us_timeline():
    """
    Returns a JSON file of user's timeline by receiving a username
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    acct = input('Enter Twitter Account:')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    with open('file_file.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)