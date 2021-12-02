import subprocess

print('$ nslookup www.python.com')
r=subprocess.call(['nslookup','www.python.com'])
print('Exit code:',r)


m=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=m.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('exie code:',m.returncode)
