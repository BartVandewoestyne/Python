# Script to download the pictures from Jennes first Communion.
#
# Run this script with Python 3.
#
# TODO:
#   - Do not store gallery.xml, but retrieve XML and process in memory.
#   - Refactor to make everything more elegant.

import os.path
import urllib.request
from xml.dom import minidom

album_base_url = "http://www.fotopauwels.be/ek2016_14u"


def main():
    gallery_xml_url = album_base_url + "/gallery.xml"
    urllib.request.urlretrieve(gallery_xml_url, 'gallery.xml')
    xml_doc = minidom.parse('gallery.xml')
    item_list = xml_doc.getElementsByTagName('image')
    nb_images = len(item_list)
    print("There are {0} images to download.".format(nb_images))
    if not os.path.exists('images'):
        os.makedirs('images')
    image_number = 1
    for s in item_list:
        image = s.attributes['imageURL'].value
        image_url = album_base_url + "/" + image
        print("Downloading image {0} of {1}: {2}... ".format(image_number, nb_images, image_url), end="")
        urllib.request.urlretrieve(image_url, image)
        print("done.")
        image_number += 1

if __name__ == "__main__":

    main()
