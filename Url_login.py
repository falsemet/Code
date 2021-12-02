from urllib import request,parse

print("Login in discord.com...")
email=input('Email: ')
passwd=input('Password: ')
login_data=parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry',''),
    ('client_id',''),
    ('savedata','1'),
    ('ec',''),
    ('pagerefer','')
])
req=request.Request('https://www.discord.com/login')
req.add_header('origin','')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34')
req.add_header('referer','')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',f.read().decode('utf-8'))