#!/usr/bin/python3
"""reducer.py"""

import sys

current_year = 0
current_country = ''
cnt = 0

first_row = True

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input you got from mapper.py
    year, country, _ = line.split('\t')

    if first_row:
        first_row = False
        current_year = year
        current_country = country

    if (current_year != year or current_country != country) and (first_row is False):
        print(current_year+'\t'+current_country+'\t'+str(cnt))
        cnt = 0
        current_year = year
        current_country = country

    cnt = cnt +1

print(current_year+'\t'+current_country+'\t'+str(cnt))

