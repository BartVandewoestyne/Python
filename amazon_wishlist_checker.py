# Do you have a book wishlist on http://www.amazon.fr ?  Did you know that the
# prices of second handed books vary quite a lot and are sometimes quite low?
# Maybe you want to know when the prices are low, but without having to check
# the website every day?  Automation to the resque!
#
# This script checks your Amazon.fr wishlist and sends you an email if the
# price of certain books drop below a certain limit.  You can run it daily from
# a cronjob so you'll always get notified when some book in your wishlist drops
# below a certain price.
#
# TODO: this is only a very rough first draft.  We should clean it up
#       and refactor it.

import mechanize
import re
from bs4 import BeautifulSoup
from locale import *
import argparse

PRICE_LIMIT = 20


def send_mail(args, subject, text):

    import smtplib

    message = "\r\n".join([
        "From: %s",
        "To: %s",
        "Subject: %s",
        "",
        "%s"
    ]) % (args.email, args.email, subject, text)
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo()
    server_ssl.login(args.google_login, args.google_pwd)
    server_ssl.sendmail(args.email, args.email, message)
    server_ssl.close()


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Your email address", required=True)
    parser.add_argument("-al", "--amazon_login", help="Your Amazon login name", required=True)
    parser.add_argument("-ap", "--amazon_pwd", help="Your Amazon password", required=True)
    parser.add_argument("-gl", "--google_login", help="Your Google email address", required=True)
    parser.add_argument("-gp", "--google_pwd", help="Your Google password", required=True)

    return parser.parse_args()


def amazon_login(args):

    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    browser.open("https://www.amazon.fr/gp/sign-in.html")
    browser.select_form("signIn")
    browser.form['email'] = args.amazon_login
    browser.form['password'] = args.amazon_pwd
    browser.submit()

    return browser


def main():

    args = parse_arguments()
    browser = amazon_login(args)
    
    setlocale(LC_NUMERIC, '')
    wishlist_page = browser.open("https://www.amazon.fr/gp/registry/wishlist/1YNQGVVG7J07D/ref=topnav_lists_1")
    soup = BeautifulSoup(wishlist_page.read(), 'html.parser')
    books = soup.find_all("a", class_="a-link-normal a-declarative", id=re.compile("^itemName_"))
    book_dict = {}
    cheap_books = ""
    for book in books:
        div_element = book.parent.parent.parent.parent
        second_price = div_element.find("span", class_="a-color-price itemUsedAndNewPrice")
        splitted_price = second_price.string.split()
        if atof(splitted_price[1]) < PRICE_LIMIT:
            cheap_books += "'" + book.string.strip() + "'" + " costs only " + "{:.2f}".format(atof(splitted_price[1])) + " EUR!\n"
        book_dict[book.string.strip()] = atof(splitted_price[1])
    
    sorted_books = sorted(book_dict.items(), key=lambda x: x[1])
    email_text = ""
    if cheap_books:
        email_text += "\nBooks that you consider cheap:\n"
        email_text += "------------------------------\n"
        email_text += cheap_books
    email_text += "\nWishlist sorted by price:\n"
    email_text += "-------------------------\n"
    for book in sorted_books:
        email_text += "{:6.2f}".format(book[1]) + " EUR  " + book[0] + "\n"
    
    if cheap_books:
        send_mail(args,
                  'Cheap book available alert!',
                  email_text.encode('utf-8'))
    
    print email_text.encode('utf-8')


if __name__ == "__main__":

    main()
