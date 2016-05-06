# This script checks your Amazon.fr wishlist and sends an email if
# some of the books are below a certain maximum limit.
#
# TODO: refactor and cleanup this rough version.

import mechanize
import re
from bs4 import BeautifulSoup
from locale import *


def send_mail(from_address, to_address, subject, text):
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
    server_ssl.login('Bart.Vandewoestyne@gmail.com', 'EFBCED919')
    server_ssl.sendmail(from_address, to_address, message)
    server_ssl.close()

browser = mechanize.Browser()
browser.set_handle_robots(False)

response = browser.open("https://www.amazon.fr/gp/sign-in.html")
browser.select_form("signIn")
browser.form['email'] = 'Bart.Vandewoestyne@telenet.be'
browser.form['password'] = 'SomePassword'
browser.submit()

PRICE_LIMIT = 25
setlocale(LC_NUMERIC, '')
wishlist_page = browser.open("https://www.amazon.fr/gp/registry/wishlist/1YNQGVVG7J07D/ref=topnav_lists_1")
soup = BeautifulSoup(wishlist_page.read(), 'html.parser')
books = soup.find_all("a", class_="a-link-normal a-declarative", id=re.compile("^itemName_"))
book_dict = {}
email_text = ""
for book in books:
    div_element = book.parent.parent.parent.parent
    second_price = div_element.find("span", class_="a-color-price itemUsedAndNewPrice")
    splitted_price = second_price.string.split()
    if atof(splitted_price[1]) < PRICE_LIMIT:
        email_text += "'" + book.string.strip() + "'" + " costs " + splitted_price[1] + " EUR!\n"
    book_dict[book.string.strip()] = second_price.string.strip()

if email_text:
    sorted_books = sorted(book_dict.items(), key=lambda x: x[1])
    email_text += "\nWishlist sorted by price:\n"
    email_text += "-------------------------\n"
    for book in sorted_books:
        email_text += book[1] + "  " + book[0] + "\n"
    send_mail("Bart.Vandewoestyne@telenet.be",
              "Bart.Vandewoestyne@telenet.be",
              "Cheap book available alert!",
              email_text)
