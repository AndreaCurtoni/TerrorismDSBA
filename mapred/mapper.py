#!/usr/bin/python3 

"""mapper.py""" 

import sys 

for line in sys.stdin: 
    line = line.strip() 
    elements = line.split(",") 
    year = elements[1] 
    country = elements[2] 
    print(year+'\t'+country+'\t'+'1' )
