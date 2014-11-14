from __future__ import print_function

__author__ = 'Alex Kim'

from bs4 import BeautifulSoup
import requests
import re
import json
import sys


homepage = 'http://cnn.com'

cnn = requests.get(homepage)
page = BeautifulSoup(cnn.text)

# YYYY/MM/DD/Category/(subcategory)/title
cnn_links = page.find_all('a', attrs={'href': re.compile(r"/[0-9]{4}/[0-9]{2}/[0-9]{2}/[a-zA-Z]*/")})


def process_links(links):
    output = []
    for i in links:

        try:
            article = dict(
                title = None,
                alt = None,
                link = "/".join([homepage,i.attrs['href']]),
            )
            if i.span:
                article['title'] = i.span.contents[0]
            elif i.img:
                article['alt'] = i.img.attrs['alt']
            else:
                article['title'] = i.contents[0]

            article['category'] = article['link'].split('/')[7]
        except Exception as e:
            # Catch malformed links, in the event of inconsistencies or CNN changing their formatting.
            print("WARNING: Malformed Link; '{}'; '{}'".format(repr(e), i), file=sys.stderr)

        output.append(article)

    return json.dumps({"codes":output}, indent=2)

print(process_links(cnn_links))