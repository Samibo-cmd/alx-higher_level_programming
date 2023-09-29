#!/usr/bin/python3
"""Evaluates candidates applying for a back-end position
with multiple technical challenges"""


if __name__ == "__main__":
    from sys import argv
    from requests import get

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    commits = get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
