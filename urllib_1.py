from urllib import request

with request.urlopen('https://www.google.com') as f:
    data=f.read()
    print('status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s'%(k,v))
    #print('Data:',data.decode('utf-8'))


req=request.Request('https://www.google.com')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34')
with request.urlopen(req) as f:
    print('STATUS:',f.status,f.reason)
for k,v in f.getheaders():
    print('%s: %s'%(k,v))
#print('Data',f.read().decode('utf-8'))
