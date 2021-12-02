import re

def name_of_email(addr):
    f=re.match(r'<([a-zA-Z0-9\s]+)>[a-zA-Z0-9\s]+|([a-zA-Z0-9\s]+)\@[a-z\.]+',addr)
    if f:
        m=f.groups()
        if m[0]!=None:
            print (m[0])
        elif m[0]==None:
            print (m[1])

def split_email(addr):
    m=re.split(r'[\<\>\@]+',addr)
    print (m)

name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
split_email('<Tom Paris> tom@voyager.org')
split_email('tom@voyager.org')