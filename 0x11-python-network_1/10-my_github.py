#!/usr/bin/python3
"""Script that display a github ID based on the credentials"""
import sys

import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(r.json()['id'])
    except NameError as e:
        print(e)
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
