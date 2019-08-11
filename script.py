import requests
from selenium
import webdriver
import time
import sys
import os
from bs4 import BeautifulSoup

twitter_url = "https://twitter.com/css"
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
page = requests.get(twitter_url, headers = headers)
soup = BeautifulSoup(page.content, 'twitter-data')
