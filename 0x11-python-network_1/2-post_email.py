#!/usr/bin/python3
"""akes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    value = {"email": argv[2]}
    request = Request(
            argv[1], urlencode(value).encode("ascii"))
    with urlopen(request) as response:
        head = response.headers.get('X-Request-Id')
        print(response.read().decode('utf-8'))
