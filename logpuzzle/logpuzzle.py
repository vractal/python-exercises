#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    host = filename[(filename.find("_")+1):]
    logs = ""
    puzzle_urls = []
    with open(filename) as file:
        logs = file.read()

    for url in re.findall(r'GET.*HTTP',logs):
        if re.match(r'.*puzzle.*',url):
            complete_url = "http://" + host+url[4:-5]
            if complete_url not in puzzle_urls:
                puzzle_urls.append(complete_url)

    puzzle_sorted = sorted(puzzle_urls,key=lambda x: x[-8:])

    return puzzle_sorted



def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    count = 0
    dir = os.path.abspath(dest_dir)
    if not os.path.exists(dir):
        os.makedirs(dir)


    for url in img_urls:
        name = "img" + str(count) + ".jpg"
        file = os.path.join(dir,name)
        urllib.request.urlretrieve(url,file)
        count += 1

    with open(os.path.join(dir,"index.html"),"w") as f:
        img = ''
        for i in range(0,count):
            img +='<img src="img%s.jpg">' %(i)

        template = '<html><body>%s</body></html>'%(img)
        f.write(template)
    # +++your code here+++



def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
