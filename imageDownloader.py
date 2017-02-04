# a simple python script that downloads an image from a given url

import random
import urllib2

def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib2.urlopen(url, full_name)

download_image('https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-0/p110x80/16299535_608833925986107_637764608560895145_n.jpg?oh=51eb8668b4b98b3a44e7ad4eed544379&oe=59056B7A')
