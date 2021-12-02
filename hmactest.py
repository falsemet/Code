import hmac

message=b'hello world!'
salt=b'secret'
hash=hmac.new(message,salt,digestmod='SHA1')
print(hash.hexdigest())