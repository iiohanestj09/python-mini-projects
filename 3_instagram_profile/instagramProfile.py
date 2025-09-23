import requests
from lxml import html
import re
import sys

def main(username):
    url = "https://www.instagram.com/{}/?hl=en".format(username)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[starts-with(@name, "description")]/@content')
    
    if data:
        data = data[0]
        followersMatch = re.search(r'([\d,.]+[KMB]?) Followers', data)
        followingMatch = re.search(r'([\d,.]+[KMB]?) Following', data)
        



# testing
main("cristiano")