import base64

def safe_base64_decode(s):
    if len(s)%4==0:
        return base64.b64decode(s)
    else:
        m=len(s)%4
        return base64.b64decode(s+m*('='))


assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')