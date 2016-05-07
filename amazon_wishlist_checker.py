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
# TODO: refactor some more (extract functions)

import mechanize
import re
from bs4 import BeautifulSoup
from locale import *
import argparse

PRICE_LIMIT = 20


def send_mail(from_address, to_address, subject, text, smtp_login, smtp_pwd):

    import smtplib

    message = "\r\n".join([
        "From: %s",
        "To: %s",
        "Subject: %s",
        "",
        "%s"
    ]) % (from_address, to_address, subject, text)
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo()
    server_ssl.login(smtp_login, smtp_pwd)
    server_ssl.sendmail(from_address, to_address, message)
    server_ssl.close()


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Your email address", required=True)
    parser.add_argument("-al", "--amazon_login", help="Your Amazon login name", required=True)
    parser.add_argument("-ap", "--amazon_pwd", help="Your Amazon password", required=True)
    parser.add_argument("-gl", "--google_login", help="Your Google email address", required=True)
    parser.add_argument("-gp", "--google_pwd", help="Your Google password", required=True)

    return parser.parse_args()


def amazon_login(email, password):

    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    browser.open("https://www.amazon.fr/gp/sign-in.html")
    browser.select_form("signIn")
    browser.form['email'] = email
    browser.form['password'] = password
    browser.submit()

    return browser


def main():

    args = parse_arguments()
    browser = amazon_login(args.amazon_login, args.amazon_pwd)
    
    setlocale(LC_NUMERIC, '')

    wishlist_page = browser.open("https://www.amazon.fr/gp/registry/wishlist/1YNQGVVG7J07D/ref=topnav_lists_1")
    soup = BeautifulSoup(wishlist_page.read(), 'html.parser')
    books = soup.find_all("a", class_="a-link-normal a-declarative", id=re.compile("^itemName_"))

    # Find cheap books
    book_dict = {}
    cheap_books = ""
    for book in books:
        div_element = book.parent.parent.parent.parent
        second_price = div_element.find("span", class_="a-color-price itemUsedAndNewPrice")
        splitted_price = second_price.string.split()
        if atof(splitted_price[1]) < PRICE_LIMIT:
            cheap_books += "'" + book.string.strip() + "'" + " costs only " + "{:.2f}".format(atof(splitted_price[1])) + " EUR!\n"
        book_dict[book.string.strip()] = atof(splitted_price[1])
    
    # Sort all the books from your wishlist by price.
    sorted_books = sorted(book_dict.items(), key=lambda x: x[1])

    # Build up the text for the email and screen output.
    email_text = ""
    if cheap_books:
        email_text += "\nBooks that you consider cheap:\n"
        email_text += "------------------------------\n"
        email_text += cheap_books
    email_text += "\nWishlist sorted by price:\n"
    email_text += "-------------------------\n"
    for book in sorted_books:
        email_text += "{:6.2f}".format(book[1]) + " EUR  " + book[0] + "\n"

    print email_text.encode('utf-8')
    
    # Send mail if there are cheap books available.
    if cheap_books:
        send_mail(args.email,
                  args.email,
                  'Cheap book available alert!',
                  email_text.encode('utf-8'),
                  args.google_login,
                  args.google_pwd)
    

if __name__ == "__main__":

    main()
