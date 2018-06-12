#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import pprint
import mmap



"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] lista and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a lista starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """


    rank_names = {}
    names_rank = {}
    lista  = []

    with open(filename) as file:
        data = mmap.mmap(file.fileno(),0,prot=mmap.PROT_READ)
        year = re.search(br'>Popularity\D*(?P<year>\d*)<',data).group('year').decode()
        names = re.finditer(br'<td>(?P<rank>\d*)</td><td>(?P<male>[a-zA-Z]*)</td><td>(?P<female>[a-zA-Z]*)</td>\s*',data)


    for match in names:
        rank_names[match.group('rank').decode()]= (
                                                    match.group('male').decode(),
                                                    match.group('female').decode())
        names_rank[match.group('male').decode()] = match.group('rank').decode()
        names_rank[match.group('female').decode()] = match.group('rank').decode()

    for name in names_rank:
        lista_input = " ".join([name, names_rank[name]])
        lista.append(lista_input)

    lista.append(year)
    lista.sort()
    return lista



def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]


    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    output = []
    for arg in args:

        try:
            for item in extract_names(arg):
                output.append(item)

        except:
            print("not found")

        if summary == True:
            with open("sumaryfile.txt","w") as file:
                for line in output:
                    print(line,file=file)

        else:
            for line in output:
                print(line)




if __name__ == '__main__':
    main()
