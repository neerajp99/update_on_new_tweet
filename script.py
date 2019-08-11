import requests
from selenium import webdriver
import time
import sys
import os
import smtplib
# from smtplib import SMTP
from bs4 import BeautifulSoup

def check_for_tweet():
    # url for the target twitter page
    twitter_url = "https://twitter.com/css"
    # details of the browser that's acting as a user. change this according to your browser
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    # make a call with the twitter url and the provided header
    twitter = requests.get(twitter_url, headers = headers)
    # scrap the data from that url page
    soup = BeautifulSoup(twitter.content, 'html.parser')
    # find the exact tweets field from the url page
    tweets_count = soup.find('span',{
        'class':'ProfileNav-value'
        }).get_text()
    # number of tweets from that page
    tweets_count = tweets_count.replace(',', '').strip()

    initial_tweets_file = open('initialTweets.txt', 'r+')
    #Checking if the input file is empty and adding the number of tweets to it
    if not initial_tweets_file:
        print('The input file is empty')
        exit()
    else:
        initial_tweets_count = initial_tweets_file.read().strip()

    # count of tweets added
    count = int(tweets_count) - int(initial_tweets_count)

    # conditional statement to check if there is new tweet(s) added
    if (tweets_count > initial_tweets_count):
        # if there is a new twwet, email the user regarding it
        mail_user(count)
        # update the text file with the new tweet count
        initial_tweets_file_new = open('initialTweets.txt', 'w+')
        # for word in initial_tweets_file_new:
        #     word = word.replace(initial_tweets_count, str(tweets_count))
        #     initial_tweets_file_new.write(word)
        initial_tweets_file_new.write(tweets_count)
        initial_tweets_file_new.close()
        print("An email has been with the number of new tweets added!")

    initial_tweets_file.close()

def mail_user(count):
    # create a SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # identify ourselves as an ecrypted connection
    server.ehlo()
    # call starttls to start TLS for security
    server.starttls()
    # identify ourselves as an ecrypted connection
    server.ehlo()
    # user authentication credentials
    server.login("senders_email", "gmail_password or google_app_password")
    # the message you want to send
    message = f"{count} new tweet(s) has been added by ABC channel on twitter."
    # this sends the email
    server.sendmail("senders_email", "receivers_email", message)
    #terminate the sessions
    server.quit()

check_for_tweet()
