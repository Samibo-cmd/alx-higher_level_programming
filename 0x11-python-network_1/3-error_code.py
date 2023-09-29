#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the response"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv
    from urllib.error import HTTPError

    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code:', error.code)
