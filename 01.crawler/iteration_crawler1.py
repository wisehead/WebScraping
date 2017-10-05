# -*- coding: utf-8 -*-


import itertools
from common import download


def iteration():
    for page in itertools.count(1):
        #url = 'http://example.webscraping.com/view/-{}'.format(page)
        url = 'http://example.webscraping.com/places/default/view/-{}'.format(page)
		#url = 'http://example.webscraping.com/places/default/view/-%d' % page
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            print html
            pass


if __name__ == '__main__':
    iteration()
