#!/usr/bin/python3

'''

Find the user's daily horoscope, scraped from horoscope.com

Usage:

./get_horoscope.py <astrological sign>

'''

from sys import argv
import requests
from lxml import html


def get_horoscope(sign=None):
    signs = {
        "aries": 1,
        "taurus": 2,
        "gemini": 3,
        "cancer": 4,
        "leo": 5,
        "virgo": 6,
        "libra": 7,
        "scorpio": 8,
        "sagittarius": 9,
        "capricorn": 10,
        "aquarius": 11,
        "pisces": 12
    }
    if sign == None:
        print("Usage:\n ./get_horoscope.py <astrological sign>")
        return
    s = signs.get(sign.lower())
    url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={}".format(str(s))
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # horoscope = tree.xpath('//div[@class="horoscope-content"]/text()')
    horoscope = tree.xpath('//p/text()')
    print(sign, horoscope[1], end='')


if __name__ == "__main__":
    get_horoscope(argv[1])
