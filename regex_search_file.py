import os
import re

file_open=open('file.txt','r')

data=file_open.read()

try :

    regx_in= input('Enter the regular expression')

    match=re.search(regx_in,data)

    if match !='None':
        match_all=re.findall(regx_in,data)
        print('result :'+ str(match_all))

except IOError as e :
    print('unable to find file ')

