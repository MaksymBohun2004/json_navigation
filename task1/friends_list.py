import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


# downloaded from https://www.py4e.com/code3/


def fr_list():
    """
    Returns a JSON file of user's friends list by receiving a username
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print('')
    acct = input('Enter Twitter Account:')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    with open('file_file.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
