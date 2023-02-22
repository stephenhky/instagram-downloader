
import logging
import getpass
import re
import urllib
from PIL import Image

import instaloader


def main():
    L = instaloader.Instaloader()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    L.login(username, password)

    done = False
    while not done:
        posturl = input('URL: ')
        if len(posturl) <= 0:
            done = True
            continue
        matcher = re.match('https://www.instagram.com/p/([A-Za-z0-9]+)', posturl)
        if matcher is not None:
            shortcode = matcher.group(1)
            logging.info('shortcode: {}'.format(shortcode))
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            for node in post.get_sidecar_nodes():
                logging.info(node.display_url)
                img = Image.open(urllib.request.urlopen(node.display_url))
                img.show()


if __name__ == '__main__':
    main()
