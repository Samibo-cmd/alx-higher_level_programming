#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the
passed URL with the email, and finally displays the body"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)
