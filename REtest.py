#!/bin/env python3
import re
def is_valid_email(addr):
    f=re.match(r'^([0-9a-zA-Z\.]+)\@([0-9a-zA-Z]+\.[a-z]+)$',addr)
    #
    print f.group(0)       
    return f
    
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

