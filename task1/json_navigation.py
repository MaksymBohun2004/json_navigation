"""
This module is used to work with twitter API
"""
import json
import sys
import user_timeline
import friends_list
import os


def parse_file(file):
    """
    Turns the json file to a dict
    """
    with open(file, 'r', encoding='utf-8') as json_file:
        info = json.load(json_file)
    return info


def work_with_dict(dct, filename):
    """
    Receives a JSON dictionary and helps the user navigate it
    """
    print("Here are all available keys:")
    numkey = 1
    keys = {}
    for key in dct.keys():
        print(f'{numkey}. {key}')
        keys[numkey] = key
        numkey += 1
    print(f'Choose which object of the list you want to work with(numbers 1 to {len(dct)}):')
    print('If you want to go back, input -1')
    while True:
        num = input('>>> ')
        try:
            num = int(num)
            if num == -1:
                start_work(filename)
            if 0 < num <= len(dct):
                break
        except ValueError:
            pass
    if type(dct[keys[num]]) is list or type(dct[keys[num]]) is dict:
        check_if_dict(dct[keys[num]], filename)
    else:
        print(dct[keys[num]])
    print('If you want to end work with the program, press Enter')
    print('If you want to go back, input -1')
    ans = str(input())
    if ans == '-1':
        start_work(filename)
    else:
        sys.exit()


def check_if_dict(data, filename):
    """
    Receives data and turns it into a JSON dict for
    other functions to work with
    """
    if isinstance(data, list):
        print(f'This object is a list with {len(data)} objects')
        print(f'Choose which object of the list you want to work with(numbers 1 to {len(data)}):')
        while True:
            num = input('>>> ')
            try:
                num = int(num)
                if 0 < num <= len(data):
                    num = num - 1
                    break
            except ValueError:
                pass
            print(f'Incorrect input, try again(numbers 1 to {len(data)}):')
        work_with_dict(data[num], filename)
    elif isinstance(data, dict):
        print(f'This object is a dictionary with {len(data)} objects')
        work_with_dict(data, filename)
    else:
        check_if_dict(json.loads(data), filename)


def start_work(filename):
    """
    Calls the parsing function and starts the navigation in the parsed file
    """
    info = parse_file(filename)
    check_if_dict(info, filename)


def main():
    """
    Introduces the user to the program and gives 2 options:
    1) Navigate an existing JSON file
    2) Generate a new JSON file using the Twitter API
    """
    print('Welcome to JSON Navigator!')
    print('If you have a JSON file you would like to navigate, enter 1:')
    print('If you want to generate a JSON file using Twitter API, enter 2:')
    while True:
        num = input('>>> ')
        try:
            num = int(num)
            if num == 1 or num == 2:
                break
        except ValueError:
            pass
        print(f'Incorrect input, try again(1 or 2):')
    if num == 1:
        while True:
            print('Enter path to file:')
            filename = input('>>> ')
            try:
                start_work(filename)
            except FileNotFoundError:
                pass
            print('Something went wrong. Try entering path to file again:')
    else:
        print('If you want to generate user timeline, enter 1:')
        print('If you want to generate friends list, enter 2:')
        while True:
            num = input('>>> ')
            try:
                num = int(num)
                if num == 1 or num == 2:
                    break
            except ValueError:
                pass
            print(f'Incorrect input, try again(1 or 2):')
        if num == 1:
            user_timeline.us_timeline()
            try:
                start_work('file_file.json')
            except:
                os.remove('file_file.json')
        else:
            friends_list.fr_list()
            try:
                start_work('file_file.json')
            except:
                os.remove('file_file.json')


if __name__ == "__main__":
    main()

